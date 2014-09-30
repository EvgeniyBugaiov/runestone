..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Проверка палиндрома
~~~~~~~~~~~~~~~~~~~

Интересная задача, которая может быть легко решена с использованием структуры
данных "дек" - это классическая задача палиндрома. **Палиндромом** называют
строку, которая одинаково читается справа налево и слева направо. Например,
*radar*, *toot* или *madam*. Мы хотим создать алгоритм, принимающий на вход
строку символов и проверяющий, является ли она палиндромом.

Для решения данной задачи мы будем использовать дек в качестве хранилища строковых
символов. Мы будем обрабатывать строку слева направо и добавлять каждый её элемент
в хвост дека. В этот момент он будет работать очень схоже с обычной очередью.
Однако, теперь мы можем использовать дуальную функциональность дека. Его голова
будет хранить первый символ строки, а хвост - последний (see :ref:`Рисунок 2 <fig_palindrome>`).

.. _fig_palindrome:

.. figure:: Figures/palindromesetup.png
   :align: center

   Рисунок 2: Дек


Поскольку мы способны удалять оба элемента сразу, то можно производить
сравнение и продолжать только в случае, если символы совпадают. Если
соответствие первого и последнего элементов будет сохраняться, то в
конечном итоге мы придём или к отсутствию символов, или останемся с деком
размером 1 - в зависимости от того, была ли длина исходной строки чётным
или нечётным числом. Но обоих случаях входная последовательность будет
палиндромом. Полностью функция проверки представлена в :ref:`ActiveCode 1 <lst_palchecker>`.


.. _lst_palchecker:

.. activecode:: palchecker
   :caption: Проверка палиндрома с использованием дека

   from pythonds.basic.deque import Deque
   
   def palchecker(aString):
       chardeque = Deque()

       for ch in aString:
           chardeque.addRear(ch)

       stillEqual = True

       while chardeque.size() > 1 and stillEqual:
           first = chardeque.removeFront()
           last = chardeque.removeRear()
           if first != last:
               stillEqual = False

       return stillEqual

   print(palchecker("lsdkjfskf"))
   print(palchecker("radar"))
