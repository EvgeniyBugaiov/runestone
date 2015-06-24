..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Реализация стека на Python
~~~~~~~~~~~~~~~~~~~~~~~~~~

Теперь, когда у нас есть чёткое определение АТД стека,
обратим своё внимание на использование Python для его реализации.
Напомним, что когда мы даём физическую реализацию абстрактного типа данных,
то подразумеваем реализацию структуры данных.

Как мы уже говорили в главе 1, в Python (как и в любом объектно-ориентированном
языке) реализация выбранного абстрактного типа данных (например, стека) - это
создание нового класса. Стековые операции воплотятся в его методах. Далее,
чтобы реализовать стек, который суть - коллекция элементов, имеет смысл
воспользоваться мощью и простотой примитивных коллекций, предоставляемых
Python. Мы будем использовать список.

Напомним, что класс списка в Python предоставляет механизм и набор методов для
упорядоченной коллекции. Например, если у нас есть список [2, 5, 3, 6, 7, 4], то
нам нужно только определиться, который из его концов принять за вершину стека,
а который - за базу. Как только решение принято, можно начинать реализовывать
операции, используя такие списковые методы, как ``append`` и ``pop``

Нижеследующая реализация стека (:ref:`ActiveCode 1 <lst_stackcode1>`) предполагает,
что верхний элемент стека расположен в конце списка. По мере роста стека (имеет место
операция ``push``), новые элементы будут добавляться туда же. Им же будет
манипулировать операция ``pop``

.. _lst_stackcode1:


.. activecode:: stack_1ac
   :caption: Реализация класса Stack с использованием списков Python

   class Stack:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def peek(self):
            return self.items[len(self.items)-1]

        def size(self):
            return len(self.items)

Помните, что с нажатием кнопки ``run`` не произойдёт ничего, кроме объявления
класса. Мы должны создать объект ``Stack``, а затем его использовать.
:ref:`ActiveCode 2 <lst_stackcode1>` демонстрирует класс ``Stack`` в действии,
которое мы представили последовательностью операций из :ref:`таблицы 1 <tbl_stackops>`


.. activecode:: stack_ex_1
   :include:  stack_1ac

   from pythonds.basic.stack import Stack

   s=Stack()
   
   print(s.isEmpty())
   s.push(4)
   s.push('dog')
   print(s.peek())
   s.push(True)
   print(s.size())
   print(s.isEmpty())
   s.push(8.4)
   print(s.pop())
   print(s.pop())
   print(s.size())



Важно отметить, что мы можем выбрать реализацию стека через список, где
вершиной считается первый, а не последний элемент. В этом случае предыдущие
методы ``append`` и ``pop`` работать не будут. Мы должны будем явно использовать
``pop`` и ``insert`` для позиции с индексом 0 (первый элемент в списке).
Реализация показана в :ref:`CodeLens 1 <lst_stackcode2>`


.. _lst_stackcode2:

.. codelens:: stack_cl_1
   :caption: Альтернативная реализация класса Stack

   class Stack:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def push(self, item):
            self.items.insert(0,item)

        def pop(self):
            return self.items.pop(0)

        def peek(self):
            return self.items[0]

        def size(self):
            return len(self.items)

   s = Stack()
   s.push('hello')
   s.push('true')
   print(s.pop())


Эта возможность изменять физическое воплощение абстрактного типа данных
при поддержке логических характеристик - пример того, как работает абстракция.
Однако, даже если стек будет вести себя аналогично, рассмотрение
производительности этих двух реализаций покажет их несомненное различие.
Напомним, что операции ``append`` и ``pop`` обе являются О(1). Это означает,
что первая реализация будет выполнять добавление и выталкивание за постоянное
время, независимо от количества элементов в стеке. Производительность второго
варианта страдает, поскольку и ``insert(0)``, и ``pop(0)`` для стека, размером
n, являются O(n). Очевидно, что даже если в реализации логически эквивалентны,
то при тестировании они будут иметь очень разные затраты по времени.


.. admonition:: Самопроверка

   .. mchoicemf:: stack_1
      :iscode:
      :answer_a: 'x'
      :answer_b: 'y'
      :answer_c: 'z'
      :answer_d: Стек пуст
      :correct: c
      :feedback_a: Помните, что стек строится снизу вверх.
      :feedback_b: Помните, что стек строится снизу вверх.
      :feedback_c: Хорошая работа!
      :feedback_d: Помните, что стек строится снизу вверх.

      Дана следующая последовательность стековых операций. Что будет на вершине стека, когда она завершится?
       
      .. code-block:: python
       
       m = Stack()
       m.push('x')
       m.push('y')
       m.pop()
       m.push('z')
       m.peek()

   .. mchoicemf:: stack_2
      :answer_a: 'x'
      :answer_b: стек пуст
      :answer_c: возникнет ошибка
      :answer_d: 'z'
      :correct: c
      :feedback_a: Вам стоит проверить docs на пустоту
      :feedback_b: В стеке нечётное количество элементов, но за каждый проход по циклу выталкиваются два из них
      :feedback_c: Отличная работа!
      :feedback_d: Вам стоит проверить docs на пустоту

      Дана следующая последовательность стековых операций. Что будет на вершине стека, когда последовательность завершится?

      .. code-block:: python
  
        m = Stack()
        m.push('x')
        m.push('y')
        m.push('z')
        while not m.isEmpty():
           m.pop()
           m.pop()

   Напишите функцию ``revstring(mystr)``, используя стек для изменения порядка символов в строке на противоположный.

   .. actex:: stack_stringrev

      from test import testEqual
      from pythonds.basic.stack import Stack

      def revstring(mystr):
          # место для вашего кода

      testEqual(revstring('apple'),'elppa')
      testEqual(revstring('x'),'x')
      testEqual(revstring('1234567890'),'0987654321')


.. video:: stack1_video
    :controls:
    :thumb: ../_static/activecodethumb.png

    http://media.interactivepython.org/pythondsVideos/Stack1.mov
    http://media.interactivepython.org/pythondsVideos/Stack1.webm


.. disqus::
