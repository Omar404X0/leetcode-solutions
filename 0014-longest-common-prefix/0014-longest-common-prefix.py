from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        i = 0
        keep_going = True

        while keep_going:
            if i >= len(strs[0]):
                break

            first = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != first:
                    keep_going = False
                    break

            if keep_going:
                prefix += first

            i += 1

        return prefix