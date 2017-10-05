import numpy
from . import SetupDemo, print_description


class LongestCommonSubsequence(object):
    def longest_common_sequence_recursion(self, seq1, seq2, m=-0, n=0):
        if m == len(seq1) or n == len(seq2):
            return 0
        m_compare = seq1[m]
        n_compare = seq2[n]
        if m_compare == n_compare:
            return 1 + self.longest_common_sequence_recursion(seq1, seq2, m + 1, n + 1)
        else:
            tmp1 = self.longest_common_sequence_recursion(seq1, seq2, m + 1, n)
            tmp2 = self.longest_common_sequence_recursion(seq1, seq2, m, n + 1)
            return max(tmp1, tmp2)

    def longest_common_sequence_iterate(self, seq1, seq2):
        temp = numpy.zeros((len(seq1) + 1, len(seq2) + 1))
        max_matches = 0
        for m in range(1, len(seq1) + 1):

            for n in range(1, len(seq2) + 1):
                if seq1[m - 1] == seq2[n - 1]:
                    temp[m][n] = temp[m - 1][n - 1] + 1
                else:
                    temp[m][n] = max(temp[m - 1][n], temp[m][n - 1])
                if temp[m][n] > max_matches:
                    max_matches = temp[m][n]
        print numpy.matrix(temp)
        return max_matches


class LongestCommonSubsequenceDemo(SetupDemo):
    def __init__(self):
        super(LongestCommonSubsequenceDemo, self).setup_demo(__file__)
        self.sequence1 = ['a', 'c', 'b', 'c', 'f']
        self.sequence2 = ['a', 'b', 'c', 'd', 'e', 'f']  # a b c f

    @print_description
    def longest_common_sequence_iterate(self):
        lc_subsequence = LongestCommonSubsequence()
        result = lc_subsequence.longest_common_sequence_iterate(self.sequence1, self.sequence2)
        print "Result of itertative appraoch is -->", result

    @print_description
    def longest_common_sequence_recursion(self):
        lc_subsequence = LongestCommonSubsequence()
        result = lc_subsequence.longest_common_sequence_recursion(self.sequence1, self.sequence2)
        print "Result of recursive approach is ", result

if __name__ == "__main__":
    lc_subsequence_demo = LongestCommonSubsequenceDemo()
    demos_to_run = [lc_subsequence_demo.longest_common_sequence_iterate,
                    lc_subsequence_demo.longest_common_sequence_recursion]

    [func() for func in demos_to_run]
