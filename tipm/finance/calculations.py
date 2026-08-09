"""Core financial calculations."""

from __future__ import annotations

from .models import FinancialModel, FinancialOutputs


def _npv(rate: float, cashflows: list[float]) -> float:
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def _irr(cashflows: list[float]) -> float | None:
    if not (any(x < 0 for x in cashflows) and any(x > 0 for x in cashflows)):
        return None

    lo, hi = -0.999999, 10.0
    while _npv(hi, cashflows) > 0 and hi < 1e6:
        hi *= 2
    if _npv(hi, cashflows) > 0:
        return None

    for _ in range(200):
        mid = (lo + hi) / 2
        if _npv(mid, cashflows) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def calculate(model: FinancialModel) -> FinancialOutputs:
    """Calculate TCO, NPV, IRR, payback and unit economics.

    The cash-flow timeline is [year 0, operating year 1, ..., operating year N].
    Users are read independently from model.users for every operating year.
    """

    rows = []
    cashflows = [-model.initial_capex]
    cumulative_cost = model.initial_capex
    cumulative_revenue = 0.0
    cumulative_user_years = 0.0
    payback = None
    cumulative_cash = -model.initial_capex

    for i, year in enumerate(model.years):
        user_cost = model.users[i] * model.variable_cost_per_user_year
        revenue = model.users[i] * model.revenue_per_user_year + model.other_revenue[i]
        total_cost = model.capex[i] + model.fixed_opex[i] + user_cost
        net_cashflow = revenue - total_cost
        discounted_cost = total_cost / (1 + model.discount_rate) ** (i + 1)
        discounted_cashflow = net_cashflow / (1 + model.discount_rate) ** (i + 1)
        cumulative_cost += total_cost
        cumulative_revenue += revenue
        cumulative_user_years += model.users[i]

        previous_cash = cumulative_cash
        cumulative_cash += net_cashflow
        if payback is None and cumulative_cash >= 0 and net_cashflow != 0:
            payback = i + previous_cash / net_cashflow

        capacity = model.average_capacity_mbps[i]
        cost_per_user = total_cost / model.users[i] if model.users[i] else None
        cost_per_mbps_year = total_cost / capacity if capacity else None
        rows.append(
            {
                "year": float(year),
                "users": model.users[i],
                "revenue": revenue,
                "capex": model.capex[i],
                "fixed_opex": model.fixed_opex[i],
                "variable_cost": user_cost,
                "total_cost": total_cost,
                "net_cashflow": net_cashflow,
                "discounted_cost": discounted_cost,
                "discounted_cashflow": discounted_cashflow,
                "cost_per_user_year": cost_per_user,
                "cost_per_mbps_year": cost_per_mbps_year,
            }
        )
        cashflows.append(net_cashflow)

    if model.residual_value:
        cashflows[-1] += model.residual_value
        rows[-1]["residual_value"] = model.residual_value
        rows[-1]["net_cashflow"] += model.residual_value
        rows[-1]["discounted_cashflow"] += model.residual_value / (1 + model.discount_rate) ** len(model.years)

    variable_margin = model.revenue_per_user_year - model.variable_cost_per_user_year
    fixed_annual = (sum(model.fixed_opex) / len(model.fixed_opex)) + (sum(model.capex) / len(model.capex))
    break_even = fixed_annual / variable_margin if variable_margin > 0 else None

    return FinancialOutputs(
        yearly=tuple(rows),
        tco=cumulative_cost,
        discounted_cost=model.initial_capex + sum(r["discounted_cost"] for r in rows),
        npv=_npv(model.discount_rate, cashflows),
        irr=_irr(cashflows),
        payback_years=payback,
        cumulative_cost_per_user_year=cumulative_cost / cumulative_user_years if cumulative_user_years else None,
        cumulative_revenue_per_user_year=cumulative_revenue / cumulative_user_years if cumulative_user_years else None,
        break_even_users_per_year=break_even,
    )
