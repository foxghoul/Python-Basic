def fibo(N):
    if N <= 2:
        return 1
    else:
        return fibo(N - 1) + fibo(N - 2)

# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = 'color'
# ruleValue = 'blue'
# dic = {"type": 0, "color": 1, "name": 2}
# print(list(item[dic[ruleKey]] == ruleValue for item in items))
# print(sum([True, False, False]))
#
# for i in items:
#     continue
nums = [3,2,3]
target = 6
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
