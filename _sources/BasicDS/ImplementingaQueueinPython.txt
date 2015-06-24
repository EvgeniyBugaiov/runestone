..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Реализация очереди на Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для реализации АТД очереди подходящим решением вновь станет создание нового класса.
Как и раньше, для построения внутреннего представления очереди мы будем
использовать мощь и простоту коллекции "список".

Нам надо определиться, какой конец списках считать головой, а какой - хвостом.
Реализация, показанная в :ref:`листинге 1 <lst_queuecode>` предполагает, что
последний элемент очереди находится на его нулевой позиции. Это позволяет
использовать функцию ```insert``` для добавления новых элементов в конец
очереди. Операция ```pop``` будет использоваться для удаления переднего элемента
(последнего элемента в списке). Напомним, что также это означает постановку
в очередь за O(n), а извлечение - за O(1) времени.

.. _lst_queuecode:

**Листинг 1**

::

    class Queue:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def enqueue(self, item):
            self.items.insert(0,item)

        def dequeue(self):
            return self.items.pop()

        def size(self):
            return len(self.items)

CodeLens 1 демонстрирует класс ``Queue`` в действии
для последовательности операций из :ref:`таблицы 1 <tbl_queueoperations>`


.. codelens:: ququeuetest
   :caption: Пример операций очереди

   class Queue:
       def __init__(self):
           self.items = []

       def isEmpty(self):
           return self.items == []

       def enqueue(self, item):
           self.items.insert(0,item)

       def dequeue(self):
           return self.items.pop()

       def size(self):
           return len(self.items)

   q=Queue()
   q.isEmpty()
   
   q.enqueue('dog')
   q.enqueue(4)
   q=Queue()
   q.isEmpty()
   
   q.enqueue(4)
   q.enqueue('dog')
   q.enqueue(True)

::

    >>> q.size()
    3
    >>> q.isEmpty()
    False
    >>> q.enqueue(8.4)
    >>> q.dequeue()
    4
    >>> q.dequeue()
    'dog'
    >>> q.size()
    2

.. admonition:: Самопроверка

   .. mchoicemf:: queue_1
      :correct: b
      :iscode:
      :answer_a: 'hello', 'dog'
      :answer_b: 'dog', 3
      :answer_c: 'hello', 3
      :answer_d: 'hello', 'dog', 3
      :feedback_a: Помните: что первым добавляется, то первым и удаляется (FIFO)
      :feedback_b: Верно, "первым пришёл - первым вышел" означает, что "hello" будет удалено
      :feedback_c: Очереди и стеки - это структуры данных, в которых вы имеете доступ только к первому и последнему элементам
      :feedback_d: Упс, кажется вы упустили вызов ``dequeue`` в самом конце

      Предположим, что у вас есть следующая последовательность операций с кодом.

      ::
      
          q = Queue()
          q.enqueue('hello')
          q.enqueue('dog')
          q.enqueue(3)
          q.dequeue()

      Какие элементы находятся в очереди слева?


.. disqus::
