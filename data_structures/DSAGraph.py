from linkedLists import *
from DSASorts import *
from DSAQueue import *
from DSAStack import *
import numpy as np


class DSAGraph:
    def __init__(self):
        self._vertices = DSALinkedList()
        self._edges = DSALinkedList()

    def __str__(self):
        ...

    def getEdges(self):
        return self._edges



    # def getVertex(self, label):
    #   x = self._vertices.head
    #   z = x.value
    #   while z.getLabel() != label and x.next != None:
    #       x = x.next
    #       z = x.value
        
    #   return z

    def getEdge(self, ffrom, to, value):
        x = self._edges.head
        z = x.value
        compare = str(ffrom + to + str(value))
        found = str(z.getFrom() + z.getTo() + str(z.getValue()))
        #print(compare, ' ', found, 'e1')
        while compare != found and x.next != None:
            x = x.next
            z = x.value
            found = str(z.getFrom() + z.getTo() + str(z.getValue()))
            #print(compare, ' ', found, 'e2')
        
        return z

    def getEdge2(self, ffrom, to):
        x = self._edges.head
        z = x.value
        compare = str(ffrom + to)
        found = str(z.getFrom() + z.getTo())
        #print(compare, 'compare VS ', found)
        #print(compare, ' ', found, 'e1')
        while compare != found and x.next != None:
            x = x.next
            z = x.value
            found = str(z.getFrom() + z.getTo())
            #print(compare, ' ', found, 'e2')
        
        return z

    def deleteEdge(self, ffrom, to, value):
        dele = self.getEdge(ffrom, to, value)
        self.getEdges().deleteNode(dele)

        #print(self.getVertex(ffrom)._links, self.getVertex(to)._links, 'BEFORE')
        self.getVertex(ffrom)._links.deleteNode(to)
        self.getVertex(to)._links.deleteNode(ffrom)
        #print(self.getVertex(ffrom)._links, self.getVertex(to)._links, 'AFTER')

    def addVertex(self, label):
        self._vertices.insertLast(DSAGraphVertex(label))
        
    def getVertexLabels(self):
        x = [i.getLabel() for i in self._vertices]
        return DSASorts().insertionSort(x)

    def getVertices(self):
        x = [self.getVertex(i) for i in self.getVertexLabels()]
        return x
    
    def printAdjList(self):
        for z in self._vertices:
            print(z.getLabel() + ': ' + str(DSASorts().insertionSort([i for i in z._links])))

    def adjMatrix(self):
        adj_matrix = np.zeros((self.getVertexCount(), self.getVertexCount()), dtype=int)
        x = [i.getLabel() for i in self._vertices]
        y = [i for i in range(len(self._vertices))]
        indc = dict(zip(x,y))
        for i,z in enumerate(self._vertices):
            for j in z._links:
                adj_matrix[i,indc[j]] = 1

        return adj_matrix


    def addEdge(self, v1, v2, directed = False):
        if directed == False:
            self.getVertex(v1)._links.insertLast(v2)
            self.getVertex(v2)._links.insertLast(v1)
        else:
            self.getVertex(v1)._links.insertLast(v2)


    def addEdge2(self, v1, v2, value, directed = False):
        self._edges.insertLast(DSAGraphEdge(v1, v2, value, directed))
        # print('inserted: ' + v1 + v2 + ' ' + str(value))
        # for i in self._edges:
        #   print(i, 'in edge')

        # keeps old stuff too
        if directed == False:
            self.getVertex(v1)._links.insertLast(v2)
            self.getVertex(v2)._links.insertLast(v1)
        else:
            self.getVertex(v1)._links.insertLast(v2)


    def getVertexCount(self):
        count = 0
        for i in self._vertices:
            count += 1
        return count

    def getEdgeCount(self):
        count = 0
        for i in self._vertices:
            for z in i._links:
                count += 1

        return count

    def getVertex(self, label):
        x = self._vertices.head
        z = x.value
        while z.getLabel() != label and x.next != None:
            x = x.next
            z = x.value
        
        return z


    def breadthFirst(self):
        for i in self._vertices:
            i.setVisited(False)

        result = []
        x = self.getVertices()
        qq = DSAQueue()

        result.append(str(x[0]))
        x[0].setVisited(True)

        for i in DSASorts().insertionSort([i for i in x[0]._links]):
            qq.enqueue(self.getVertex(i))
            result.append(i)
            self.getVertex(i).setVisited(True)

        while not qq.isEmpty():
            cur = qq.dequeue()
            for i in cur._links:
                if self.getVertex(str(i)).getVisited() == False:
                    qq.enqueue(self.getVertex(i))
                    result.append(i)
                    self.getVertex(i).setVisited(True)

        return result

    def hasCycleMultiple(self):
        results = []

        for ii in range(len(self.getVertices())):
            x = self.getVertices()
            for i in self._vertices:
                i.setVisited(False)
            flag = False
            seen = []
            ss = DSAStack()
            ss.push(x[ii])

            while not ss.isEmpty() and len(set([i.getLabel() for i in ss])) == len(ss):
                cur = ss.pop()
                for i in cur._links:
                    if self.getVertex(i).getVisited() == False:
                        ss.push(self.getVertex(i))
                seen.append(cur)
                cur.setVisited(True)

            if len(set([i.getLabel() for i in ss])) != len(ss):
                flag = True

            results.append(flag)

        rr = set(results)
        if len(rr) != 1:
            flag = True
        elif len(rr) == 1:
            if False in rr:
                flag = False
            elif True in rr:
                flag = True

        return flag

    def hasCycle(self):
        flag = False

        for i in self._vertices:
            i.setVisited(False)

        seen = []
        x = self.getVertices()
        ss = DSAStack()

        ss.push(x[0])

        while not ss.isEmpty() and len(set([i.getLabel() for i in ss])) == len(ss):
            cur = ss.pop()
            for i in cur._links:
                if self.getVertex(i).getVisited() == False:
                    ss.push(self.getVertex(i))
            seen.append(cur)
            cur.setVisited(True)

        if len(set([i.getLabel() for i in ss])) != len(ss):
            flag = True

        return flag



    def depthFirst(self):
        for i in self._vertices:
            i.setVisited(False)

        result = []
        x = self.getVertices()
        ss = DSAStack()

        ss.push(x[0])
        result.append(str(x[0]))
        x[0].setVisited(True)

        while not ss.isEmpty():
            #print([i.getLabel() for i in ss])
            cur = ss.top()
            #print(cur)
            # print('top is ')
            # print(cur)
            # print('has unvisited? ' + str(self.hasUnvisited(cur.getLabel())))

            if self.hasUnvisited(cur.getLabel()):
                cur = self.getUnvisited(cur.getLabel())
                # print('got unvisited as: ' + str(cur))
                ss.push(cur)
                result.append(str(cur))
                cur.setVisited(True)
                #print(cur)
            else:
                ss.pop()

        return result


    def depthFirstVisitedList(self, start_vertex):
        for i in self._vertices:
            i.setVisited(False)

        x = self.getVertices()
        y = [i.getLabel() for i in x]

        found = None
        for i,v in enumerate(y):
            if v == str(start_vertex):
                target = i
                found = True
            else:
                if found != True:
                    found = False

        if found == False or found == None:
            return
        else:
            pass

        ss = DSAStack()
        absolute_visited = DSALinkedList()

        ss.push(x[target])
        x[target].setVisited(True)

        while not ss.isEmpty():
            cur = ss.top()
            absolute_visited.insertLast(cur)
            if len(set(absolute_visited)) == len(x):
                return absolute_visited
            else:
                if self.hasUnvisited(cur.getLabel()):
                    cur = self.getUnvisited(cur.getLabel())
                    ss.push(cur)
                    cur.setVisited(True)
                else:
                    ss.pop()

        return None


    def kruskalsAlgorithm(self, val_idx):
        gg = DSAGraph()
        ll = DSALinkedList()
        count = 0

        temp = self.getEdges()
        for i in temp:
            ll.insertLast(i.getFrom())
            ll.insertLast(i.getTo())
        
        v_list = np.array(list(set(ll)))
        
        for i in v_list:
            gg.addVertex(i)

        temp2 = np.empty(len(temp), dtype=object)
        for i,z in enumerate(temp):
            entry = np.empty(2, dtype=object)
            entry[0] = z.getValue()[val_idx]
            entry[1] = z
            temp2[i] = entry

        sorted_edges = DSASorts().edgeSort(temp2)
        # temp = np.array(sorted(temp, key=lambda x: x.getValue()[val_idx], reverse=False))

        stop_point = len(v_list) - 1 # v - 1
        e_count = 0

        while e_count < stop_point and count < len(temp):
            gg.addEdge2(sorted_edges[count][1].getFrom(), sorted_edges[count][1].getTo(), sorted_edges[count][1].getValue(), False)
            e_count += 1

            temp2 = self.getEdges()
            for i in temp2:
                ll.insertLast(i.getFrom())
                ll.insertLast(i.getTo())
            v_list_len = len(list(set(ll)))
            dfs_len = len(gg.depthFirst())

            if v_list_len != dfs_len:
                if gg.hasCycleMultiple():
                    gg.deleteEdge(sorted_edges[count][1].getFrom(), sorted_edges[count][1].getTo(), sorted_edges[count][1].getValue())
                    e_count -= 1
            elif v_list_len == dfs_len:
                if gg.hasCycle():
                    gg.deleteEdge(sorted_edges[count][1].getFrom(), sorted_edges[count][1].getTo(), sorted_edges[count][1].getValue())
                    e_count -= 1

            count += 1

        return gg


    def hasUnvisited(self, vertex):
        z = self.getVertex(vertex)
        ordered_links = DSASorts().insertionSort([i for i in z._links])
        total_adj = len(z._links)
        count = 0
        flag = None

        while flag != True and count < total_adj:
            if self.getVertex(ordered_links[count]).getVisited() == True:
                count += 1
            else:
                flag = True

        if count == total_adj:
            flag = False

        if total_adj == 0:
            flag = None

        return flag


    def getUnvisited(self, vertex):
        flag = False
        z = self.getVertex(vertex)
        adj = DSASorts().insertionSort([i for i in z._links])
        total_adj = len(z._links)
        count = 0
        value = None

        while flag == False and count < total_adj:
            if self.getVertex(adj[count]).getVisited() == False:
                value = self.getVertex(adj[count])
                flag = True
            else:
                count += 1

        return value


class DSAGraphVertex():
    def __init__(self, inLabel):
        self._label = inLabel
        self._links = DSALinkedList()
        self._visited = False

    def __str__(self):
        return str(self._label)

    def getLabel(self):
        return self._label

    def setVisited(self, visited):
        self._visited = visited

    def getVisited(self):
        return self._visited

class DSAGraphEdge():
    def __init__(self, v1, v2, inValue, directed = False):
        self._value = inValue
        self._from = v1
        self._to = v2
        self._label = str(v1) + str(v2)
        self._directed = directed
        self._visited = False

    def __str__(self):
        return str(self._label)

    def getLabel(self):
        return self._label

    def getValue(self):
        return self._value

    def getFrom(self):
        return self._from

    def getTo(self):
        return self._to

    def isDirected(self):
        return self._directed

    def __str__(self):
        return str(self._label) + ' : ' + str(self._value)
