import sys
sys.path.insert(0, '.')
from lesson2_template import tokenize, tokenize_all


def test_tokenize_returns_list():
    r = tokenize("课程非常好，讲解清晰易懂！")
    assert isinstance(r, list)


def test_tokenize_not_empty_when_input_valid():
    r = tokenize("课程非常好")
    assert len(r) > 0


def test_tokenize_no_empty_string():
    r = tokenize("课程  非常好")
    assert all(t != "" for t in r)


def test_tokenize_all_aggregates():
    r = tokenize_all(["课程好", "讲解清晰"])
    assert isinstance(r, list)
    assert len(r) >= 2


if __name__ == "__main__":
    test_tokenize_returns_list()
    test_tokenize_not_empty_when_input_valid()
    test_tokenize_no_empty_string()
    test_tokenize_all_aggregates()
    print("lesson2 tests passed")
