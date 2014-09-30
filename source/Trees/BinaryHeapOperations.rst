..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Операции с двоичной кучей
~~~~~~~~~~~~~~~~~~~~~~~~~

Основные операции, которые мы реализуем для нашей двоичной кучи, следующие:

-  ``BinaryHeap()`` создаёт новую пустую двоичную кучу.

-  ``insert(k)`` добавляет в кучу новый элемент.

-  ``findMin()`` возвращает элемент с минимальным значением ключа, оставляя его в куче.

-  ``delMin()`` возвращает элемент с минимальным значением ключа, удаляя его из кучи.

-  ``isEmpty()`` возвращает истину, если куча пуста, ложь в противном случае.

-  ``size()`` возвращает количество элементов в куче.

-  ``buildHeap(list)`` создаёт новую кучу из списка ключей.

:ref:`ActiveCode 1 <lst_heap1>` демонстрирует использование некоторых из этих методов. Обратите внимание, что неважно, в каком порядке мы добавляем элементы, - каждый раз удаляется наименьший. Сосредоточимся на воплощении этой задумки.

.. _lst_heap1:


.. activecode:: heap1
    :caption: Использование двоичной кучи
    
    from pythonds.trees.binheap import BinHeap
    
    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    
    print(bh.delMin())

    print(bh.delMin())

    print(bh.delMin())

    print(bh.delMin())
