from price_info import total_cost_shopping, cost_of_fruits

def test_total_cost_shopping():
    expected_total_cost = 46.75  # Expected result based on price and quantity lists
    assert total_cost_shopping() == expected_total_cost, f"total_cost_shopping() failed! Expected {expected_total_cost}, got {total_cost_shopping()}"
    print("total_cost_shopping() test passed!")

def test_cost_of_fruits():
    assert cost_of_fruits('apple', 10) == 12.0, "cost_of_fruits('apple', 10) failed!"
    print("cost_of_fruits('apple', 10) test passed!")
