def check_types(number, string):
    if type(number) != int: raise Exception("Parameter 'number' must be an Integer")
    if type(string) != str: raise Exception("Parameter 'string' must be a String")

    print "parameters are ok: {} {}".format(number, string)

check_types(3, 'fdfgdf')
#check_types('dd', 'gjjf')
check_types(3, 67)
