#!python3

'''
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5
'''

'''
def find(needle):
    file = open('task01.txt','r')
    hay = file.read()
    haystack = hay.split('\n')
    for i in range(len(haystack)):
        if haystack[i] == needle:
            print(haystack[i],i)
            return i
'''

def find(needle):
    haystack = open('task01.txt','r').read().split('\n')
    if needle in haystack:
        print(haystack.index(needle))
        return haystack.index(needle)

if __name__ == "__main__":
    assert find('apple') == 0
    assert find('fish') == 5