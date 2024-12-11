import pytest

@pytest.fixture
def sample_data():
    return {"name": "TestUser", "age": 30}

@pytest.fixture
def another_data():
    return {"name": "TestUser2", "age": 25}


# def test_add():
    
#     assert 3 == 3