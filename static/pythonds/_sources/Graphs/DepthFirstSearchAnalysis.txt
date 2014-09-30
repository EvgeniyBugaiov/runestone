..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Анализ поиска в глубину
~~~~~~~~~~~~~~~~~~~~~~~

В общем случае время выполнения поиска в глубину следующее. Оба цикла в ``dfs`` выполняются за :math:`O(V)` (без учёта происходящего в ``dfsvisit``), поскольку они вычисляются по одному разу для каждой вершины графа. Цикл в ``dfsvisit`` вычисляется один раз для каждого ребра из списка смежности текущей вершины. Поскольку ``dfsvisit`` вызывается рекурсивно только в том случае, если вершина окрашена в белый, то цикл для каждого ребра графа выполнится максимум единожды (:math:`O(E)`). Таким образом, общее время выполнения поиска в глубину равно :math:`O(V + E)`.


