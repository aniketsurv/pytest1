from app.module2 import another_function

def test_another_function():
    data = {"name": "Charlie", "age": 40}
    result = another_function(data)
    assert result == {"age": 40, "full_name": "Charlie Doe"}
