'''
functios no3
'''
def sum_deca_digits(*nums):
    sum = 0
    for num in nums:
        if type(num) != int: raise Exception("All Parameters must be Integers")    
        div = num/10
        mod = div % 10
        sum += mod

    return sum

print sum_deca_digits(140,220,1120)        


