"""
Knuth–Morris–Pratt algorithm

searches for occurrences of a "pattern" P within a main "text string" S by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters.  
"""

class KMP:
    """
    kmp algorithm
    """
    
    def __init__(self, s):
        self.S = s
        self.length = len(s)
        
    def kmp_table(self):
        """
        return the partial match table of S.
        O(len(S))
        return: list of integers
        """
        partial_match_table = [0]*self.length
        s = list(self.S)
        i,j=0,1
        while i<self.length and j<self.length:
            if s[i]==s[j]:  # case 1: the substring continues  
                partial_match_table[j]=i+1
                i+=1
                j+=1
            else:  # case 2: the substring doesn't continues, but can fall back
                if i==0:
                    partial_match_table[j]=0
                    j+=1
                else:  # case 3: run out of candates
                    i = partial_match_table[i-1]
        return partial_match_table
    
    def kmp_search(self, P):
        """
        O(len(S))
        P: the pattern(word) sought
        return: an integer (the zero-based position in S at which P is found)
        """
        m = 0  # the beginning of the current match in S
        i = 0  # the position of the current character in P
        kmp_table=self.kmp_table()


        while m + i < self.length:
            if P[i] == self.S[m+i]:
                if i == len(P) - 1:
                    return m
                i += 1
            else:
                if kmp_table[i] > 0:
                    m = m + i - kmp_table[i]
                    i = kmp_table[i]
                else:
                    m += 1
                    i = 0
        return None  # have searched all of S unsuccessfully