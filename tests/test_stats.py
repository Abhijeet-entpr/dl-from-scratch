import pytest
import time
import math
from utils.stats import RunningStats, Timer, standardize

def test_running_stats_initial_state():
    stats = RunningStats()
    assert stats.count == 0
    assert stats.mean == 0.0
    assert stats.var == 0.0

def test_running_stats_mean():
    stats = RunningStats()
    stats.update(10.0)
    stats.update(20.0)
    assert stats.mean == 15.0

def test_running_stats_variance():
    stats = RunningStats()
    stats.update(10.0)
    stats.update(20.0)
    # Sample variance for [10, 20] is 50.0
    assert stats.var == 50.0

def test_timer_elapsed():
    with Timer() as t:
        time.sleep(0.01)
    assert t.elapsed_time >= 0.01

def test_running_stats_count():
    stats = RunningStats()
    stats.update(5.0)
    stats.update(15.0)
    assert stats.count == 2

def test_single_element_variance():
    stats = RunningStats()
    stats.update(42.0)
    # Variance should default to 0.0 when count <= 1
    assert stats.var == 0.0

def test_running_stats_invalid_type():
    stats = RunningStats()
    with pytest.raises(TypeError):
        # Passing a string instead of a number triggers a TypeError
        stats.update("not_a_number")

@pytest.fixture
def stats():
    """Fixture providing a fresh RunningStats instance."""
    return RunningStats()

# 6 Parametrized test cases for mean and variance validation
@pytest.mark.parametrize(
    "data, expected_count, expected_mean, expected_var",
    [
        # Case 1: Single element (variance should be 0.0)
        ([5.0], 1, 5.0, 0.0),
        # Case 2: Standard positive numbers
        ([10.0, 20.0, 30.0], 3, 20.0, 100.0),
        # Case 3: Symmetric negative and positive (mean = 0)
        ([-10.0, 10.0], 2, 0.0, 200.0),
        # Case 4: All identical values (variance = 0)
        ([7.0, 7.0, 7.0, 7.0], 4, 7.0, 0.0),
        # Case 5: Floating point values
        ([1.5, 2.5, 3.5, 4.5], 4, 3.0, 1.6666666666666667),
        # Case 6: Large values testing numerical stability
        ([1e6 + 1, 1e6 + 2, 1e6 + 3], 3, 1e6 + 2, 1.0),
    ],
)
def test_running_stats_updates(stats, data, expected_count, expected_mean, expected_var):
    """Tests count, mean, and sample variance across multiple input sequences."""
    for x in data:
        stats.update(x)

    assert stats.count == expected_count
    assert math.isclose(stats.mean, expected_mean, rel_tol=1e-7)
    assert math.isclose(stats.var, expected_var, rel_tol=1e-7)

@pytest.mark.parametrize(
    "inputs, expected_output",
   [
        # Case 1: Standard input - mean becomes 0, std dev becomes 1
        ([10.0, 20.0, 30.0], [-1.224744871391589, 0.0, 1.224744871391589]),
        # Case 2: Symmetric inputs
        ([-2.0, 0.0, 2.0], [-1.224744871391589, 0.0, 1.224744871391589]),
        # Case 3: Constant values (variance is 0) -> return zeros
        ([5.0, 5.0, 5.0], [0.0, 0.0, 0.0]),
    ],
)
def test_standardize(inputs, expected_output):
    result = standardize(inputs)
    
    # 1. Ensure the output list isn't empty!
    assert len(result) == len(expected_output), f"Expected {len(expected_output)} items, got {len(result)}"
    
    # 2. Compare elements
    for res, exp in zip(result, expected_output):
        assert math.isclose(res, exp, abs_tol=1e-5)
