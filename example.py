from KMP import KMP


s = "ababab"
pat1 = "bab"
pat2 = "abc"

kmp = KMP(s)

print(kmp.kmp_table())  # [0, 0, 1, 2, 3, 4]
print(kmp.kmp_search(pat1)) # 1
print(kmp.kmp_search(pat2)) # None
