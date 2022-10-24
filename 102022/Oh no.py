"""
Oh no!
Some really funny web dev gave you a sequence of numbers from his API response as an sequence of strings!

You need to cast the whole array to the correct type.

Create the function that takes as a parameter a sequence of numbers represented as strings and outputs a
 sequence of numbers.

ie:["1", "2", "3"] to [1, 2, 3]

Note that you can receive floats as well.
"""

def to_float_array(arr):
    result = []
    for i in arr:
        result.append(int(i))
    return result


print(to_float_array(["1", "2", "3"]))


# best practice from Codewars
def to_float_array(arr):
    return list(map(float, arr))

# map(function, iterables)
def add_strings(a, b):
    result = a+'-'+b
    return result


x = map(add_strings, ('Aaa', 'Bbb'), ('aaa', 'bbb'))
print(x)
# converting obcjet to list
print(list(x))
