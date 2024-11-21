#!Python 3
"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

def main(fileName):
    file = open(fileName,'r')
    tripleSets = file.read().split('\n\n')
    pythagoreanTriples = []
    #print(tripleSets)
    for set in tripleSets:
        sides = set.split('\n')
        for i in range(3):
            sides[i] = int(sides[i])
        sides.sort()
        if ((sides[0]**2)+(sides[1]**2)) == (sides[2]**2):
            pythagoreanTriples.append(sides)
            #print(sides)
    print(len(pythagoreanTriples))
    return pythagoreanTriples


if __name__ == '__main__':
    assert len(main('task02a.txt')) == 6
    assert len(main('task02b.txt')) == 4
    assert len(main('task02c.txt')) == 11