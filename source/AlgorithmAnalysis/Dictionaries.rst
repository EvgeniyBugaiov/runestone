..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Словари
~~~~~~~~~~~~



Второй основной структурой данных в Python является словарь. Как вы,
наверное, помните, словари отличаются от списков тем, что в них вы получаете
доступ к элементу по ключу, а не по позиции. Позднее в этой книге вы увидите
множество способов реализации словаря. Сейчас же наиболее важно отметить, что
операции получения и записи элемента в словарь имеют :math:`O(1)`. Другой важной
операцией со словарями является определение принадлежности ему элемента. Проверка,
есть ли с словаре данный ключ или нет, тоже :math:`O(1)`. Эффективности всех
операций над словарями собраны в :ref:`Таблице 3 <tbl_dictbigo>`. Важное замечание
в сторону относительно производительности словарей: эффективности, которые мы
предоставляем в таблице, - это усреднённая производительность. В редких случаях
принадлежность, получение или запись элемента могут деградировать до :math:`O(n)`.
Мы встретимся с этим в одной из последующих глав, когда будем говорить о различных
способах, которыми можно реализовать словарь.


.. _tbl_dictbigo:

.. table:: **Таблица 3: Эффективность операций над словарями в Python в терминах нотации "большое О"**

    ================== ==================
              операция      эффективность
    ================== ==================
           копирование               O(n)
      получить элемент               O(1)
      записать элемент               O(1)
       удалить элемент               O(1)
        вхождение (in)               O(1)
              итерация               O(n)
    ================== ==================



В нашем последнем эксперименте с производительностью мы сравним эффективность
операций принадлежности у списков и словарей. В процессе мы подтвердим, что
оператор принадлежности для списков имеет :math:`O(n)`, а для словарей -
:math:`O(1)`. Производить сравнение мы будем просто. Мы создадим список с
диапазоном чисел, затем будем брать число случайным образом и смотреть, есть
ли оно в списке. Если наша таблица производительности верна, то чем больше
список, тем дольше будет происходить определение, содержится ли в нём данное
число.


Мы повторим тот же эксперимент со словарём, содержащим числа в качестве ключей.
В этом эксперименте мы хотим увидеть, что определение есть или нет число в словаре
не только намного быстрее, но и время, занимаемое для проверки, остаётся постоянным,
даже если объём словаря возрастает.


:ref:`Листинг 6 <lst_listvdict>` реализовывает это сравнение. Заметьте, что мы
выполняем в точности одинаковые операции ``number in container``. Различие только в
том, что в седьмой строке <code>x</code> - это список, а в девятой - словарь.


.. _lst_listvdict:

**Листинг 6**


.. sourcecode:: python
    :linenos:

    import timeit
    import random

    for i in range(10000,1000001,20000):
        t = timeit.Timer("random.randrange(%d) in x"%i,
                         "from __main__ import random,x")
        x = list(range(i))
        lst_time = t.timeit(number=1000)
        x = {j:None for j in range(i)}
        d_time = t.timeit(number=1000)
        print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
        
        


:ref:`Рисунок 4 <fig_listvdict>` подытоживает результаты запуска
:ref:`Листинге 6 <lst_listvdict>`. Вы видите, что словарь стабильно быстрее.
Для списков малых размеров на 10 000 элементов словарь быстрее в 89,4 раза.
Для больших списков на 990 000 элементов разница становится в 11 603 раза!
Вы также можете видеть, что время, требуемое операции проверки принадлежности
для списка, линейно возрастает с ростом размера списка. Это подтверждает
утверждение, что оператор принадлежности для списков имеет :math:`O(n)`. Так
же хорошо видно, что аналогичная операция для словаря остаётся постоянной даже
при возрастании объёма словаря. Фактически, для словаря размером в 10 000
операция проверки принадлежности занимает 0,004 миллисекунды, как и для словаря
на 990 000 элементов.


.. _fig_listvdict:

.. figure:: Figures/listvdict.png

    Рисунок 4: Сравнение операторов ``in`` для списков и словарей в Python

Поскольку Python - развивающийся язык, то за сценой постоянно происходят
изменения. Последнюю информацию о производительности структур данных в Python можно
найти на сайте Python. На момент написания этих строк Python wiki имеет хорошую
страничку, посвящённую временной сложности. Вы можете ознакомиться с ней
`Time Complexity Wiki <http://wiki.python.org/moin/TimeComplexity>`_




.. admonition:: Самопроверка

    .. mchoicemf:: mcpyperform
       :answer_a: list.pop(0)
       :answer_b: list.pop()
       :answer_c: list.append()
       :answer_d: list[10]
       :answer_e: all of the above are O(1)
       :correct: a
       :feedback_a: When you remove the first element of a list, all the other elements of the list must be shifted forward.
       :feedback_b: Removing an element from the end of the list is a constant operation.
       :feedback_c: Appending to the end of the list is a constant operation
       :feedback_d: Indexing a list is a constant operation
       :feedback_e: There is one operation that requires all other list elements to be moved.

       Какая из перечисленных операций для списков не является O(1)?

    .. mchoicemf:: mcpydictperf
      :answer_a: 'x' in mydict
      :answer_b: del mydict['x']
      :answer_c: mydict['x'] == 10
      :answer_d: mydict['x'] = mydict['x'] + 1
      :answer_e: all of the above are O(1)
      :correct: e
      :feedback_a: in is a constant operation for a dictionary because you do not have to iterate but there is a better answer.
      :feedback_b: deleting an element from a dictionary is a constant operation but there is a better answer.
      :feedback_c: Assignment to a dictionary key is constant but there is a better answer.
      :feedback_d: Re-assignment to a dictionary key is constant but there is a better answer.
      :feedback_e: The only dictionary operations that are not O(1) are those that require iteration.                  

      Какая из перечисленных операций для словарей не является O(1)?

.. video::  pythonopsperf
   :controls:
   :thumb: ../_static/function_intro.png

   http://media.interactivepython.org/pythondsVideos/pythonops.mov
   http://media.interactivepython.org/pythondsVideos/pythonops.webm
