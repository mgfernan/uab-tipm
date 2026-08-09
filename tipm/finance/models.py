"""Data models and validation for financial analyses."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence


def _as_float_list(name: str, values: Sequence[float], n: int) -> list[float]:
    result = [float(x) for x in values]
    if len(result) != n:
        raise ValueError(f"{name} must contain exactly {n} values")
    if any(x < 0 for x in result):
        raise ValueError(f"{name} cannot contain negative values")
    return result


@dataclass(frozen=True)
class FinancialModel:
    """Inputs for one initial-investment period followed by operating years.

    users is the average active-user forecast for each operating year. It may
    contain a different value for every year; it is not assumed constant.
    Annual figures use the same currency and are nominal unless the caller
    supplies already-escalated values.
    """

    years: Sequence[int]
    users: Sequence[float]
    initial_capex: float = 0.0
    capex: Sequence[float] = field(default_factory=list)
    fixed_opex: Sequence[float] = field(default_factory=list)
    variable_cost_per_user_year: float = 0.0
    revenue_per_user_year: float = 0.0
    other_revenue: Sequence[float] = field(default_factory=list)
    discount_rate: float = 0.10
    average_capacity_mbps: Sequence[float] = field(default_factory=list)
    residual_value: float = 0.0

    def __post_init__(self) -> None:
        n = len(self.years)
        if n == 0:
            raise ValueError("years cannot be empty")
        if list(self.years) != list(range(self.years[0], self.years[0] + n)):
            raise ValueError("years must be consecutive")
        if self.initial_capex < 0 or self.residual_value < 0:
            raise ValueError("initial_capex and residual_value cannot be negative")
        if self.variable_cost_per_user_year < 0 or self.revenue_per_user_year < 0:
            raise ValueError("per-user values cannot be negative")

        object.__setattr__(self, "years", list(self.years))
        object.__setattr__(self, "users", _as_float_list("users", self.users, n))
        object.__setattr__(self, "capex", _as_float_list("capex", self.capex or [0.0] * n, n))
        object.__setattr__(self, "fixed_opex", _as_float_list("fixed_opex", self.fixed_opex or [0.0] * n, n))
        object.__setattr__(self, "other_revenue", _as_float_list("other_revenue", self.other_revenue or [0.0] * n, n))

        if self.average_capacity_mbps:
            object.__setattr__(
                self,
                "average_capacity_mbps",
                _as_float_list("average_capacity_mbps", self.average_capacity_mbps, n),
            )
        else:
            object.__setattr__(self, "average_capacity_mbps", [0.0] * n)

        if self.discount_rate < 0:
            raise ValueError("discount_rate must be non-negative")


@dataclass(frozen=True)
class FinancialOutputs:
    """Computed yearly results and project-level indicators."""

    yearly: tuple[dict[str, float], ...]
    tco: float
    discounted_cost: float
    npv: float
    irr: float | None
    payback_years: float | None
    cumulative_cost_per_user_year: float | None
    cumulative_revenue_per_user_year: float | None
    break_even_users_per_year: float | None
