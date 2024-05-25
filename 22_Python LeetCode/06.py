"""Reorder Data in Log Files leetcode 937"""

class solution:
    def recoderlogfile(self , logs):
        
        res1 , res2 = [] ,[]

        for log in logs:
            if (log.split()[1].isdigit()): #index of log 1 is digit

                res2.append(log)
            else:
                res1.append(log.split())

            res1.sort(key= lambda x : x[0])
            res1.sort(key= lambda x : x[1 :])

            for i in range(len(res1)):
                res1[i] = ( "" .join(res1[i])) 
            res1.extend(res2)
            return res1
            