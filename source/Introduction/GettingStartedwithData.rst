..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Приступая к работе с данными
~~~~~~~~~~~~~~~~~~~~~~~~~

Выше мы уже отмечали, что Python поддерживает парадигму объектно-ориентированного программирования. Это означает, что в фокус процесса решения задачи Python ставит данные. В Python, как и в любом другом объектно-ориентированном языке программирования, мы определяем **класс**, являющийся описанием того, как, собственно, выглядят данные (состояние) и что они могут делать (поведение). Классы аналогичны абстрактным типам данных, поскольку пользователь класса видит только состояние и поведение единицы данных. Такие единицы в объектно-ориентированной парадигме называются **объектами**. Объект является экземпляром класса.

Встроенные элементарные типы данных
^^^^^^^^^^^^^^^^^^^^^^^^^^

Начнём наш обзор с рассмотрения элементарных типов данных. У Python есть два основных встроенных числовых класса, реализующих типы для целых чисел и чисел с плавающей запятой. Они называются ``int`` и ``float``. Стандартные арифметические операции +, -, *, / и ** (возведение в степень) могут использоваться со скобками, задающими порядок операций, отличный от обусловленного обычным приоритетом операторов. Другими полезными операциями являются оператор остатка целочисленного деления % и собственно целочисленного деления //. Обратите внимание, что при делении двух целых чисел результат - число с плавающей запятой. Оператор целочисленного деления возвращает целую часть частного путём отсечения от неё дробной части.


.. activecode:: intro_1
    :caption: Основные арифметические операторы

    print 2+3*4
    print (2+3)*4
    print 2**10
    print 6/3
    print 7/3
    print 7//3
    print 7%3
    print 3/6
    print 3//6
    print 3%6
    print 2**100

Логический тип данных, реализованный в Python как класс ``bool``, будет весьма полезен для представления значений истинности. Возможными значениями для логического объекта являются ``True`` и ``False`` со стандартными булевыми операторами ``and``, ``or`` и ``not``.


::

    >>> True
    True
    >>> False
    False
    >>> False or True
    True
    >>> not (False or True)
    False
    >>> True and True
    True

Объекты булева типа данных также используются в качестве результатов операций сравнения, таких как "равно" (==) и "больше, чем" (:math:`>`). Кроме того, операторы отношений и логических операций могут быть скомбинированы вместе в форме сложных логических вопросов. В :ref:`Таблице 1 <tab_relational>` показаны операторы отношений и логические операторы вместе с примерами их использования.


.. _tab_relational:

.. table:: **Таблица 1: Логические операторы и операторы отношений**

    =========================== ============== =================================================================
             **Название**        **Оператор**                                                       **Описание**
    =========================== ============== =================================================================
                      меньше      :math:`<`                                                Оператор "меньше"
                      больше      :math:`>`                                                Оператор "больше"
              меньше или равно    :math:`<=`                                     Оператор "меньше или равно"
              больше или равно    :math:`>=`                                     Оператор "больше или равно"
                         равно    :math:`==`                                              Оператор равенства
                      не равно    :math:`!=`                                            Оператор неравенства
                логическое "и"    :math:`and`            Если оба операнда истинны, то результат тоже истина
              логическое "или"    :math:`or`    Если хотя бы один из операндов истина, то результат - истина
               логическое "не"    :math:`not`         Инвертирует значение: False становится True и наоборот
    =========================== ============== =================================================================


.. activecode:: intro_2
    :caption: Basic Relational and Logical Operators

    print(5==10)
    print(10 > 5)
    print((5 >= 1) and (5 <= 10))

В качестве имён в языках программирования используются идентификаторы. В Python они начинаются с буквы или подчёркивания (_), чувствительны к регистру и могут быть произвольной длины. Не забывайте о том, что давать имена, отражающие смысл переменной, - всегда здравая идея, делающая ваш код более простым для чтения и понимания.

В Python переменная создаётся при первом использовании имени с левой стороны от оператора присваивания. Присваивание предоставляет возможность ассоциировать имя со значением. Переменная будет содержать ссылку на кусочек данных, а не сами данные. Рассмотрим следующий код:


::

    >>> theSum = 0
    >>> theSum
    0
    >>> theSum = theSum + 1
    >>> theSum
    1
    >>> theSum = True
    >>> theSum
    True

Присваивание ``theSum = 0`` создаёт переменную с именем ``theSum``, содержащую ссылку на объект данных ``0`` (см. :ref:`Рисунок 3 <fig_assignment1>`). В целом, когда правая часть оператора присваивания вычисляется, ссылка на результат "назначается" имени в левой части. В данный момент в нашем примере тип переменной - целое, и это тип данных, на которые сейчас ссылается ``theSum``. Если он изменится (см. :ref:`Рисунок 4 <fig_assignment2>`), как показано выше, на булево значение ``True``, то изменится и тип переменной (сейчас ``theSum`` имеет тип ``bool``). Оператор присваивания меняет ссылки, хранящиеся в переменной. Это динамическая характеристика Python. Одна и та же переменная может ссылаться на различные типы данных.


.. _fig_assignment1:

.. figure:: Figures/assignment1.png
   :align: center

   Рисунок 3: Переменная содержит ссылку на объект данных

.. _fig_assignment2:

.. figure:: Figures/assignment2.png
   :align: center

   Рисунок 4: Присваивание изменяет ссылку

Built-in Collection Data Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to the numeric and boolean classes, Python has a number of
very powerful built-in collection classes. Lists, strings, and tuples
are ordered collections that are very similar in general structure but
have specific differences that must be understood for them to be used
properly. Sets and dictionaries are unordered collections.

A **list** is an ordered collection of zero or more references to Python
data objects. Lists are written as comma-delimited values enclosed in
square brackets. The empty list is simply ``[ ]``. Lists are
heterogeneous, meaning that the data objects need not all be from the
same class and the collection can be assigned to a variable as below.
The following fragment shows a variety of Python data objects in a list.

::

    >>> [1,3,True,6.5]
    [1, 3, True, 6.5]
    >>> myList = [1,3,True,6.5]
    >>> myList
    [1, 3, True, 6.5]

Note that when Python evaluates a list, the list itself is returned.
However, in order to remember the list for later processing, its
reference needs to be assigned to a variable.

Since lists are considered to be sequentially ordered, they support a
number of operations that can be applied to any Python sequence.
:ref:`Table 2 <tab_sequence>` reviews these operations and the following session
gives examples of their use.

.. _tab_sequence:

.. table:: **Table 2: Operations on Any Sequence in Python**

    =========================== ============== ========================================
             **Operation Name**   **Operator**                          **Explanation**
    =========================== ============== ========================================
                       indexing            [ ]          Access an element of a sequence
                  concatenation             \+          Combine sequences together
                     repetition             \*   Concatenate a repeated number of times
                     membership             in     Ask whether an item is in a sequence
                         length            len  Ask the number of items in the sequence
                        slicing          [ : ]             Extract a part of a sequence
    =========================== ============== ========================================


Note that the indices for lists (sequences) start counting with 0. The
slice operation, myList[1:3], returns a list of items starting with the
item indexed by 1 up to but not including the item indexed by 3.

Sometimes, you will want to initialize a list. This can quickly be
accomplished by using repetition. For example,

::

    >>> myList = [0] * 6
    >>> myList
    [0, 0, 0, 0, 0, 0]

One very important aside relating to the repetition operator is that the
result is a repetition of references to the data objects in the
sequence. This can best be seen by considering the following session:

.. activecode:: intro_3
    :caption: Repetition of References

    myList = [1,2,3,4]
    A = [myList]*3
    print(A)
    myList[2]=45
    print(A)


The variable ``A`` holds a collection of three references to the
original list called ``myList``. Note that a change to one element of
``myList`` shows up in all three occurrences in ``A``.

Lists support a number of methods that will be used to build data
structures. :ref:`Table 3 <tab_listmethods>` provides a summary. Examples of their
use follow.

.. _tab_listmethods:

.. table:: **Table 3: Methods Provided by Lists in Python**

    ======================== ========================== =======================================================
             **Method Name**                    **Use**                                         **Explanation**
    ======================== ========================== =======================================================
                  ``append``     ``alist.append(item)``                    Adds a new item to the end of a list
                  ``insert``   ``alist.insert(i,item)``           Inserts an item at the ith position in a list
                     ``pop``            ``alist.pop()``             Removes and returns the last item in a list
                     ``pop``           ``alist.pop(i)``              Removes and returns the ith item in a list
                    ``sort``           ``alist.sort()``                            Modifies a list to be sorted
                 ``reverse``        ``alist.reverse()``                  Modifies a list to be in reverse order
                     ``del``           ``del alist[i]``                    Deletes the item in the ith position
                   ``index``      ``alist.index(item)``   Returns the index of the first occurrence of ``item``
                   ``count``      ``alist.count(item)``           Returns the number of occurrences of ``item``
                  ``remove``     ``alist.remove(item)``                Removes the first occurrence of ``item``
    ======================== ========================== =======================================================


.. activecode:: intro_5
    :caption: Examples of List Methods

    myList = [1024, 3, True, 6.5]
    myList.append(False)
    print(myList)
    myList.insert(2,4.5)
    print(myList)
    print(myList.pop())
    print(myList)
    print(myList.pop(1))
    print(myList)
    myList.pop(2)
    print(myList)
    myList.sort()
    print(myList)
    myList.reverse()
    print(myList)
    print(myList.count(6.5))
    print(myList.index(4.5))
    myList.remove(6.5)
    print(myList)
    del myList[0]
    print(myList)


You can see that some of the methods, such as ``pop``, return a value
and also modify the list. Others, such as ``reverse``, simply modify the
list with no return value. ``pop`` will default to the end of the list
but can also remove and return a specific item. The index range starting
from 0 is again used for these methods. You should also notice the
familiar “dot” notation for asking an object to invoke a method.
``myList.append(False)`` can be read as “ask the object ``myList`` to
perform its ``append`` method and send it the value ``False``.” Even
simple data objects such as integers can invoke methods in this way.

::

    >>> (54).__add__(21)
    75
    >>>

In this fragment we are asking the integer object ``54`` to execute its
``add`` method (called ``__add__`` in Python) and passing it ``21`` as
the value to add. The result is the sum, ``75``. Of course, we usually
write this as ``54+21``. We will say much more about these methods later
in this section.

One common Python function that is often discussed in conjunction with
lists is the ``range`` function. ``range`` produces a range object that
represents a sequence of values. By using the ``list`` function, it is
possible to see the value of the range object as a list. This is
illustrated below.

::

    >>> range(10)
    range(0, 10)
    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> range(5,10)
    range(5, 10)
    >>> list(range(5,10))
    [5, 6, 7, 8, 9]
    >>> list(range(5,10,2))
    [5, 7, 9]
    >>> list(range(10,1,-1))
    [10, 9, 8, 7, 6, 5, 4, 3, 2]
    >>>

The range object represents a sequence of integers. By default, it will
start with 0. If you provide more parameters, it will start and end at
particular points and can even skip items. In our first example,
``range(10)``, the sequence starts with 0 and goes up to but does not
include 10. In our second example, ``range(5,10)`` starts at 5 and goes
up to but not including 10. ``range(5,10,2)`` performs similarly but
skips by twos (again, 10 is not included).

**Strings** are sequential collections of zero or more letters, numbers
and other symbols. We call these letters, numbers and other symbols
*characters*. Literal string values are differentiated from identifiers
by using quotation marks (either single or double).

::

    >>> "David"
    'David'
    >>> myName = "David"
    >>> myName[3]
    'i'
    >>> myName*2
    'DavidDavid'
    >>> len(myName)
    5
    >>>

Since strings are sequences, all of the sequence operations described
above work as you would expect. In addition, strings have a number of
methods, some of which are shown in :ref:`Table 4<tab_stringmethods>`. For example,

::

    >>> myName
    'David'
    >>> myName.upper()
    'DAVID'
    >>> myName.center(10)
    '  David   '
    >>> myName.find('v')
    2
    >>> myName.split('v')
    ['Da', 'id']

Of these, ``split`` will be very useful for processing data. ``split``
will take a string and return a list of strings using the split
character as a division point. In the example, ``v`` is the division
point. If no division is specified, the split method looks for
whitespace characters such as tab, newline and space.

.. _tab_stringmethods:

.. table:: **Table 4: Methods Provided by Strings in Python**

    ======================== ========================= =============================================================
             **Method Name**                   **Use**                                               **Explanation**
    ======================== ========================= =============================================================
                  ``center``     ``astring.center(w)``            Returns a string centered in a field of size ``w``
                   ``count``   ``astring.count(item)``   Returns the number of occurrences of ``item`` in the string
                   ``ljust``      ``astring.ljust(w)``      Returns a string left-justified in a field of size ``w``
                   ``lower``       ``astring.lower()``                             Returns a string in all lowercase
                   ``rjust``      ``astring.rjust(w)``     Returns a string right-justified in a field of size ``w``
                    ``find``    ``astring.find(item)``         Returns the index of the first occurrence of ``item``
                   ``split``  ``astring.split(schar)``                  Splits a string into substrings at ``schar``
    ======================== ========================= =============================================================


A major difference between lists and strings is that lists can be
modified while strings cannot. This is referred to as **mutability**.
Lists are mutable; strings are immutable. For example, you can change an
item in a list by using indexing and assignment. With a string that
change is not allowed.

::

    >>> myList
    [1, 3, True, 6.5]
    >>> myList[0]=2**10
    >>> myList
    [1024, 3, True, 6.5]
    >>>
    >>> myName
    'David'
    >>> myName[0]='X'

    Traceback (most recent call last):
      File "<pyshell#84>", line 1, in -toplevel-
        myName[0]='X'
    TypeError: object doesn't support item assignment
    >>>

Tuples are very similar to lists in that they are heterogeneous
sequences of data. The difference is that a tuple is immutable, like a
string. A tuple cannot be changed. Tuples are written as comma-delimited
values enclosed in parentheses. As sequences, they can use any operation
described above. For example,

::

    >>> myTuple = (2,True,4.96)
    >>> myTuple
    (2, True, 4.96)
    >>> len(myTuple)
    3
    >>> myTuple[0]
    2
    >>> myTuple * 3
    (2, True, 4.96, 2, True, 4.96, 2, True, 4.96)
    >>> myTuple[0:2]
    (2, True)
    >>>

However, if you try to change an item in a tuple, you will get an error.
Note that the error message provides location and reason for the
problem.

::

    >>> myTuple[1]=False

    Traceback (most recent call last):
      File "<pyshell#137>", line 1, in -toplevel-
        myTuple[1]=False
    TypeError: object doesn't support item assignment
    >>>

A set is an unordered collection of zero or more immutable Python data
objects. Sets do not allow duplicates and are written as comma-delimited
values enclosed in curly braces. The empty set is represented by
``set()``. Sets are heterogeneous, and the collection can be assigned to
a variable as below.

::

    >>> {3,6,"cat",4.5,False}
    {False, 4.5, 3, 6, 'cat'}
    >>> mySet = {3,6,"cat",4.5,False}
    >>> mySet
    {False, 4.5, 3, 6, 'cat'}
    >>>

Even though sets are not considered to be sequential, they do support a
few of the familiar operations presented earlier. :ref:`Table 5 <tab_setops>` reviews
these operations and the following session gives examples of their use.

.. _tab_setops:

.. table:: **Table 5: Operations on a Set in Python**

    =========================== ===================== ===================================================================
             **Operation Name**          **Operator**                                                     **Explanation**
    =========================== ===================== ===================================================================
                     membership                    in                                                      Set membership
                         length                   len                                  Returns the cardinality of the set
                          ``|``   ``aset | otherset``                  Returns a new set with all elements from both sets
                          ``&``   ``aset & otherset``      Returns a new set with only those elements common to both sets
                          ``-``   ``aset - otherset``   Returns a new set with all items from the first set not in second
                         ``<=``  ``aset <= otherset``       Asks whether all elements of  the first set are in the second
    =========================== ===================== ===================================================================


::

    >>> mySet
    {False, 4.5, 3, 6, 'cat'}
    >>> len(mySet)
    5
    >>> False in mySet
    True
    >>> "dog" in mySet
    False
    >>>

Sets support a number of methods that should be familiar to those who
have worked with them in a mathematics setting. :ref:`Table 6 <tab_setmethods>`
provides a summary. Examples of their use follow. Note that ``union``,
``intersection``, ``issubset``, and ``difference`` all have operators
that can be used as well.

.. _tab_setmethods:

.. table:: **Table 6: Methods Provided by Sets in Python**

    ======================== ================================= ================================================================
             **Method Name**                           **Use**                                                  **Explanation**
    ======================== ================================= ================================================================
                   ``union``          ``aset.union(otherset)``               Returns a new set with all elements from both sets
            ``intersection``   ``aset.intersection(otherset)``   Returns a new set with only those elements common to both sets
              ``difference``     ``aset.difference(otherset)``    Returns a new set with all items from first set not in second
                ``issubset``       ``aset.issubset(otherset)``            Asks whether all elements of one set are in the other
                     ``add``                ``aset.add(item)``                                             Adds item to the set
                  ``remove``             ``aset.remove(item)``                                        Removes item from the set
                     ``pop``                    ``aset.pop()``                        Removes an arbitrary element from the set
                   ``clear``                  ``aset.clear()``                                Removes all elements from the set
    ======================== ================================= ================================================================


::

    >>> mySet
    {False, 4.5, 3, 6, 'cat'}
    >>> yourSet = {99,3,100}
    >>> mySet.union(yourSet)
    {False, 4.5, 3, 100, 6, 'cat', 99}
    >>> mySet | yourSet
    {False, 4.5, 3, 100, 6, 'cat', 99}
    >>> mySet.intersection(yourSet)
    {3}
    >>> mySet & yourSet
    {3}
    >>> mySet.difference(yourSet)
    {False, 4.5, 6, 'cat'}
    >>> mySet - yourSet
    {False, 4.5, 6, 'cat'}
    >>> {3,100}.issubset(yourSet)
    True
    >>> {3,100}<=yourSet
    True
    >>> mySet.add("house")
    >>> mySet
    {False, 4.5, 3, 6, 'house', 'cat'}
    >>> mySet.remove(4.5)
    >>> mySet
    {False, 3, 6, 'house', 'cat'}
    >>> mySet.pop()
    False
    >>> mySet
    {3, 6, 'house', 'cat'}
    >>> mySet.clear()
    >>> mySet
    set()
    >>>

Our final Python collection is an unordered structure called a
**dictionary**. Dictionaries are collections of associated pairs of
items where each pair consists of a key and a value. This key-value pair
is typically written as key:value. Dictionaries are written as
comma-delimited key:value pairs enclosed in curly braces. For example,

::

    >>> capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
    >>> capitals
    {'Wisconsin': 'Madison', 'Iowa': 'DesMoines'}
    >>>

We can manipulate a dictionary by accessing a value via its key or by
adding another key-value pair. The syntax for access looks much like a
sequence access except that instead of using the index of the item we
use the key value. To add a new value is similar.

.. activecode:: intro_7
    :caption: Using a Dictionary

    capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
    print(capitals['Iowa'])
    capitals['Utah']='SaltLakeCity'
    print(capitals)
    capitals['California']='Sacramento'
    print(len(capitals))
    for k in capitals:
       print(capitals[k]," is the capital of ", k)

It is important to note that the dictionary is maintained in no
particular order with respect to the keys. The first pair added
(``'Utah':`` ``'SaltLakeCity'``) was placed first in the dictionary and
the second pair added (``'California':`` ``'Sacramento'``) was placed
last. The placement of a key is dependent on the idea of “hashing,”
which will be explained in more detail in Chapter 4. We also show the
length function performing the same role as with previous collections.

Dictionaries have both methods and operators. :ref:`Table 7 <tab_dictopers>` and
:ref:`Table 8 <tab_dictmethods>` describe them, and the session shows them in action. The
``keys``, ``values``, and ``items`` methods all return objects that
contain the values of interest. You can use the ``list`` function to
convert them to lists. You will also see that there are two variations
on the ``get`` method. If the key is not present in the dictionary,
``get`` will return ``None``. However, a second, optional parameter can
specify a return value instead.

.. _tab_dictopers:

.. table:: **Table 7: Operators Provided by Dictionaries in Python**

    ===================== ================== =====================================================================
             **Operator**            **Use**                                                       **Explanation**
    ===================== ================== =====================================================================
                   ``[]``      ``myDict[k]``       Returns the value associated with ``k``, otherwise its an error
                   ``in``   ``key in adict``   Returns ``True`` if key is in the   dictionary, ``False`` otherwise
                  ``del`` del ``adict[key]``                                Removes the entry from the  dictionary
    ===================== ================== =====================================================================



::

    >>> phoneext={'david':1410,'brad':1137}
    >>> phoneext
    {'brad': 1137, 'david': 1410}
    >>> phoneext.keys()
    dict_keys(['brad', 'david'])
    >>> list(phoneext.keys())
    ['brad', 'david']
    >>> phoneext.values()
    dict_values([1137, 1410])
    >>> list(phoneext.values())
    [1137, 1410]
    >>> phoneext.items()
    dict_items([('brad', 1137), ('david', 1410)])
    >>> list(phoneext.items())
    [('brad', 1137), ('david', 1410)]
    >>> phoneext.get("kent")
    >>> phoneext.get("kent","NO ENTRY")
    'NO ENTRY'
    >>>

.. _tab_dictmethods:

.. table:: **Table 8: Methods Provided by Dictionaries in Python**

    ======================== ==================== ===============================================================
             **Method Name**              **Use**                                                 **Explanation**
    ======================== ==================== ===============================================================
                    ``keys``     ``adict.keys()``       Returns the keys of the dictionary in a dict_keys object
                  ``values``   ``adict.values()``   Returns the values of the dictionary in a dict_values object
                   ``items``    ``adict.items()``             Returns the key-value pairs in a dict_items object
                     ``get``     ``adict.get(k)``     Returns the value associated with ``k``, ``None`` otherwise
                     ``get`` ``adict.get(k,alt)``      Returns the value associated with ``k``, ``alt`` otherwise
    ======================== ==================== ===============================================================


.. note::

    This workspace is provided for your convenience.  You can use this activecode window to try out anything you like.

    .. activecode:: scratch_01_01


