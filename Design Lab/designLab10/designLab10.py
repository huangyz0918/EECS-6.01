import heapq
from highways import *
from lib601.plotWindow import PlotWindow
from lib601.search import search,SearchNode

class PriorityQueue:
    def __init__(self, items=None):
        self.items = [] if items is None else items
        heapq.heapify(self.items)

    def push(self, item, priority):
        heapq.heappush(self.items, (priority, item))

    def pop(self):
        return heapq.heappop(self.items)

    def __len__(self):
        return self.items.__len__()

    def __str__(self):
        return "PriorityQueue(%r)" % self.items

def pathCost(path):
    cost = 0
    i = 0
    for i in range(len(path)-1):
            node1 = locationFromID[path[i]]
            node2 = locationFromID[path[i+1]]
            cost += distance(node1.id_number, node2.id_number)
    return cost

def highway_successors(state):
    return neighbors[state]

def uc_successors(state):
    al = []
    nex = neighbors[state]
    for idn in nex:
        al.append((idn,distance(state,idn)))
    return al

def testsearch():
    startState = 2000071
    goalTest = lambda idn: idn == 25000502
    return search(highway_successors, startState, goalTest, dfs=False)

def ucSearch(successors, startState, goalTest, alpha, heuristic=lambda s: 0):
    if goalTest(startState):
        return [startState]
    agenda = PriorityQueue()
    agenda.push(SearchNode(startState, None, cost=0), heuristic(startState))
    expanded = set()
    while len(agenda) > 0:
        priority, parent = agenda.pop()
        if parent.state not in expanded:
            expanded.add(parent.state)
            if goalTest(parent.state):
                print len(expanded)
                return parent.path()
            for childState, cost in successors(parent.state):
                child = SearchNode(childState, parent, parent.cost+cost)
                if childState not in expanded:
                    agenda.push(child, ((10.0-alpha)/10.0)*child.cost+(alpha/10.0)*heuristic(childState))
    return None

def testucsearch(alpha):
    startState = 6002971
    goalTest = lambda state: state == 25000502
    return ucSearch(uc_successors, startState, goalTest,  alpha, heuristic=lambda x: distance(x, 25000502))

def testplot():
    p = PlotWindow()
    xs = range(10) 
    ys = [pathCost(testucsearch(alpha)) for alpha in xs]
    p.plot(xs,ys)

def testplot2():
    p = PlotWindow()
    xs = range(10) 
    p.plot(xs,[85795,85402,84617,82383,73836,37048,798,1691,1885,1787])

