# Import the BMI module
from Lab_2 import BMI

# Test case for underweight BMI (< 18.5)
def test_bmi_under_weight():
    height = 1.75
    weight = 50
    result = BMI.calculate_bmi(height, weight)
    assert result == -1, "Expected underweight classification (-1) for BMI < 18.5"

# Test case for normal weight BMI (18.5 <= BMI < 25)
def test_bmi_normal_weight():
    height = 1.75
    weight = 68
    result = BMI.calculate_bmi(height, weight)
    assert result == 0, "Expected normal weight classification (0) for 18.5 <= BMI < 25"

# Test case for overweight BMI (> 25)
def test_bmi_over_weight():
    height = 1.75
    weight = 80
    result = BMI.calculate_bmi(height, weight)
    assert result == 1, "Expected overweight classification (1) for BMI > 25"
