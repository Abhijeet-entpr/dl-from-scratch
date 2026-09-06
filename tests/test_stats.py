import pytest
import time
from utils.stats import RunningStats, Timer

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