from tipm.finance import FinancialModel, build_starlink_case, calculate


def test_users_can_vary_by_year() -> None:
    model = FinancialModel(
        years=[1, 2, 3],
        users=[10, 20, 40],
        fixed_opex=[100, 100, 100],
        revenue_per_user_year=20,
    )
    result = calculate(model)
    assert [r["users"] for r in result.yearly] == [10.0, 20.0, 40.0]
    assert result.yearly[0]["cost_per_user_year"] == 10.0


def test_empty_optional_series_are_filled() -> None:
    model = FinancialModel(years=[1, 2], users=[1, 2])
    assert len(model.capex) == 2


def test_starlink_case_runs() -> None:
    result = calculate(build_starlink_case())
    assert result.tco > 0
    assert result.discounted_cost > 0
    assert len(result.yearly) == 5
