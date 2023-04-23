n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

p, q = -1, -1
while p != 0 or q != 0:
    p, q = map(int, input().split())
    if p > q:
        valueAtQ = nums[q]
        for i in range(q, p):
            nums[i] = nums[i + 1]
        nums[p] = valueAtQ
    elif p < q:
        valueAtP = nums[p]
        for i in range(p, q):
            nums[i] = nums[i + 1]
        nums[q] = valueAtP

for num in nums:
    print(num, end=' ')
