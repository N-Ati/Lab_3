from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept

def test_get_employees_by_age_range():
    # Test for a valid age range
    result = get_employees_by_age_range(20, 30)
    expected = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    assert result == expected

    # Test for an empty result
    result = get_employees_by_age_range(50, 60)
    expected = []
    assert result == expected

def test_calculate_average_salary():
    # Test the average salary calculation
    result = calculate_average_salary()
    expected = round((50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6)  # 5,0000
    assert result == expected

def test_get_employees_by_dept():
    # Test for a valid department
    result = get_employees_by_dept("Engineering")
    expected = [
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    assert result == expected

    # Test for a department with no employees
    result = get_employees_by_dept("HR")
    expected = []
    assert result == expected

# Run the tests
if __name__ == "__main__":
    try:
        test_get_employees_by_age_range()
        test_calculate_average_salary()
        test_get_employees_by_dept()
        print("All tests passed!")
    except AssertionError as e:
        print("A test failed:", e)
