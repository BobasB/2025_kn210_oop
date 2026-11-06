"""Helpers for evaluating a student's score."""


def calculate_average(scores: list[float]) -> float:
    """Return the average score, or zero when no scores were supplied."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def describe_result(score: float) -> str:
    """Return a text description for a score from 0 to 100."""
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "excellent"
    if score >= 60:
        return "passed"
    return "failed"

def no_covered_by_tests(score: float) -> bool:
    """Return True if the score is not covered by tests."""
    print(f"Score: {score}")
    return score < 0 or score > 100