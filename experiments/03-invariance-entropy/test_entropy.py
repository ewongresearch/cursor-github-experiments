import numpy as np
from entropy import demo_system, invariance_entropy_continuous, invariance_entropy_discrete


def test_continuous_entropy_is_sum_of_unstable_real_parts():
    A = np.array([[1.0, 0.0], [0.0, -0.5]])
    assert invariance_entropy_continuous(A) == 1.0


def test_discrete_entropy_ignores_stable_modes():
    A = np.array([[0.5, 0.0], [0.0, 2.0]])
    assert np.isclose(invariance_entropy_discrete(A), np.log(2.0))


def test_demo_system_has_positive_continuous_entropy():
    A = demo_system()
    assert invariance_entropy_continuous(A) > 0
    assert invariance_entropy_discrete(A) > 0
