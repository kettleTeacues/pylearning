gohyaku = int(input())
hyaku = int(input())
goju = int(input())
total = int(input())

count = 0
for i in range(gohyaku + 1):
    for j in range(hyaku + 1):
        for k in range(goju + 1):
            if 500 * i + 100 * j + 50 * k == total:
                count += 1

print(count)