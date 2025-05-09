from git_actions_test.src.math_operations import add, sub


def test_add():
    assert add(3,5 )== 8
    assert add(10,10) == 20


def test_sub():
    assert sub(8,3) == 5
    assert sub(10,10) == 0