import random

"""
Input: weighted adjacency list
"""
def longest_path_dag(adj, reverse_adj, start, end):
    order = topological_order(adj)
    order = order[order.index(start)+1:order.index(end)+1]
    score = {}
    previous_node = {}
    for n in order:
        score[n] = -100
        previous_node[n] = None
    score[start] = 0

    # follow topo ordering
    for i in range(len(order)):
        node = order[i]
        max_weight = -100
        max_node = None

        # skip 'source' nodes
        if node not in reverse_adj:
            previous_node[node] = node
            continue

        for previous in reverse_adj[node]:
            if previous[0] not in score: # skip nodes that are not in the desired path
                continue
            new_score = int(previous[1]) + score[previous[0]]
            if new_score > max_weight:
                max_weight = new_score
                max_node = previous[0]

        # record score and previous node
        score[node] = max_weight
        previous_node[node] = max_node
    return previous_node, score[end]

'''
construct path from source to sink
'''
def construct_path(previous_node, end, start):
    node = end
    path = []
    while node != start and node != previous_node[node]:
        path.insert(0, node)
        node = str(previous_node[node])
    path.insert(0, node)
    return path
        

def topological_order(adj):
    in_nodes, out_nodes, nodes = degrees(adj)
    order = []
    sources = [n for n in nodes if in_nodes[n] == 0]
    while len(sources) > 0:
        s = random.choice(sources)
        order.append(s)
        sources.remove(s)
        if s in adj:
            for n in adj[s]:
                if in_nodes[n[0]] != 0:
                    in_nodes[n[0]] -= 1
                    if in_nodes[n[0]] == 0:
                        sources.append(n[0])
    for i in in_nodes:
        if in_nodes[i] != 0:
            print "this is not a DAG"
    return order

"""
 get degrees of all nodes
"""
def degrees(adj_list):
    in_nodes = {}
    for i in adj_list:
        for j in adj_list[i]:
            in_nodes[i] = 0
            in_nodes[j[0]] = 0
    out_nodes = {}
    nodes = set()
    for i in adj_list:
        nodes.add(i)
        for j in adj_list[i]:
            nodes.add(j[0])
            if j[0] not in in_nodes:
                in_nodes[j[0]] = 1
            else:
                in_nodes[j[0]] += 1
            if i not in out_nodes:
                out_nodes[i] = 1
            else:
                out_nodes[i] += 1
    return in_nodes,out_nodes, nodes

"""
Construct reverse and forward adjacency list
"""
def arrow_to_adj(arrows):
    adj_list = {}
    reverse_adj = {} 
    for l in arrows:
        p = l.split('->')[0]
        s = tuple(l.split('->')[1].split(':'))
        # forward adj_list
        if p in adj_list:
            adj_list[p].append(s)
        else:        
            adj_list[p] = [s]
        # backward adj_list
        if s[0] in reverse_adj:
            reverse_adj[s[0]].append((p,s[1]))
        else:
            reverse_adj[s[0]] = [(p,s[1])]
    return adj_list, reverse_adj

if __name__ == '__main__':
    f = open('test')
    start = f.readline().rstrip('\n')
    end = f.readline().rstrip('\n')   
    adj, reverse_adj = arrow_to_adj([l.rstrip('\n') for l in f])
    track, score = longest_path_dag(adj, reverse_adj, start, end)
    path = construct_path(track, end, start)
    print score
    print '->'.join(path)


    

