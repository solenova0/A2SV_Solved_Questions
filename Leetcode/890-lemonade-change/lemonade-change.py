# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         # a = 0
#         # b = 0
#         # if bills[0] != 5 or bills[1] == 20:
#         #     return False
#         # for v in bills:
#         #     if v == 5:
#         #         a += 1
#         #     elif v == 10 and a > 0:
#         #         a -= 1
#         #         b += 1
#         #     elif v == 20 and 15 <= a * 5 + 10 * b:
#         #         if b > 0 and a > 0:
#         #             b -= 1
#         #             a -= 1
#         #         elif a >= 3:
#         #             a -= 3
#         #         else:
#         #             return False
#         #     else:
#         #         return False
#         # return True
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = 0
        mymap = dict()
        for bill in bills:
            # if bill in mymap:
            #     mymap[bill] -= 1
            #     if mymap[bill] == 0:
            #         del mymap[bill]
            # else:
                if bill == 10:
                    if 5 in mymap:
                        mymap[5] -= 1
                        mymap[10] = mymap.get(10,0)+1
                        if mymap[5] == 0:
                            del mymap[5]
                    else:
                        return False
                elif bill == 20:
                    need = 15
                    if 10 in mymap:
                        mymap[10] -= 1
                        need -= 10
                        if mymap[10] == 0:
                            del mymap[10]
                    while need and 5 in mymap:
                        mymap[5] -= 1
                        need -= 5
                        if mymap[5] == 0:
                            del mymap[5]
                    if need:
                        return False
                        
                else:
                    mymap[5] = mymap.get(5,0) + 1
                    
        return True





        