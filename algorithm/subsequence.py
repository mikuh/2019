"""最长公共子序列
动态规划实现
"""


def max_subsequence(s1, s2):
    """最长公共子序列"""

    def equal(table, i, j):
        return table[i - 1][j - 1] + 1

    def not_equal(table, i, j):
        return max(table[i][j - 1], table[i - 1][j])

    table = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
    for i, row in enumerate(table[:-1]):
        for j, c in enumerate(row[:-1]):
            if s2[i] == s1[j]:
                table[i][j] = equal(table, i, j)
            else:
                table[i][j] = not_equal(table, i, j)
    return max([x for l in table for x in l])


if __name__ == '__main__':
    s1 = 'fosh'
    s2 = 'fish'
    print(max_subsequence(s1, s2))
