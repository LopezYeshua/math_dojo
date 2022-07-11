class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self

# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,3).add(2,5,1,5).subtract(6,2,3).result
print(x)

