def expect_to_actual(expect, actual):
    if expect == actual:
        result = 'pass'
    else:
        result = 'fail'
    return result
