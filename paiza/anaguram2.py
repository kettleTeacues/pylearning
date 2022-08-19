# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

from unittest import result


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
                
        # それ以外の要素をotherWordsとする
        for otherWord in words:
            if (otherWord != firstWord
            and otherWord != secondWord):
                # firstWordとsecondWordが確定したらオブジェクトを定義
                obj = {
                    'firstWord': firstWord,
                    'secondWord': secondWord,
                    'otherWord': otherWord
                }
                pareObjects.append(obj)

for firstWord in words:
    for otherWord in words:
        if firstWord != otherWord:
            # firstWordとsecondWordが確定したらオブジェクトを定義
            obj = {
                'firstWord': firstWord,
                'secondWord': firstWord,
                'otherWord': otherWord
            }
            pareObjects.append(obj)

result = 0
for obj in pareObjects:
    if ''.join(sorted(list(obj['firstWord']) + list(obj['secondWord']))) == ''.join(sorted(list(obj['otherWord']))):
        result += 1
print(result)