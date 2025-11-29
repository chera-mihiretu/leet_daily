class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0 for i in range(len(nums) + 1)]
        self.nums = nums

        self.build()
    def build(self):
        for i in range(len(self.nums)):
            temp = i + 1

            self.update_next(i)
    def update_next(self, index):
        temp = index + 1
        while temp < len(self.arr):
            self.arr[temp] += self.nums[index]
            temp = temp + (temp & -temp)
        

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        temp = index + 1
        while temp < len(self.arr):
            self.arr[temp] += delta
            temp = temp + (temp & -temp)


    def getMeSum(self, index) -> int:
        temp = index + 1
        result = 0
        while temp != 0:
            result += self.arr[temp]
            temp = temp - (temp & -temp)
        return result

    def sumRange(self, left: int, right: int) -> int:
        return self.getMeSum(right) - self.getMeSum(left - 1)
       

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)