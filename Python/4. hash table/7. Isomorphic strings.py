class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}   # rule: s character -> t character
        t_to_s = {}   # rule: t character -> s character

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            # if c1 already has a rule, it must match c2
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False

            # if c2 already has a rule, it must match c1
            if c2 in t_to_s:
                if t_to_s[c2] != c1:
                    return False

            # create the rules
            s_to_t[c1] = c2
            t_to_s[c2] = c1

        return True
