class Solution(object):
    def RemoveElement(self,nums,value):
        k=0
        for i in range(len(nums)):
            if nums[i] != value:
                nums[k]=nums[i]
                k+=1
        return k
        # Функция удаляет указанное число,сдвигает остальные на лево и return количество остальных элементов
a=[0,1,2,2,3,0,4,2]
val =2
solution =Solution()
k = solution.RemoveElement(a,val)
print(k)