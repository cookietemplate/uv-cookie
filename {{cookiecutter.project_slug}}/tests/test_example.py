import pytest


@pytest.mark.parametrize("gt", ["hello world"])
def test_example(gt):
    assert "hello world" == gt
