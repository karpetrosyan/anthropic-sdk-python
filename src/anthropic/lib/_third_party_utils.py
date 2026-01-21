from __future__ import annotations

from typing import Any, TypeVar, Callable, cast
from functools import wraps

__all__ = ["reject_output_format_and_config"]

_F = TypeVar("_F", bound=Callable[..., Any])


def reject_output_format_and_config(func: _F) -> _F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if "output_format" in kwargs:
            raise ValueError(f"{func.__name__}() does not support 'output_format' parameter.")
        if "output_config" in kwargs:
            raise ValueError(f"{func.__name__}() does not support 'output_config' parameter.")
        return func(*args, **kwargs)

    return cast(_F, wrapper)
