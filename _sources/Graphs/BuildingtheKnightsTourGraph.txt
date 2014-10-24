..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Построение графа для задачи о ходе коня
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Чтобы представить задачу о ходе коня в виде графа, воспользуемся следующими двумя соображениями: каждая клетка на доске будет узлом, а каждый возможный ход фигуры - ребром. :ref:`Рисунок 1 <fig_knightmoves>` иллюстрирует соответствие доступных фигуре ходов рёбрам графа.

.. _fig_knightmoves:

.. figure:: Figures/knightmoves.png
   :align: center

   Рисунок 1: Доступные ходы коня, стоящего на клетке 12, и соответствующий им граф

Чтобы построить полный граф для доски :math:`n \times n`, мы используем код на Python, показанный в :ref:`листинге 1 <lst_knighttour1>`. Функция ``knightGraph`` совершает один проход через всю доску. В каждой из клеток она вызывает вспомогательную функцию ``genLegalMoves``, чтобы создать список возможных ходов для этой позиции. Все они конвертируются в рёбра графа. Другая вспомогательная функция ``posToNodeId`` преобразует положение фигуры на доске в терминах столбца и строки в линейный номер вершины, аналогичный номерам, показанным на :ref:`рисунке 1 <fig_knightmoves>`. 

.. _lst_knighttour1:

**Листинг 1**

::

    from pythonds.graphs import Graph
    
    def knightGraph(bdSize):
        ktGraph = Graph()
        for row in range(bdSize):
           for col in range(bdSize):
               nodeId = posToNodeId(row,col,bdSize)
               newPositions = genLegalMoves(row,col,bdSize)
               for e in newPositions:
                   nid = posToNodeId(e[0],e[1],bdSize)
                   ktGraph.addEdge(nodeId,nid)
        return ktGraph

Функция ``genLegalMoves`` (:ref:`листинг 2 <lst_knighttour2>`) принимает позицию коня на доске и генерирует восемь доступных ходов. Вспомогательная функция ``legalCoord`` (:ref:`листинг 2 <lst_knighttour2>`) проверяет, что сгенерированный ход всё ещё лежит на доске.

.. _lst_knighttour2:

**Листинг 2**

::


    def genLegalMoves(x,y,bdSize):
        newMoves = []
        moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                       ( 1,-2),( 1,2),( 2,-1),( 2,1)]
        for i in moveOffsets:
            newX = x + i[0]
            newY = y + i[1]
            if legalCoord(newX,bdSize) and \
                            legalCoord(newY,bdSize):
                newMoves.append((newX,newY))
        return newMoves

    def legalCoord(x,bdSize):
        if x >= 0 and x < bdSize:
            return True
        else:
            return False

На :ref:`рисунке 2 <fig_bigknight>` показан полный граф возможных ходов для доски :math:`8 \times 8`. Это ровно 336 рёбер. Обратите внимание: вершины, на которые отображаются клетки на краю доски, имеют меньше связей (возможных ходов), чем вершины из середины. Мы снова видим, насколько граф разрежен. Если бы он был полностью связан, то имел бы 4 096 рёбер. Но поскольку их в нём всего лишь 336, то матрица смежности будет заполнена всего на 8.2%

.. _fig_bigknight:

.. figure:: Figures/bigknight.png
   :align: center

   Рисунок 2: Все возможные ходы коня на доске :math:`8 \times 8`
