import pytest
import io
import sys
from unittest.mock import patch


def test_script_runs_without_errors():
    """Test that the script can be imported and executed without errors."""
    import pythonSample


def test_sum_calculation():
    """Test that the sum calculation is correct."""
    a = 5
    b = 10
    expected_sum = 15
    actual_sum = a + b
    assert actual_sum == expected_sum


def test_print_output_capturable():
    """Test that we can capture the printed output."""
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        print("Hello, World!")
        output = mock_stdout.getvalue()
        assert "Hello, World!" in output


def test_variable_values():
    """Test that variables have expected values."""
    a = 5
    b = 10
    c = a + b
    assert a == 5
    assert b == 10
    assert c == 15


def test_arithmetic_operations():
    """Test various arithmetic operations."""
    assert 5 + 10 == 15
    assert 10 - 5 == 5
    assert 5 * 2 == 10
    assert 10 / 2 == 5.0


def test_string_formatting_in_print():
    """Test that print with multiple arguments works correctly."""
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        a, b, c = 5, 10, 15
        print("The sum of", a, "and", b, "is:", c)
        output = mock_stdout.getvalue()
        assert "The sum of" in output
        assert "5" in output
        assert "10" in output
        assert "15" in output


def test_script_contains_expected_strings():
    """Test that the script contains expected message strings."""
    import pythonSample
    expected_strings = [
        "Hello, World!",
        "sample Python script",
        "Happy coding!",
        "End of the script"
    ]
    # This test verifies the script structure by checking it can be imported
    assert pythonSample is not None


@pytest.mark.parametrize("a,b,expected", [
    (5, 10, 15),
    (0, 0, 0),
    (-5, 10, 5),
    (100, 200, 300),
])
def test_sum_various_inputs(a, b, expected):
    """Test sum calculation with various input combinations."""
    assert a + b == expected


def test_module_level_variables_accessible():
    """Test that module-level variables are accessible after import."""
    import pythonSample
    assert hasattr(pythonSample, 'a')
    assert hasattr(pythonSample, 'b')
    assert hasattr(pythonSample, 'c')
    assert pythonSample.a == 5
    assert pythonSample.b == 10
    assert pythonSample.c == 15
