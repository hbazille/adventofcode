# -*- coding: utf-8 -*-
"""Graph module.

Provide an implementation of graphs with adjacency lists.

In a graph, vertices are considered numbered from 0 to the order of the graph
minus one. The vertex key, or number, can then be used to access its
adjacency list.

"""

#from .exception import NoneException   # fait planter mon Python !!!!


class Graph:
    """ Simple class for graph: adjacency lists

    Attributes:
        order (int): Number of nodes.
        directed (bool): True if the graph is directed. False otherwise.
        adjlists (List[List[int]]): Lists of connected vertices for each vertex.
        labels (list[str]): optionnal vector of vertex labels
        costs (dict): [optionnal] edge (src, dst) -> cost (float)
        infos (dict)! optionnal dictionary for informations (purpose, dimensions, ...)
    """

    def __init__(self, order, directed=False, costs=False, labels=None):
        """Init graph, allocate adjacency lists

        Args:
            order (int): Number of nodes.
            directed (bool): True if the graph is directed. False otherwise.
            labels (list[str]): optionnal vector of vertex labels
            costs (bool): True if the graph is weighted. False otherwise. 

        """

        self.order = order
        self.directed = directed
        if costs:
            self.costs = {}
        else:
            self.costs = None
        self.adjlists = []
        for _ in range(order):
            self.adjlists.append([])
        self.labels = labels


    def addedge(self, src, dst, cost=None):
        """Add egde to graph.
    
        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.
            cost: if not None, the cost of edge (src, dst)
    
        Raises:
            IndexError: If any vertex index is invalid.
            Exception: If graph is None.
    
        """
    
        # Check graph and vertex indices.
        if self is None:
            raise Exception('Empty graph')
        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")
        # Add edge if multi or not already existing, and reverse-edge if undirected.
        #if src != dst and dst not in self.adjlists[src]:
        self.adjlists[src].append(dst)
        if not self.directed and dst != src:
            self.adjlists[dst].append(src)
        if self.costs != None:
            self.costs[(src, dst)] = cost
            if not self.directed:
                self.costs[(dst, src)] = cost


    def addvertex(self, number=1, labels=None):
        """Add number vertices to graph.
    
        Args:
            number (int): Number of vertices to add.
            labels (str list) optionnal list of new vertex labels
        Raises:
            Exception: If graph is None.
                
        """
        # Check graph
        if self is None:
            raise Exception('Empty graph')    
        # Increment order and extend adjacency list
        self.order += number
        for _ in range(number):
            self.adjlists.append([])
        if labels:
            self.labels += labels

    def removeedge(self, src, dst):
        """Remove egde from the graph.
    
        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.
    
        Raises:
            IndexError: If any vertex index is invalid.
            Exception: If graph is None.
    
        """
    
        # Check graph and vertex indices.
        if self is None:
            raise Exception('Empty graph')
        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")
        # Add edge if multi or not already existing, and reverse-edge if undirected.
        if dst in self.adjlists[src]:
            self.adjlists[src].remove(dst)
            if self.costs:
                self.costs.pop((src, dst))
            if not self.directed and dst != src:
                self.adjlists[dst].remove(src)
                if self.costs:
                    self.costs.pop((dst, src))
                
        
def dot(ref):
    """Write down dot format of graph.

    Args:
        ref (Graph).

    Returns:
        str: String storing dot format of graph.

    """

    # Check if empty graph.
    if ref is None:
        return "graph G { }"
    # Build dot for non-empty graph.
    (s, link) = ("digraph ", " -> ") if ref.directed else ("graph ", " -- ")
    s += " G {\n"
    if not ref.labels:   
        s += "node [shape = circle]\n"
    for src in range(ref.order):
        if ref.labels:
            s += "  " + str(src) + '[label = "' + ref.labels[src] + '", xlabel = "' + str(src) + '"]\n'
        else:
            s += "  " + str(src) + '\n'        
        for dst in ref.adjlists[src]:
            cost = ' [label=' + str(ref.costs[(src, dst)]) + '] ' if ref.costs else ""
            if ref.directed or src >= dst:
                s += "  " + str(src) + link + str(dst) + cost + '\n'
    s += '}'
    return s

def toDotHighlightEdges(G, edges):
    (dot, link) = ("digraph ", " -> ") if G.directed else ("graph ", " -- ")
    dot += "G {\n"
    if not G.labels:
        dot += "node [shape = circle]\n"
        
    #vertex traversal
    for s in range(G.order):
        if G.labels:
            dot += "  " + str(s) + '[caption = "' + G.labels[s] + '"]\n'
        else:
            dot += "  " + str(s) + '\n'        
        # adjacent list traversal
        for adj in G.adjlists[s]:   
            if G.directed or s >= adj:
                if (s, adj) in edges or (adj, s) in edges:
                    highLight = ', color="red", style="bold"'
                else:
                    highLight = ''
                cost = 'label=' + str(G.costs[(s, adj)]) if G.costs else ''
                if highLight or cost:
                    cost = ' [' + cost + highLight + ']'
                dot += "  " + str(s) + link + str(adj) + cost + '\n'
    dot += '}'
    return dot
    



def display(ref, eng=None, highlightedges=None):
    """
    *Warning:* Made for use within IPython/Jupyter only.
    eng: graphivz.Source "engine" optional argument (try "neato", "fdp", "sfdp", "circo")
    """
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    if highlightedges:
        dotstr = toDotHighlightEdges(ref, highlightedges)
    else:
        dotstr = dot(ref)
    display(Source(dotstr, engine = eng))

    
# load / save gra(wgra) format    

def load(filename):
    """Build a new graph from a GRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.

    Raises:
        FileNotFoundError: If file does not exist. ????

    """

    f = open(filename)
    lines = f.readlines()
    infos = {}
    i = 0
    while '#' in lines[i]: # lines[i][0] == '#'
        (key, val) = lines[i][1:].strip().split(": ")
        infos[key] = val
        i += 1
    
    directed = bool(int(lines[i]))
    order = int(lines[i+1])
    g = Graph(order, directed)
    g.infos = infos
    if g.infos and "labels" in g.infos:
        g.labels = g.infos["labels"].split(',')
    for line in lines[i+2:]:
        edge = line.strip().split(' ')
        (src, dst) = (int(edge[0]), int(edge[1]))
        g.addedge(src, dst)
    f.close()
    return g



def load_weightedgraph(filename, costType=float):
    """Build a new weighted graph from a WGRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.
    """
    f = open(filename)
    lines = f.readlines()
    infos = {}
    i = 0
    while '#' in lines[i]:
        (key, val) = lines[i][1:].strip().split(": ")
        infos[key] = val
        i += 1
    directed = bool(int(lines[i]))
    order = int(lines[i+1])
    G = Graph(order, directed, costs=True)
    G.infos = infos
    if G.infos and "labels" in G.infos:
        G.labels = G.infos["labels"].split(',')    
    for line in lines[i+2:]:
        edge = line.strip().split(' ')
        (x, y, cost) = (int(edge[0]), int(edge[1]), costType(edge[2]))
        G.addedge(x, y, cost)
    f.close()

    return G
    
def save(G, fileOut):
    gra = ""
    if G.labels:
        lab = "#labels: "
        for i in range(G.order - 1):
            lab += G.labels[i] + ','
        lab += G.labels[-1]
        gra += lab + '\n'
    gra += str(int(G.directed)) + '\n'
    gra += str(G.order) + '\n'
    for s in range(G.order):
        for adj in G.adjlists[s]:
            if G.directed or s >= adj:
                cost = ' ' + str(G.costs[(s, adj)]) if G.costs else ""
                gra += str(s) + " " + str(adj) + cost + '\n'
    fout = open(fileOut, mode='w')
    fout.write(gra)
    fout.close()


# add-on: sorts adjacency lists -> to have same results as those asked in tutorials/exams

def sort(G):
    """
    sort adjacency lists -> to have same results as those asked in tutorials/exams
    """
    for i in range(G.order):
        G.adjlists[i].sort()

#
def fromlist(order, directed, edges):
    """Build a new graph from an int tuple list.

    Args:
        order (int): Order of graph.
        directed (bool): True if the graph is directed. False otherwise.
        edges (List[(int, int)]): Source/Destination tuple list.

    Returns:
        Graph: New graph.

    Raises:
        IndexError: If either order or edge extremity is invalid.

    """

    # Check order:
    if order <= 0:
        raise IndexError('Invalid order')
    # Build graph
    g = Graph(order, directed)
    for (src, dst) in edges:
        g.addedge(src, dst)
    return g

# Another way to display graphs

def displaySVG(ref, filename='temp'):
    """Render a graph to SVG format.

    *Warning:* Made for use within IPython/Jupyter only.

    Args:
        ref (Graph).
        filename (str): Temporary filename to store SVG output.

    Returns:
        SVG: IPython SVG wrapper object for graph.

    """

    # Ensure all modules are available
    try:
        from graphviz import Graph as gvGraph, Digraph as gvDigraph
        from IPython.display import SVG
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    # Traverse graph and generate temporary Digraph/Graph object
    output_format = 'svg'
    if ref.directed:
        graph = gvDigraph(filename, format=output_format)
    else:
        graph = gvGraph(filename, format=output_format)
    if ref is not None:
        for src in range(ref.order):
            src_id = 'node_' + str(src)
            graph.node(src_id, label=str(src))
            for dst in ref.adjlists[src]:
                if ref.directed or src >= dst:
                    graph.edge(src_id, 'node_' + str(dst))
    # Render to temporary file and SVG object
    graph.render(filename=filename, cleanup=True)
    return SVG(filename + '.' + output_format)

