import pytest

from app.module1 import function_to_test

@pytest.mark.parametrize("data, expected", [
    ({"name": "Alice", "age": 30}, {"name": "Alice", "age": 30}),
    ({"name": "Bob", "age": 25}, {"name": "Bob", "age": 25})
])
def test_function_to_test(data, expected):
    result = function_to_test(data)
    assert result == expected
