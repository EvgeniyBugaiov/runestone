..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Реализация упорядоченного списка
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Перед началом реализации упорядоченного списка нелишним будет
вспомнить, что положение элементов относительно друг друга основывается
на некой базовой характеристике. Упорядоченный список целых чисел,
представленный выше (17, 26, 31, 77 и 93), может быть выражен связанной
структурой, показанной на :ref:`рисунке 15 <fig_orderlinked>`.
Опять же, узел и ссылка идеально подходят для представления
взаимного расположения элементов.

.. _fig_orderlinked:

.. figure:: Figures/orderlinkedlist.png
   :align: center

   Рисунок 15: Упорядоченный связанный список


Для реализации класса ``OrderedList`` мы будем использовать ту же технику,
что и для неупорядоченного списка. Пустой список вновь будет обозначаться
ссылкой ``head`` на ``None`` (см. :ref:`листинг 8 <lst_orderlist>`).


.. _lst_orderlist:

**Листинг 8**

::

    class OrderedList:
        def __init__(self):
            self.head = None

Рассматривая операции для упорядоченного списка, стоит отметить, что методы
``isEmpty`` и ``size`` могут быть реализованы аналогично неупорядоченному
списку, поскольку имеют дело только с количеством узлов безотносительно их
содержимого. Также хорошо будет работать метод ``remove``, потому что нам
по-прежнему надо искать элемент, а затем окружающие узел ссылки, чтобы
удалить его. Два оставшихся метода - ``search`` и ``add`` - потребуют
некоторой модификации.

Поиск в неупорядоченном списке требует, чтобы мы обходили узлы по одному
за раз, пока не найдём искомый элемент или не выйдем за пределы списка
(``None``). Такой подход будет работать и для упорядоченного списка. В
том случае, когда элемент найдётся, - он будет тем, что нам нужен. Однако,
в случае, когда элемент не содержится в списке, мы можем воспользоваться
преимуществом упорядочения, чтобы остановить поиск как можно раньше.

Например, :ref:`рисунок 16 <fig_stopearly>` показывает упорядоченный связанный
список, в котором ищется значение 45. В процессе обхода мы начинаем с его головы
и сначала проверяем на соответствие 17. Поскольку 17 - не то, что мы
ищем, то смещаемся к следующему узлу - 26. Это снова не то, перемещаемся
к 31, а затем к 54. И тут кое-что меняется. Поскольку 54 не тот элемент,
что мы ищем, наша предыдущая стратегия должна заключаться в продвижении вперёд.
Однако, с учётом упорядоченности списка в этом больше нет необходимости.
Раз значение в узле больше, чем искомое, значит поиск можно останавливать и возвращать
``False``. Не существует способа значению оказаться среди остатка упорядоченного списка.

.. _fig_stopearly:

.. figure:: Figures/orderedsearch.png
   :align: center

   Рисунок 16: Поиск в упорядоченном списке


:ref:`Листинг 9 <lst_ordersearch>` показывает законченный метод ``search``.
Новое условие, обсуждаемое выше, можно вставить очень легко: добавить ещё
одну булеву переменную - ``stop`` - и инициализировать её ``False`` (строка 4).
Пока ``stop`` равно ```False``` мы можем продолжать поиск в списке (строка 5).
Если в любом из узлов обнаружится значение больше искомого, то 
``stop`` установится в ``True`` (строки 9-10). Оставшиеся строки идентичны поиску в
неупорядоченном списке.

.. _lst_ordersearch:

**Листинг 9**

::

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

Наиболее значительная модификация затронет метод ``add``. Напомним, что
в неупорядоченных списках он просто помещал новый элемент в голову списка -
самую доступную точку. К сожалению, с упорядоченным списком это больше не
сработает. Теперь нам надо искать специальное место, где будет размещаться
новый элемент среди уже существующих в упорядоченном списке.


Предположим, что есть упорядоченный список из 17, 26, 54, 77 и 93,
и мы хотим добавить в него значение 31. Метод ``add`` должен решить, что
новый элемент следует расположить между 26 и 54. :ref:`Рисунок 17 <fig_orderinsert>`
показывает необходимую вставку. Как мы объясняли ранее, нужно обойти
связанный список в поисках места, куда будет вставлен новый элемент.
Мы знаем, что место найдено, если мы или вышли за пределы списка (``current``
равно ``None``), или значение текущего узла стало больше, чем добавляемый элемент.
В нашем примере нас вынудит остановится появление значения 54.

.. _fig_orderinsert:

.. figure:: Figures/linkedlistinsert.png
   :align: center

   Рисунок 17: Добавление элемента в упорядоченный связанный список


Как мы уже видели для неупорядоченных списков, здесь понадобится дополнительная
ссылка (``previous``), поскольку ``current`` не сможет предоставить доступ к
узлу, который нужно будет изменить. :ref:`Листинг 10 <lst_orderadd>` показывает
законченный метод ``add``. Строки 2-3 устанавливают две внешние ссылки, а строки
9-10 вновь позволяют ``previous`` следовать на один узел после ``current`` во
время каждой итерации. Условие в строке 5 разрешает итерациям продолжаться до
тех пор, пока остаются непросмотренные узлы и значение текущего не превышает
искомое. Противный случай - когда итерация терпит неудачу - означает, что мы
нашли место для нового узла.

Остаток метода завершает двухшаговый процесс, показанный на
:ref:`рисунке 17 <fig_orderinsert>`. Поскольку для элемента был создан новый узел,
то остаётся единственный вопрос: куда он будет добавлен - в начало или в середину
связанного списка? Для ответа на него вновь используется ``previous == None``.

.. _lst_orderadd:

**Листинг 10**

::

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
Класс ``OrderedList`` с реализованными на данный момент методами можно
найти в ActiveCode 4.

Оставшиеся операции мы оставляем в качестве упражнения.
Вам следует внимательно рассмотреть, когда неупорядоченная реализация будет
работать правильно с учётом того, что теперь список упорядочен.

.. activecode:: orderedlistclass
   :caption: Класс ``OrderedList`` на данный момент
   :hidecode:
   
   class Node:
       def __init__(self,initdata):
           self.data = initdata
           self.next = None

       def getData(self):
           return self.data

       def getNext(self):
           return self.next

       def setData(self,newdata):
           self.data = newdata

       def setNext(self,newnext):
           self.next = newnext


   class OrderedList:
       def __init__(self):
           self.head = None

       def search(self,item):
           current = self.head
           found = False
           stop = False
           while current != None and not found and not stop:
               if current.getData() == item:
                   found = True
               else:
                   if current.getData() > item:
                       stop = True
                   else:
                       current = current.getNext()

           return found

       def add(self,item):
           current = self.head
           previous = None
           stop = False
           while current != None and not stop:
               if current.getData() > item:
                   stop = True
               else:
                   previous = current
                   current = current.getNext()

           temp = Node(item)
           if previous == None:
               temp.setNext(self.head)
               self.head = temp
           else:
               temp.setNext(current)
               previous.setNext(temp)       

       def isEmpty(self):
           return self.head == None

       def size(self):
           current = self.head
           count = 0
           while current != None:
               count = count + 1
               current = current.getNext()

           return count


   mylist = OrderedList()
   mylist.add(31)
   mylist.add(77)
   mylist.add(17)
   mylist.add(93)
   mylist.add(26)
   mylist.add(54)

   print(mylist.size())
   print(mylist.search(93))
   print(mylist.search(100))
   
   

Анализ связанных списков
^^^^^^^^^^^^^^^^^^^^^^^^

Чтобы проанализировать сложность операций для связанных списков, нам нужно
выяснить, требуют ли они обход. Рассмотрим связанный список из :math:`n` узлов
Метод ``isEmpty`` имеет :math:`O(1)`, поскольку нужен всего один шаг, чтобы
проверить, ссылается ли ``head`` на ``None``. С другой стороны, ``size``
всегда требует :math:`n` шагов, поскольку не существует способа узнать количество
узлов в связанном списке, не обойдя его от головы до конца. Таким образом,
``size`` имеет :math:`O(n)`. Добавление элемента в неупорядоченный список
всегда будет :math:`O(1)`, ведь мы просто помещаем новый узел в голову
связанного списка. Однако, ``search`` и ``remove``, а так же ``add`` для
упорядоченных списков, требуют процесса обхода. Хотя в среднем им потребуется
обойти только половину списка, все они имеют :math:`O(n)` - исходя из наихудшего
случая с обработкой каждого узла в списке.


Вы также можете заметить, что представление этой реализации отличается от
существующей, даваемой раньше для списков Python. Это предполагает, что там
списки основываются не на связанной модели, а на чём-то ещё. Действительно,
в основе существующей реализация списков в Python лежит понятие массива.
Мы обсудим это более детально в другой главе. 
