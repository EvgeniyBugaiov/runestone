..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Реализация дека в Python
~~~~~~~~~~~~~~~~~~~~~~~~

Создадим новый класс для реализации АТД "дек", как мы
неоднократно делали в предыдущих разделах. Список Python вновь предоставит
очень хороший набор методов, с помощью которых мы построим детализацию этой структуры данных.
Наша реализация (:ref:`листинг 1 <lst_dequecode>`) будет предполагать, что хвост
дека находится в нулевой позиции списка.

.. _lst_dequecode:

.. highlight:: python
   :linenothreshold: 5

**Листинг 1**

::

    class Deque:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def addFront(self, item):
            self.items.append(item)

        def addRear(self, item):
            self.items.insert(0,item)

        def removeFront(self):
            return self.items.pop()

        def removeRear(self):
            return self.items.pop(0)

        def size(self):
            return len(self.items)

.. highlight:: python
   :linenothreshold: 500

В ``removeFront`` мы используем метод ``pop`` для удаления последнего
элемента из списка. Однако, в ``removeRear`` метод ``pop(0)`` должен
удалять первый из них. Также нам нужно использовать метод ``insert``
(строка 12) в ``addRear``, поскольку ``append`` предполагает добавление
нового элемента в конец списка.


CodeLens 1 демонстрирует класс ``Deque`` в последовательности действий,
которую мы представили в :ref:`таблице 1 <tbl_dequeoperations>`.

.. codelens:: deqtest
   :caption: Пример операций над деком

   class Deque:
       def __init__(self):
           self.items = []

       def isEmpty(self):
           return self.items == []

       def addFront(self, item):
           self.items.append(item)

       def addRear(self, item):
           self.items.insert(0,item)

       def removeFront(self):
           return self.items.pop()

       def removeRear(self):
           return self.items.pop(0)

       def size(self):
           return len(self.items)

   d=Deque()
   print(d.isEmpty())
   d.addRear(4)
   d.addRear('dog')
   d.addFront('cat')
   d.addFront(True)
   print(d.size())
   print(d.isEmpty())
   d.addRear(8.4)
   print(d.removeRear())
   print(d.removeFront())
   

Можно найти много сходства в коде на Python, описывающем стеки и
очереди. Вероятно, вы также заметили, что в этой реализации добавление
и удаление элементов из головы имеет O(1), в то время как те же операции
для хвоста - O(n). Это и следовало ожидать, учитывая какие распространённые
методы использовались для этой цели. Опять же, главное, в чём мы должны
быть уверены, так это в том, что в нашей реализации назначено хвостом,
а что головой дека.

.. disqus::
