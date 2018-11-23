"""狄克斯特拉算法的Python实现
这里用了换钢琴的例子
"""


# 首先构建这个图
def generate_graph():
    # 图
    graph = {}

    # 记录边的权重
    graph['score'] = {}
    graph['score']['poster'] = 0  # 乐谱换海报
    graph['score']['disc'] = 5  # 乐谱换唱片
    graph['disc'] = {}
    graph['disc']['guitar'] = 15  # 唱片换吉他
    graph['disc']['drum'] = 20  # 唱片换架子鼓
    graph['poster'] = {}
    graph['poster']['guitar'] = 30  # 海报换吉他
    graph['poster']['drum'] = 35  # 海报换架子鼓
    graph['guitar'] = {}
    graph['guitar']['piano'] = 20  # 吉他换钢琴
    graph['drum'] = {}
    graph['drum']['piano'] = 10  # 吉他换钢琴
    graph['piano'] = {}

    return graph


def dijkstars(node, costs, parents):
    """狄克斯特拉算法
    """
    for sub_node in graph[node]:
        cost = costs[node] + graph[node][sub_node]
        if sub_node not in costs or cost < costs[sub_node]:
            costs[sub_node] = cost
            parents[sub_node] = node
    for node in graph[node]:
        dijkstars(node, costs, parents)


def get_path(parents, end, path=''):
    if end in parents:
        if path == '':
            path = parents[end] + "-->" + end + path
        else:
            path = parents[end] + "-->" + path
        return get_path(parents, parents[end], path)
    else:
        return path


if __name__ == '__main__':
    infinity = float("inf")  # 无穷大

    graph = generate_graph()

    parents = {}  # 父节点

    # 初始化开销
    costs = {k: infinity if k != 'score' else 0 for k in graph.keys()}

    dijkstars('score', costs, parents)

    print(parents)
    path = get_path(parents, 'piano')
    print(path)
