class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hm = {}
        for v in secret:
            if v in hm:
                hm[v] +=1
            else:
                hm[v] = 1
        bull = 0
        cow = 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bull += 1
        for k in guess:        
            if k in hm and hm[k] != 0:
                cow += 1
                hm[k] -= 1
        return str(bull)+'A'+str(cow-bull)+'B'

            

        
        