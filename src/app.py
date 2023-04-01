first_bracket = (250000 - 145000)*0.02
second_bracket = first_bracket + (325000 - 250000)*0.05
third_bracket = second_bracket + (750000 - 325000)*0.1

def LBBT_calc(house_value):
    if (house_value < 145000): 
        return 0
    elif (house_value < 250000):
        return (house_value - 145000)*0.02
    elif (house_value < 325000):
        return first_bracket + (house_value - 250000)*0.05
    elif (house_value < 750000):
        return second_bracket + (house_value - 325000)*0.1
    else:
        return third_bracket + (house_value - 750000)*0.12