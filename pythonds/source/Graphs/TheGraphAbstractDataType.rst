..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Абстрактный тип данных "граф"
-----------------------------

АТД "граф" определяется следующим образом:

-  ``Graph()`` создаёт новый пустой граф.

-  ``addVertex(vert)`` добавляет в граф объект типа ``Vertex``.

-  ``addEdge(fromVert, toVert)`` Добавляет в граф новое направленное ребро, соединяющее две вершины.

-  ``addEdge(fromVert, toVert, weight)`` Добавляет в граф новое взвешенное направленное ребро, соединяющее две вершины.

-  ``getVertex(vertKey)`` находит в графе вершину ``vertKey``.

-  ``getVertices()`` возвращает список всех вершин графа.

-  ``in`` возвращает ``True`` для оператора формы ``vertex in graph``, если данная вершина в графе имеется, и ``False`` в противном случае.

Взяв за отправную точку формальное определение, АТД *граф* с помощью Python можно реализовать несколькими способами. Мы увидим, что каждый из них имеет свою цену. Есть две широко известные реализации графа: **матрица смежности** и **список смежности**. Мы объясним их обе, а затем воплотим в классах на Python.
