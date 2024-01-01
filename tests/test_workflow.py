import pytest
from temporal_workflows.workflow import activity1, activity2


def test_activity1():
    assert activity1("test") == "test_processed_by_activity1"


def test_activity2():
    assert activity2("test") == "test_and_activity2"
