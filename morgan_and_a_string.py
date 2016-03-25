test_cases = int(raw_input())
for i in range(test_cases):
    s1 = raw_input()
    s2 = raw_input()
    l1 = len(s1)
    l2 = len(s2)
    total_len = l1+l2
    k = 0
    i = 0
    j = 0
    res = ""
    while k < total_len:
        if i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                p = s1[i:]
                q = s2[j:]
                if len(p) < len(q):
                    p = p +'z'
                else:
                    q = q + 'z'
                if p < q:
                    res += s1[i]
                    i = i + 1
                else:
                    res += s2[j]
                    j = j + 1
            elif s1[i] < s2[j]:
                res += s1[i]
                i = i + 1
            else:
                res += s2[j]
                j = j + 1
        elif i < l1:
            res += s1[i]
            i = i + 1
        else:
            res = res + s2[j]
            j = j + 1
        k = k + 1
    print res
