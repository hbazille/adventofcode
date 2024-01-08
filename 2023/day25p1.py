
from utils import graph
import networkx as nx

def buildgraph(l):
    G = nx.Graph()
    for (name, dest) in l:
        for dst in dest:
            G.add_edge(name, dst, weight = 1)
    cut_value, partition = nx.stoer_wagner(G)
    return cut_value, partition


def parseline(l):
    idx = l.index(":")
    name = l[:idx]
    dest = list(map(lambda x : x.strip(), l[idx+1:].split()))
    return name, dest
           
                 
if __name__ == "__main__":
    """
    25th of december, 8am, no I won't recode stoer wagner
    thx mr networkx
    """
    l = [parseline(s) for s in open('data/day25', 'r').readlines()]
    _, p = buildgraph(l)
    print(len(p[0]) * len(p[1]))
