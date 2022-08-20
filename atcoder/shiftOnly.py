arrLen = int(input())
arr = input().split()
divNum = 0

# すべての数字をintにする
for i, num in enumerate(arr):
    arr[i] = int(num)
# print(arr)

# すべて偶数のとき2で割る
isAllEven = True

while isAllEven:
    for num in arr:
        if num % 2 == 1:
            isAllEven = False

    if isAllEven:
        divNum += 1
        for i, num in enumerate(arr):
            arr[i] = num/2

print(divNum)