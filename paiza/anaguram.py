# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

from re import template

words = []
for i in range(int(input())):
    words.append(input())

# 比較用の組み合わせを作る
# firstWordとsecondWordを取り出し、それ以外の要素をotherWordsとする
pareObjects = []
for firstWord in words:
    # firstWordの取得
    for secondWord in words:
        # secondWordの取得
        
        # 同一組み合わせ回避
        if firstWord == secondWord:
            break
        
        # firstWordとsecondWordが確定したらオブジェクトを定義
        obj = {
            'firstWord': firstWord,
            'secondWord': secondWord,
            'otherWords':[]
        }
        pareObjects.append(obj)
        
        # それ以外の要素をotherWordsとする
        for otherWord in words:
            if (otherWord != firstWord
            and otherWord != secondWord):
                obj['otherWords'].append(otherWord)

# アナグラム判定
result = 0
for obj in pareObjects:
    sortedPare = ''.join(sorted(list(obj['firstWord']) + list(obj['secondWord'])))
    for word in obj['otherWords']:
        sortedWord = ''.join(sorted(list(word)))
        if sortedPare == sortedWord:
            result += 1

            

# print(pareObjects)
print(result)