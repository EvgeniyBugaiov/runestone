..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Задача о ходе коня
~~~~~~~~~~~~~~~~~~

Чтобы проиллюстрировать второй распространённый алгоритм для графов, мы возьмём другую классическую задачу: "о ходе коня". Она разыгрывается на шахматной доске всего одной фигурой - конём. Целью головоломки является поиск такой последовательности ходов (маршрута), чтобы конь посетил каждую клетку доски ровно один раз. Эта задача очаровывает шахматных игроков, математиков и информатиков уже в течение многих лет. Верхний предел количества возможных маршрутов для шахматной доски 8х8 равен :math:`1.305 \times 10^{35}`. Однако, тупиковых вариантов неизмеримо больше. Очевидно, что задача из тех, которые требуют человеческого разума, компьютерной мощи или и того и другого вместе.

Хотя исследователи изучили множество различных алгоритмов для решения этой головоломки, поиск по графу - один из простейших для понимания и программирования. Мы вновь будем искать решение, используя два основных шага:

- Представим в виде графа осуществимые ходы коня по доске.

- Используем алгоритм для поиска в графе пути длиной :math:`rows \times columns - 1`, где каждая вершина будет посещена ровно один раз.
