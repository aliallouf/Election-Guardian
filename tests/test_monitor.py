import pytest
import sys
import os

# Add src to path for testing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.monitor import StreamMonitor

def test_strict_majority():
    monitor = StreamMonitor(strict=True)
    data = [1, 2, 1, 3, 1] # 1 appears 3/5 times (Strict Majority)
    for x in data: monitor.process_element(x)
    assert monitor.verify_majority(data) == 1

def test_no_majority():
    monitor = StreamMonitor(strict=True)
    data = [1, 2, 3] # No majority
    for x in data: monitor.process_element(x)
    assert monitor.verify_majority(data) == -1

def test_weak_majority():
    # In a list of 4, two 1s is 50% (Weak, not Strict)
    data = [1, 1, 2, 3]
    monitor = StreamMonitor(strict=False)
    for x in data: monitor.process_element(x)
    assert monitor.verify_majority(data) == 1

def test_empty_input():
    monitor = StreamMonitor()
    assert monitor.verify_majority([]) == -1