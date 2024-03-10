"""Triplet
[1 , 0 , 1 , 2 , -1 , -1]

#First Step Sort the Array
[-4 , -1 , -1 , 0 , 1 , 2] #asending order

#2nd step left and right l = i+1 and r is last num

#sum total = i + (i+1) +R 

sum total  = 0  L = L+1 , R = R-1

sum total < 0 
L=L+1

sum total > 0
R = R-1

sum total == 0
result.append (num[i] , num[l] , num[r])
"""

class Solution:
    def threesum(self , number):
        result = []
        number.sort()

        length = len(number)

        for i in range(length-2):
            
            if i>0 and  number[i]== number[i-1]:
                continue
            Left = i+1
            Right = length-1


            while Left<Right:
                total = number[i] + number[Left] + number[Right]
                if total <0:
                    Left = Left+1
                elif total >0:
                    Right = Right -1
                else:
                    result.append([number[i] , number[Left] , number[Right]])

                    while Left<Right and number[Left]==number[Left+1]:
                        Left = Left+1
                    while Left<Right and number[Left]==number[Left-1]:
                        Left = Left-1
            
                    Left = Left+1 
                    Right = Right-1
        return result       