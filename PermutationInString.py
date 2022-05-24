class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

        In other words, return true if one of s1's permutations is the substring of s2.
        :param s1: first string
        :param s2: second string
        :return: boolean 
        """
        if len(s2) < len(s1):  # edge case
            return False

        freq_s1, freq_s2 = [0] * 26, [0] * 26

        # populate freq_s1 list
        for x in s1:
            freq_s1[ord(x) - ord('a')] += 1

        # populate freq_s2 list
        for x in range(0, len(s2) - len(s1) + 1):
            if x == 0:
                for y in range(x, x + len(s1)):
                    freq_s2[ord(s2[y]) - ord('a')] += 1
            else:  # increment the count for char in end of sliding window
                freq_s2[ord(s2[x + len(s1) - 1]) - ord('a')] += 1

            if freq_s2 == freq_s1:
                return True

            # decrement count for char in begining of sliding window, for next iteration
            freq_s2[ord(s2[x]) - ord('a')] -= 1

        return False