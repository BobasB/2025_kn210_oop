import pytest

from cov.score import calculate_average, describe_result


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20


def test_result_descriptions():
    cases = [
        (100, "excellent"),
        (75, "passed"),
        (0, "failed"),
    ]
    for score, expected in cases:
        assert describe_result(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_describe_result_rejects_score_outside_range(score):
    with pytest.raises(ValueError, match="between 0 and 100"):
        describe_result(score)
