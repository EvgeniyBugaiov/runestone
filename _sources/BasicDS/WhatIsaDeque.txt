..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Что такое дек?
~~~~~~~~~~~~~~

**Дек**, также называемый двусторонней очередью, - это упорядоченная
коллекция элементов, подобная очереди. Он имеет два конца (голову и хвост),
и его элементы остаются позиционированными. Что отличает дек, так это
нестрогая природа добавления и удаления его составляющих. Новые элементы могут
быть добавлены как в голову, так и в хвост. Аналогично, существующие компоненты
могут удаляться из обоих концов. В каком-то смысле, этот гибрид линейной
структуры объединяет все возможности стеков и очередей. :ref:`Рисунок 1 <fig_basicdeque>` демонстрирует дек из объектов данных Python.

Важно отметить, что несмотря на обладание деком многих характеристик стеков и
очередей, он не поддерживает LIFO или FIFO упорядочение, которые воплощаются в
жизнь этими структурами данных. Только от вас зависит, какого типа операции
добавления или удаления использовать.

.. _fig_basicdeque:

.. figure:: Figures/basicdeque.png
   :align: center

   Рисунок 1: Дек из объектов данных Python

.. disqus::
