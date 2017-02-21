# Define a Python function "descending(l)" that returns True if each element in
# its input list is at most as big as the one before it

def descending(l):
    for i in range(len(l)-1):
        if l[i] < l[i + 1]:
            return False

    return True

# Define a Python function "alternating(l)" that returns True if the values in
# the input list alternately go up and down (in a strict manner).

def alternating(l):
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return False

    for i in range(len(l)-2):
        if l[i] < l[i+1]:
            if l[i+1] < l[i+2]:
                return False

        if l[i] > l[i+1]:
            if  l[i+1] > l[i+2]:
                return False

    return True

# function "matmult(m1,m2)" that takes as input two matrices using this row-wise
# representation and returns the matrix product m1*m2 using the same
# representation (like matrix = [[1,2,3],[4,5,6]])

def matmult(m1, m2):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m2[0])):
            m3[i].append(0)
            for k in range(len(m2)):
                m3[i][j] += m1[i][k] * m2[k][j]

    return m3
