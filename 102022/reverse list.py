def reverse(lst):
    empty_list = list()            # use this!
    result = list()
    while lst:
        result.append(lst.pop())
    return result

print(reverse([1,None,14,"two"]))