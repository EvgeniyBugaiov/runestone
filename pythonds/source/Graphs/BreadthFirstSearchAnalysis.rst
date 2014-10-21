..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Анализ поиска в ширину
~~~~~~~~~~~~~~~~~~~~~~~

Прежде, чем перейти к другим алгоритмам для графов, давайте проанализируем временнУю производительность поиска в ширину. В первую очередь нужно заметить, что для каждой вершины из :math:`|V|` происходит как минимум одно вычисление цикла ``while``. Вы можете убедиться, что это так, поскольку вершина должна быть окрашена в белый перед тем, как быть проверенной и добавленной в очередь. Это даёт нам :math:`O(V)` для цикла ``while``. Вложенный цикл ``for`` вычисляется минимум один раз для каждого ребра из :math:`|E|`. Причина этого в том, что каждая вершина (например, :math:`u`) хотя бы единожды извлекается из очереди, и мы проверяем ребро из :math:`u` в :math:`v` только в этом случае. Это даёт :math:`O(E)` для каждого цикла ``for``. Комбинируя два цикла вместе, получим :math:`O(V + E)`.

Конечно, поиск в ширину - всего лишь часть задания. Проследовать по ссылкам от стартового узла до целевого является его второй частью. Наихудшим случаем станет граф в виде обычной длинной цепочки. Тогда проход по всем вершинам даст :math:`O(V)`. Обычно же берётся некая часть :math:`|V|`, но мы по-прежнему будем писать :math:`O(V)`.

Наконец, для данной задачи потребуется время на постороение начального графа. Мы оставляем анализ функции ``buildGraph`` в качестве упражнения для вас.
