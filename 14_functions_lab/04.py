'''
functions no4
'''
def longer_than(long, *words):
    array = []
    for word in words:
        if len(word) > long:
            array.append(word)

    return array

print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')   


