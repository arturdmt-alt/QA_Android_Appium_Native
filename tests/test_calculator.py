import pytest
from pages.calculator_page import CalculatorPage

class TestCalculator:
    """Tests for Android Calculator app"""
    
    def test_addition(self, driver):
        """Test: 1 + 5 = 6"""
        calc = CalculatorPage(driver)
        
        calc.click_digit(calc.DIGIT_1)
        calc.click_operation(calc.PLUS)
        calc.click_digit(calc.DIGIT_5)
        calc.click_operation(calc.EQUALS)
        
        result = calc.get_result()
        assert result == "6"
        print(f"Addition test passed: 1 + 5 = {result}")
    
    def test_multiple_operations(self, driver):
        """Test: 2 + 2 = 4"""
        calc = CalculatorPage(driver)
        
        calc.click_digit(calc.DIGIT_2)
        calc.click_operation(calc.PLUS)
        calc.click_digit(calc.DIGIT_2)
        calc.click_operation(calc.EQUALS)
        
        result = calc.get_result()
        assert result == "4"
        print(f"Multiple operations test passed: 2 + 2 = {result}")
        