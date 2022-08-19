# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
params = input().split(' ')

peopleNum = int(params[0])
playNum = int(params[1])
#インプットデータ整形
records = []
for i in range(1, peopleNum+1):
    intDatas = []
    
    #1人ずつの結果オブジェクトを定義
    records.append({
        'key': 'person-' + str(i),
        'values': intDatas
    })
    
    #1人ずつの各結果を取得
    strDatas = input().split(' ')
    for strData in strDatas:
        intDatas.append(int(strData))
    
    #1人ずつの結果をソート
    intDatas.sort(reverse=True)
# print(records)

#順位を比較
tops = []
bool = True
i = 0
while bool:
    tops = []
    sortList = [] 
    
    #i回目のトップスコアを取得
    for record in records:
        sortList.append(record['values'][i])
    sortList.sort(reverse=True)
    topScore = sortList[0]
    
    #i回目のトップパーソンを取得
    for record in records:
        if record['values'][i] == topScore:
            tops.append(record)
    #i回目のトップパーソンをrecordsに戻す
    records = tops
    
    #すべての試行回数を超えたとき処理を抜ける
    i += 1
    if i > playNum-1:
        bool = False
    
    #トップが1人のとき処理を抜ける
    if len(tops) == 1:
        bool = False

for top in tops:
    print(top['key'].replace('person-', ''))
# print(top)
# for rec in records:
#     print(rec)