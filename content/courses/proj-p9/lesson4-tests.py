import sys
sys.path.insert(0, '.')
from lesson4_template import solve


def test_solve_returns_list():
    r = solve('../../datasets/teacher_metrics.csv')
    assert isinstance(r, list)


def test_solve_top_5():
    r = solve('../../datasets/teacher_metrics.csv')
    assert len(r) == 5


def test_all_strings():
    r = solve('../../datasets/teacher_metrics.csv')
    for tid in r:
        assert isinstance(tid, str)


if __name__ == "__main__":
    test_solve_returns_list()
    test_solve_top_5()
    test_all_strings()
    print("lesson4 tests passed")
