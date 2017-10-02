seqeuence1 = ['a', 'c', 'b', 'c', 'f']
seqeuence2 = ['a', 'b', 'c', 'd', 'e', 'f'] # a b c f
import numpy

def longest_common_sequence(seq1, seq2, m, n):
    if m == len(seq1) or n == len(seq2):
        return 0
    m_compare = seq1[m]
    n_compare = seq2[n]
    if m_compare == n_compare:
        return 1 + longest_common_sequence(seq1, seq2, m + 1, n + 1)
    else:
        tmp1 = longest_common_sequence(seq1, seq2, m + 1, n)
        tmp2 = longest_common_sequence(seq1, seq2, m, n + 1)
        return max(tmp1, tmp2)


print "---recursive approach---"
result = longest_common_sequence(seqeuence1, seqeuence2, 0, 0)
print "recursive approach result is ", result

def longest_common_sequence_iterate(seq1, seq2):
    temp = numpy.zeros((len(seq1)+1, len(seq2)+1))
    max_matches = 0
    for m in range(1, len(seq1)+1):

        for n in range(1, len(seq2)+1):
            if seq1[m-1] == seq2[n-1]:
                temp[m][n] = temp[m-1][n-1] + 1
            else:
                temp[m][n] = max(temp[m-1][n], temp[m][n-1])
            if temp[m][n] > max_matches:
                max_matches = temp[m][n]
    print numpy.matrix(temp)
    return max_matches


result = longest_common_sequence_iterate(seqeuence1, seqeuence2)
print "---iterative approach---"
print "iterative approach result is ", result
