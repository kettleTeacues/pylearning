max, under, top = map(int, list(input().split()))

total = 0
for num in range(1, max+1):
    numDigit = list(map(int, list(str(num))))
    digitSum = 0
    for digit in numDigit:
        digitSum += digit
    if (digitSum >= under
    and digitSum <= top):
        total += num

print(total)