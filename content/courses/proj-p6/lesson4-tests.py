import sys
sys.path.insert(0, '.')
from lesson4_template import load_data, per_step_rates, solve


def test_solve_returns_string():
    df = load_data('../../datasets/conversion_funnel.csv')
    result = solve(df)
    assert isinstance(result, str)
    assert '_to_' in result


def test_per_step_rates_is_dict():
    df = load_data('../../datasets/conversion_funnel.csv')
    rates = per_step_rates(df)
    assert isinstance(rates, dict)
    assert len(rates) == 4


def test_bottleneck_is_lowest():
    df = load_data('../../datasets/conversion_funnel.csv')
    rates = per_step_rates(df)
    bottleneck = solve(df)
    assert rates[bottleneck] == min(rates.values())


if __name__ == "__main__":
    test_solve_returns_string()
    test_per_step_rates_is_dict()
    test_bottleneck_is_lowest()
    print("lesson4 tests passed")
