"""Reference financial scenarios used in the TIPM slides."""

from __future__ import annotations

from .models import FinancialModel


def build_starlink_case() -> FinancialModel:
    """Build a compact Starlink-like 5-year scenario for classroom exercises.

    The values are illustrative and aligned with references cited in session 04.
    """

    return FinancialModel(
        years=[1, 2, 3, 4, 5],
        users=[1.8e6, 2.3e6, 2.8e6, 3.2e6, 3.5e6],
        initial_capex=10_000_000_000,
        capex=[1_500_000_000, 1_300_000_000, 1_100_000_000, 900_000_000, 900_000_000],
        fixed_opex=[1_600_000_000, 1_750_000_000, 1_900_000_000, 2_100_000_000, 2_250_000_000],
        variable_cost_per_user_year=180,
        revenue_per_user_year=1_080,
        average_capacity_mbps=[35_000, 45_000, 55_000, 62_000, 68_000],
        discount_rate=0.10,
        residual_value=1_500_000_000,
    )
