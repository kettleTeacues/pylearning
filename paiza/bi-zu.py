# すべてのinputを取得
debug = False
nodeNum = int(input())

nodes = []
for i in range(nodeNum):
    node = input().split(' ')
    nodes.append({
        'key': node[0],
        'path': node[1]
    })

# ノードを連結
networks = []
for node in nodes:
    keyStr = 'n' + str(node['key'])

    # 既存のノードを検索
    nodeFind = list(filter(
        lambda item: item['key'] == keyStr,networks
    ))

    if nodeFind:
        # 既存のノードがあるときpathにこのノードを追加
        nodeFind[0]['path'].append('n' + str(node['path']))
    else:
        # 既存のノードがないときnetworksにこのノードを追加
        networks.append({
            'key': keyStr,
            'path': ['n' + str(node['path'])]
        })

# ネットワークをカウント
networkNum = 0
for node in networks:
    if len(node['path']) >= 2:
        for path in node['path']:
            loopPoint = list(filter(
                lambda item: path in item['path'], networks
            ))
            if len(loopPoint) >= 2:
                networkNum += 1
if debug:
    print(networkNum)

# 分岐ノードをカウント
connectNodeNum = 0
for node in networks:
    if len(node['path']) >= 2:
        connectNodeNum += 1
if debug:
    print(connectNodeNum)

# 終端ノードをカウント
edgeNodeNum = 0
for i in range(1, len(nodes)+1):
    cnt = 0
    keyList = list(filter(
        lambda item: item['key'] == str(i), nodes
    ))
    cnt = cnt + len(keyList)

    pathList = list(filter(
        lambda item: item['path'] == str(i), nodes
    ))
    cnt = cnt + len(pathList)

    if cnt == 1:
        edgeNodeNum += 1
if debug:
    print(edgeNodeNum)

# ネットワークの種類を判定
if (networkNum == 1
and connectNodeNum == 1):
    if edgeNodeNum == 0:
        print('O')
    elif edgeNodeNum == 1:
        print('P')
    elif edgeNodeNum == 2:
        print('Q')
    else:
        print('NON')
else:
    print('NON')

# すべてのinputを出力
# print(networks)