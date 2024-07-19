from typing import Callable, Dict, List

import numpy as np


def calculate(lst: List[int]) -> Dict[str, List]:
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst).reshape(3, 3)
    calculations: Dict[str, List]

    # Applies a function on a numpy array three times on
    # axis1, axis2 and flattened then returns them in list
    three_axes: Callable[..., List] = lambda x: [
        x(arr, axis=0).tolist(),
        x(arr, axis=1).tolist(),
        x(arr).tolist(),
    ]

    calculations = {
        "mean": three_axes(np.mean),
        "variance": three_axes(np.var),
        "standard deviation": three_axes(np.std),
        "max": three_axes(np.max),
        "min": three_axes(np.min),
        "sum": three_axes(np.sum),
    }

    return calculations
