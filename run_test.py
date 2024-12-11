# run_tests.py
import pytest

# Run pytest programmatically
def run_tests():
    # Run pytest on the current directory and capture the result
    #result = pytest.main()
    result = pytest.main(["-v"])  # Add '-v' for verbose output

    # Check if pytest run passed or failed
    if result == 0:
        print("All tests passed!")
    else:
        print(f"Some tests failed. Test result code: {result}")

if __name__ == "__main__":
    run_tests()
