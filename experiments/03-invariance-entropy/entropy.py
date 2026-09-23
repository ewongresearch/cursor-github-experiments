"""Invariance entropy estimators for linear control systems."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def invariance_entropy_continuous(A: NDArray[np.floating]) -> float:
    eigenvalues = np.linalg.eigvals(A)
    return float(sum(max(0.0, np.real(value)) for value in eigenvalues))


def invariance_entropy_discrete(A: NDArray[np.floating]) -> float:
    eigenvalues = np.linalg.eigvals(A)
    return float(
        sum(np.log(np.abs(value)) for value in eigenvalues if np.abs(value) > 1.0)
    )


def demo_system() -> NDArray[np.floating]:
    return np.array([[0.5, 1.0], [0.0, 1.2]], dtype=float)
