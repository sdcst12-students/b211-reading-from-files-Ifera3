#!python
# Sum of Values

"""
The file task03.txt contains a lot of data. Each cluster of data is the number of points for that particular group. Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

def main():
    fileName = 'task03.txt'
    file = open(fileName,'r')
    clusters = file.read().split('\n\n')
    #print(clusters)
    #intClusters = []
    scores = []
    for set in clusters:
        group = set.split('\n')
        #print(group)
        for i in range(len(group)):
            #print(group[i])
            group[i] = int(group[i])
        scores.append(sum(group))
        #intClusters.append(group)
    #print(scores)
    highscore = max(scores)
    print(f'Cluster {scores.index(highscore)} won, with a score of {highscore}')



if __name__ == '__main__':
    main()