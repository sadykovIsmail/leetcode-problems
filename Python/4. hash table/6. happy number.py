class Solution:
    def isHappy(self, n: int) -> bool:
        
        results = set()
        repeatance = False
        summ = n
        
        while repeatance == False:
            
            sum = list(str(summ))
            list_sum = [int(d) for d in sum]
            sum8 = 0

            for num in list_sum:
                
                sum8 += num * num
                summ = sum8


            if summ in results:
                return False

            elif summ == 1:
                return True
            
            results.add(summ)
            
        

            
example = Solution()
print(example.isHappy(19))

        

#clearer
class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        summ = n

        while True:
            digits = list(str(summ))
            sum8 = 0

            for num in digits:
                sum8 += int(num) * int(num)

            summ = sum8

            if summ == 1:
                return True

            if summ in results:
                return False

            results.add(summ)


example = Solution()
print(example.isHappy(19))  # True
print(example.isHappy(3))   # False


