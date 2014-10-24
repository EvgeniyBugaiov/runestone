..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Реализация
~~~~~~~~~~

Реализовать список смежности на Python с помощью словарей очень легко. Для АТД графа мы создадим два класса (см. :ref:`листинг 1 <lst_vertex>` и :ref:`листинг 2 <lst_graph>`): ``Graph``, содержащий основной список вершин, и ``Vertex`` - представление каждой из них в графе.

Объекты ``Vertex`` будут использовать словарь для отслеживания смежных вершин и весов рёбер. Называться он будет ``connectedTo``. Листинг ниже показывает код для класса ``Vertex``. Конструктор просто инициализирует ``id`` (обычную строку) и словарь ``connectedTo``. Метод ``addNeighbor`` используется для добавления связи данной вершины с другой. Метод ``getConnections`` возвращает все вершины из списка смежности, которые представлены в ``connectedTo``. Метод ``getWeight`` возвращает вес ребра из этой вершины к передаваемой ему в качестве параметра.

.. _lst_vertex:

**Листинг 1**

::

    class Vertex:
        def __init__(self,key):
            self.id = key
            self.connectedTo = {}

        def addNeighbor(self,nbr,weight=0):
            self.connectedTo[nbr] = weight

        def __str__(self):
            return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

        def getConnections(self):
            return self.connectedTo.keys()

        def getId(self):
            return self.id

        def getWeight(self,nbr):
            return self.connectedTo[nbr]

Класс ``Graph``, показанный в следующем листинге, содержит словарь, отображающий имена вершин на их объекты. На :ref:`рисунке 4 <fig_adjlist>` последний показан затенённым серым прямоугольником. Также ``Graph`` предоставляет методы для добавления вершин в граф и связывания их друг с другом. Дополнительно мы имеем реализацию метода ``__iter__``, облегчающего итерации по объектам ``Vertex`` в конкретном графе. Вместе два метода позволяют делать итерации по именам вершин или непосредственно по объектам.

.. _lst_graph:

**Листинг 2**

::

    class Graph:
        def __init__(self):
            self.vertList = {}
            self.numVertices = 0
            
        def addVertex(self,key):
            self.numVertices = self.numVertices + 1
            newVertex = Vertex(key)
            self.vertList[key] = newVertex
            return newVertex
        
        def getVertex(self,n):
            if n in self.vertList:
                return self.vertList[n]
            else:
                return None

        def __contains__(self,n):
            return n in self.vertList
        
        def addEdge(self,f,t,cost=0):
            if f not in self.vertList:
                nv = self.addVertex(f)
            if t not in self.vertList:
                nv = self.addVertex(t)
            self.vertList[f].addNeighbor(self.vertList[t], cost)
        
        def getVertices(self):
            return self.vertList.keys()
            
        def __iter__(self):
            return iter(self.vertList.values())

Следующая сессия Python создаёт граф с :ref:`рисунка 2 <fig_dgsimple>`, используя свежеопределённые классы ``Graph`` и ``Vertex``. Сначала мы создаём шесть вершин, пронумерованных от 0 до 5. Затем печатаем словарь, их содержащий. Обратите внимание, что для каждого ключа от 0 до 5 создаётся сущность класса ``Vertex``. Далее добавляем рёбра, связывающие вершины вместе. Наконец, вложенный цикл удостоверяется, что каждое ребро в графе сохранено правильно. Вы можете сравнить вывод списка рёбер в конце сессии с :ref:`рисунком 2 <fig_dgsimple>`.

::

    >>> g = Graph()
    >>> for i in range(6):
    ...    g.addVertex(i)
    >>> g.vertList
    {0: <adjGraph.Vertex instance at 0x41e18>, 
     1: <adjGraph.Vertex instance at 0x7f2b0>, 
     2: <adjGraph.Vertex instance at 0x7f288>, 
     3: <adjGraph.Vertex instance at 0x7f350>, 
     4: <adjGraph.Vertex instance at 0x7f328>, 
     5: <adjGraph.Vertex instance at 0x7f300>}
    >>> g.addEdge(0,1,5)
    >>> g.addEdge(0,5,2)
    >>> g.addEdge(1,2,4)
    >>> g.addEdge(2,3,9)
    >>> g.addEdge(3,4,7)
    >>> g.addEdge(3,5,3)
    >>> g.addEdge(4,0,1)
    >>> g.addEdge(5,4,8)
    >>> g.addEdge(5,2,1)
    >>> for v in g:
    ...    for w in v.getConnections(): 
    ...        print("( %s , %s )" % (v.getId(), w.getId()))
    ... 
    ( 0 , 5 )
    ( 0 , 1 )
    ( 1 , 2 )
    ( 2 , 3 )
    ( 3 , 4 )
    ( 3 , 5 )
    ( 4 , 0 )
    ( 5 , 4 )
    ( 5 , 2 )
