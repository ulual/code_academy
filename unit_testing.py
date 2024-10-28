def times_ten(number):
    return number * 10

# A unit test function with a single test case
def test_multiply_ten_by_zero():
    assert times_ten(0) == 0, 'Expected times_ten(0) to return 0'
    
def test_multiply_ten_by_one_million():
    assert times_ten(1000000) == 10000000, 'Expected times_ten(1000000) to return 10000000'

def test_multiply_ten_by_negative_number():
    assert times_ten(-10) == -100, 'Expected times_ten(-10) to return -100'


test_multiply_ten_by_zero()
test_multiply_ten_by_one_million()
test_multiply_ten_by_negative_number()
