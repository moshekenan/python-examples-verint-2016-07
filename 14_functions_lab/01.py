'''
functions no.1
'''
def func_sum(*params):
    res = 0
    for param in params:
        if type(param) == int:
            res += param

    return res

print func_sum(10,20,30)
print func_sum(10, 'foo', 'bar', 20)


def func_mul(*params):
    res = 1
    for param in params:
        if type(param) == int:
            res *= param

    return res

print func_mul()
print func_mul('foo', 'bar', 10, 20)

