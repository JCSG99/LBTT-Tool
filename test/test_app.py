from src.app import LBBT_calc

first_bracket = (250000 - 145000)*0.02
second_bracket = first_bracket + (325000 - 250000)*0.05
third_bracket = second_bracket + (750000 - 325000)*0.1

def test_returns_0_when_passed_0():
    assert LBBT_calc(0) == 0

def test_returns_0_when_passed_144000():
    assert LBBT_calc(144000) == 0

def test_returns_0_when_passed_145000():
    assert LBBT_calc(145000) == 0
    
def test_house_value_in_first_bracket():
    assert LBBT_calc(200000) == (200000 - 145000)*0.02

def test_returns_expected_at_250000():
    assert LBBT_calc(250000) == (250000 - 145000)*0.02
    
def test_house_value_in_second_bracket():
    expected_value = first_bracket + (300000 - 250000)*0.05
    assert LBBT_calc(300000) == expected_value

def test_returns_expected_at_325000():
    assert LBBT_calc(325000) == first_bracket + (325000-250000)*0.05
    
def test_house_value_in_third_bracket():
    expected_value = second_bracket + (600000-325000)*0.1
    assert LBBT_calc(600000) == expected_value

def test_returns_expected_at_750000():
    assert LBBT_calc(750000) == third_bracket

def test_house_value_above_third_bracket():
    expected_value = third_bracket + (1250000-750000)*0.12
    assert LBBT_calc(1250000) == expected_value