class Solution:
    def isSubset(self, a, b):
        # return set(b).issubset(set(a))

        a.sort()
        b.sort()

        i = 0
        j = 0

        if len(b) > len(a):
            return False

        while i < len(b) and j < len(a):
            if b[i] == a[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(b)


    # #Hashmap
    #     freq = {}
    #     for x in a:
    #         freq[x] = freq.get(x, 0) + 1

    #     for x in b:
    #         if x not in freq or freq[x] == 0:
    #             return False
    #         freq[x] -= 1

    #     return True
