"""Small reporting helpers with no third-party dependencies."""

from __future__ import annotations

from .models import FinancialOutputs


def to_dict(result: FinancialOutputs) -> dict:
    return {
        "yearly": [dict(row) for row in result.yearly],
        "tco": result.tco,
        "discounted_cost": result.discounted_cost,
        "npv": result.npv,
        "irr": result.irr,
        "payback_years": result.payback_years,
        "cumulative_cost_per_user_year": result.cumulative_cost_per_user_year,
        "cumulative_revenue_per_user_year": result.cumulative_revenue_per_user_year,
        "break_even_users_per_year": result.break_even_users_per_year,
    }


def to_csv(result: FinancialOutputs) -> str:
    if not result.yearly:
        return ""

    columns = list(result.yearly[0])
    lines = [",".join(columns)]
    for row in result.yearly:
        lines.append(",".join("" if row[c] is None else str(row[c]) for c in columns))
    return "\n".join(lines) + "\n"
