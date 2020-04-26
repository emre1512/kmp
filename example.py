from KMP import KMP


s = "Hayalperestsin güzel hayaller peşinde, çok gençsin yanlış insanlar kalbinde"
pat = "hayaller"

kmp = KMP(s)

""" print(kmp.kmp_table()) """  # print kmp table
print(kmp.kmp_search(pat)) # print index
