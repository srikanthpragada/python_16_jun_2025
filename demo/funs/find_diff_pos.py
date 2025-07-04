def diff_pos(s1, s2):
    if s1 == s2:
        return -1

    smallest = s1 if len(s1) < len(s2) else s2
    other = s2 if len(s1) < len(s2) else s1

    for idx, c in enumerate(smallest):
        if c != other[idx]:
            return idx

    if len(s1) != len(s2):
        return len(smallest)

    return -1


def diff_pos2(s1, s2):
    if s1 == s2:
        return -1

    min_len = min(len(s1), len(s2))

    for i in range(min_len):
        if s1[i] != s2[i]:
            return i

    return min_len if len(s1) != len(s2) else -1


print(diff_pos('abcd', 'abcd'))
