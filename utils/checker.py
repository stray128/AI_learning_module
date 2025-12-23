"""
Validation module for learning exercises.
Uses property-based checks that provide hints without revealing exact answers.
"""
import numpy as np
import pandas as pd
from typing import Any, Tuple, Optional, Callable
import hashlib


class Checker:
    """
    Validation helper for checking student solutions.
    Uses property-based validation to avoid revealing expected answers.
    """

    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.results = []

    def reset(self):
        """Reset the checker for a new notebook."""
        self.passed = 0
        self.failed = 0
        self.results = []

    def _result(self, passed: bool, problem: str, hint: str = ""):
        """Record and display result with optional hint."""
        self.results.append((problem, passed, hint))
        if passed:
            self.passed += 1
            print(f"\033[92m✓ {problem}: PASSED\033[0m")
        else:
            self.failed += 1
            print(f"\033[91m✗ {problem}: INCORRECT\033[0m")
            if hint:
                print(f"  💡 Hint: {hint}")

    # ==========================================
    # Basic Checks
    # ==========================================

    def is_not_none(self, value: Any, problem: str):
        """Check if value is not None."""
        if value is not None:
            self._result(True, problem)
        else:
            self._result(False, problem, "Your variable is None. Did you assign a value?")

    def is_type(self, value: Any, expected_type: type, problem: str):
        """Check if value is of expected type."""
        if isinstance(value, expected_type):
            self._result(True, problem)
        else:
            self._result(False, problem, f"Expected type: {expected_type.__name__}")

    def is_true(self, condition: bool, problem: str, hint: str = ""):
        """Check if a condition is True."""
        if condition:
            self._result(True, problem)
        else:
            self._result(False, problem, hint or "Condition not satisfied")

    def is_false(self, condition: bool, problem: str, hint: str = ""):
        """Check if a condition is False."""
        if not condition:
            self._result(True, problem)
        else:
            self._result(False, problem, hint or "Condition should be False")

    # ==========================================
    # Length and Shape Checks
    # ==========================================

    def has_length(self, container: Any, expected_length: int, problem: str):
        """Check if container has expected length."""
        try:
            actual = len(container)
            if actual == expected_length:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Expected length {expected_length}, got {actual}")
        except TypeError:
            self._result(False, problem, "Object should have a length")

    def has_shape(self, arr: Any, expected_shape: Tuple, problem: str):
        """Check if array/DataFrame has expected shape."""
        try:
            if arr.shape == expected_shape:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Expected shape {expected_shape}, got {arr.shape}")
        except AttributeError:
            self._result(False, problem, "Object should have a shape attribute")

    def has_ndim(self, arr: Any, expected_ndim: int, problem: str):
        """Check number of dimensions."""
        try:
            if arr.ndim == expected_ndim:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Expected {expected_ndim} dimensions, got {arr.ndim}")
        except AttributeError:
            self._result(False, problem, "Object should have ndim attribute")

    def has_dtype(self, arr: Any, expected_dtype, problem: str):
        """Check if array has expected dtype."""
        try:
            expected = np.dtype(expected_dtype)
            if arr.dtype == expected:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Expected dtype {expected}, got {arr.dtype}")
        except AttributeError:
            self._result(False, problem, "Object should have dtype attribute")

    # ==========================================
    # Value Range Checks (don't reveal exact answers)
    # ==========================================

    def value_in_range(self, value: Any, low: float, high: float, problem: str):
        """Check if value is within range."""
        try:
            if low <= value <= high:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Value should be between {low} and {high}")
        except TypeError:
            self._result(False, problem, "Value should be numeric")

    def all_values_in_range(self, arr: Any, low: float, high: float, problem: str):
        """Check if all values are within range."""
        try:
            arr = np.array(arr)
            if np.all((arr >= low) & (arr <= high)):
                self._result(True, problem)
            else:
                self._result(False, problem, f"All values should be between {low} and {high}")
        except Exception:
            self._result(False, problem, "Could not check value range")

    def min_value_is(self, arr: Any, expected_min: float, problem: str):
        """Check minimum value."""
        try:
            actual = np.min(arr)
            if np.isclose(actual, expected_min):
                self._result(True, problem)
            else:
                self._result(False, problem, f"Minimum should be {expected_min}")
        except Exception:
            self._result(False, problem, "Could not find minimum")

    def max_value_is(self, arr: Any, expected_max: float, problem: str):
        """Check maximum value."""
        try:
            actual = np.max(arr)
            if np.isclose(actual, expected_max):
                self._result(True, problem)
            else:
                self._result(False, problem, f"Maximum should be {expected_max}")
        except Exception:
            self._result(False, problem, "Could not find maximum")

    # ==========================================
    # Statistical Checks (reveal aggregate properties)
    # ==========================================

    def sum_is(self, arr: Any, expected_sum: float, problem: str, tolerance: float = 0.01):
        """Check if sum matches expected value."""
        try:
            actual = np.sum(arr)
            if np.isclose(actual, expected_sum, rtol=tolerance):
                self._result(True, problem)
            else:
                self._result(False, problem, f"Sum should be {expected_sum}")
        except Exception:
            self._result(False, problem, "Could not calculate sum")

    def mean_is_close(self, arr: Any, expected_mean: float, problem: str, tolerance: float = 0.1):
        """Check if mean is close to expected."""
        try:
            actual = np.mean(arr)
            if abs(actual - expected_mean) <= tolerance:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Mean should be close to {expected_mean}")
        except Exception:
            self._result(False, problem, "Could not calculate mean")

    def std_is_close(self, arr: Any, expected_std: float, problem: str, tolerance: float = 0.1):
        """Check if std is close to expected."""
        try:
            actual = np.std(arr)
            if abs(actual - expected_std) <= tolerance:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Std should be close to {expected_std}")
        except Exception:
            self._result(False, problem, "Could not calculate std")

    # ==========================================
    # Element Checks
    # ==========================================

    def first_element_is(self, arr: Any, expected: Any, problem: str):
        """Check first element value."""
        try:
            if hasattr(arr, 'iloc'):
                first = arr.iloc[0]
            else:
                first = arr[0]

            if isinstance(first, (float, np.floating)):
                passed = np.isclose(first, expected)
            else:
                passed = first == expected

            if passed:
                self._result(True, problem)
            else:
                self._result(False, problem, f"First element should be {expected}")
        except Exception:
            self._result(False, problem, "Could not access first element")

    def last_element_is(self, arr: Any, expected: Any, problem: str):
        """Check last element value."""
        try:
            if hasattr(arr, 'iloc'):
                last = arr.iloc[-1]
            else:
                last = arr[-1]

            if isinstance(last, (float, np.floating)):
                passed = np.isclose(last, expected)
            else:
                passed = last == expected

            if passed:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Last element should be {expected}")
        except Exception:
            self._result(False, problem, "Could not access last element")

    def element_at_is(self, arr: Any, index: Any, expected: Any, problem: str):
        """Check element at specific index."""
        try:
            if hasattr(arr, 'iloc'):
                actual = arr.iloc[index] if isinstance(index, int) else arr.loc[index]
            else:
                actual = arr[index]

            if isinstance(actual, (float, np.floating)):
                passed = np.isclose(actual, expected)
            else:
                passed = actual == expected

            if passed:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Element at index {index} should be {expected}")
        except Exception as e:
            self._result(False, problem, f"Could not access element at index {index}")

    # ==========================================
    # Collection Checks
    # ==========================================

    def contains(self, container: Any, item: Any, problem: str):
        """Check if container contains item."""
        try:
            if item in container:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Should contain: {item}")
        except TypeError:
            self._result(False, problem, "Object should be a container")

    def not_contains(self, container: Any, item: Any, problem: str):
        """Check if container does NOT contain item."""
        try:
            if item not in container:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Should NOT contain: {item}")
        except TypeError:
            self._result(False, problem, "Object should be a container")

    def is_sorted(self, arr: Any, problem: str, ascending: bool = True):
        """Check if array is sorted."""
        try:
            arr = np.array(arr)
            if ascending:
                passed = np.all(arr[:-1] <= arr[1:])
            else:
                passed = np.all(arr[:-1] >= arr[1:])

            if passed:
                self._result(True, problem)
            else:
                order = "ascending" if ascending else "descending"
                self._result(False, problem, f"Array should be sorted in {order} order")
        except Exception:
            self._result(False, problem, "Could not check if sorted")

    def all_unique(self, arr: Any, problem: str):
        """Check if all values are unique."""
        try:
            arr = np.array(arr).flatten()
            if len(arr) == len(np.unique(arr)):
                self._result(True, problem)
            else:
                self._result(False, problem, "All values should be unique")
        except Exception:
            self._result(False, problem, "Could not check uniqueness")

    # ==========================================
    # Pandas Specific Checks
    # ==========================================

    def has_columns(self, df: pd.DataFrame, expected_cols: list, problem: str):
        """Check if DataFrame has expected columns (exact match)."""
        try:
            if list(df.columns) == expected_cols:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Expected columns: {expected_cols}")
        except AttributeError:
            self._result(False, problem, "Object should be a DataFrame")

    def contains_column(self, df: pd.DataFrame, col: str, problem: str):
        """Check if DataFrame contains a specific column."""
        try:
            if col in df.columns:
                self._result(True, problem)
            else:
                self._result(False, problem, f"DataFrame should contain column: {col}")
        except AttributeError:
            self._result(False, problem, "Object should be a DataFrame")

    def has_index(self, df: pd.DataFrame, expected_index: list, problem: str):
        """Check if DataFrame/Series has expected index."""
        try:
            if list(df.index) == expected_index:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Expected index: {expected_index}")
        except Exception:
            self._result(False, problem, "Could not check index")

    def has_no_nulls(self, df: Any, problem: str):
        """Check that DataFrame/Series has no null values."""
        try:
            if isinstance(df, pd.DataFrame):
                null_count = df.isnull().sum().sum()
            else:
                null_count = df.isnull().sum()

            if null_count == 0:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Found {null_count} null values - should be 0")
        except Exception:
            self._result(False, problem, "Could not check for null values")

    def null_count_is(self, df: Any, expected_count: int, problem: str):
        """Check number of null values."""
        try:
            if isinstance(df, pd.DataFrame):
                null_count = df.isnull().sum().sum()
            else:
                null_count = df.isnull().sum()

            if null_count == expected_count:
                self._result(True, problem)
            else:
                self._result(False, problem, f"Expected {expected_count} nulls, found {null_count}")
        except Exception:
            self._result(False, problem, "Could not check null values")

    # ==========================================
    # Array Comparison (use sparingly)
    # ==========================================

    def arrays_match(self, actual: np.ndarray, expected: np.ndarray, problem: str):
        """Check if arrays are equal (when answer can't be hidden)."""
        try:
            if np.array_equal(actual, expected):
                self._result(True, problem)
            else:
                self._result(False, problem, "Array values don't match expected")
        except Exception:
            self._result(False, problem, "Could not compare arrays")

    def arrays_close(self, actual: np.ndarray, expected: np.ndarray, problem: str, rtol: float = 1e-5):
        """Check if arrays are approximately equal."""
        try:
            if np.allclose(actual, expected, rtol=rtol):
                self._result(True, problem)
            else:
                self._result(False, problem, "Array values not close enough to expected")
        except Exception:
            self._result(False, problem, "Could not compare arrays")

    # ==========================================
    # File System Checks
    # ==========================================

    def file_exists(self, path: str, problem: str):
        """Check if file exists."""
        import os
        if os.path.isfile(path):
            self._result(True, problem)
        else:
            self._result(False, problem, f"File not found: {path}")

    def dir_exists(self, path: str, problem: str):
        """Check if directory exists."""
        import os
        if os.path.isdir(path):
            self._result(True, problem)
        else:
            self._result(False, problem, f"Directory not found: {path}")

    # ==========================================
    # Hashed Answer Verification (for hidden answers)
    # ==========================================

    def verify(self, actual: Any, answer_hash: str, problem: str, hint: str = ""):
        """Verify against a hashed answer (answer not visible in code)."""
        actual_hash = hashlib.md5(str(actual).encode()).hexdigest()
        if actual_hash == answer_hash:
            self._result(True, problem)
        else:
            self._result(False, problem, hint or "Value doesn't match expected")

    # ==========================================
    # Summary
    # ==========================================

    def summary(self):
        """Print summary of all results."""
        total = self.passed + self.failed
        print(f"\n{'='*50}")
        if total > 0:
            pct = 100 * self.passed / total
            print(f"Results: {self.passed}/{total} passed ({pct:.0f}%)")
            if self.failed == 0:
                print("\033[92m🎉 Excellent! All problems solved correctly!\033[0m")
            elif pct >= 80:
                print("\033[93m👍 Good progress! A few more to go.\033[0m")
            else:
                print("\033[93m📚 Keep practicing! Review the hints above.\033[0m")
        else:
            print("No problems checked yet.")
        print(f"{'='*50}")


# Global checker instance
check = Checker()
