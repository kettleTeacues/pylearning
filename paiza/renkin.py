# すべてのinputを取得・整形
taskNum = int(input())
taskPlans = []
for cnt in range(taskNum):
    task = input().split(' ')
    taskPlans.append({
        'key': 't' + str(cnt),
        'sta': int(task[0]),
        'end': int(task[1])
    })


# 連勤配列を生成
daysBool = []
for num in range(taskPlans[-1]['end']):
    daysBool.append(0)

for task in taskPlans:
    staDate = task['sta']
    endDate = task['end']

    for day in range(staDate-1, endDate):
        daysBool[day] = 1
# print(daysBool)
# 連勤をカウント
renkinList = [0]
renkinNum = 0
for day in daysBool:
    if day == 1:
        renkinNum += 1
    elif renkinNum > 0 and day == 0:
        renkinList.append(renkinNum)
        renkinNum = 0

# 配列最終日が出勤だったときリストにアペンド
if renkinNum > 0:
    renkinList.append(renkinNum)

renkinList.sort(reverse=True)
print(renkinList[0])