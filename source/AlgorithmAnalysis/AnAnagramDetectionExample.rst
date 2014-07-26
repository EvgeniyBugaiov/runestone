..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Пример с определением анаграммы
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Хорошим примером для демонстрации алгоритмов с разным порядком величины
является классическая задача для строк - определения анаграммы. Одна
строка является анаграммой другой, если вторая получается простой
перестановкой букв первой. Например, ``'heart'`` и ``'earth'`` - это
анаграммы. Как и строки ``'python'`` и ``'typhon'``. Для простоты будем
полагать, что обе заданные строки одной длины и составлены из набора
символов в 26 букв в нижнем регистре. Нашел целью будет написать булеву
функцию, принимающую две строки и возвращающую ответ - являются ли они
анаграммами?


Решение 1: Метки
^^^^^^^^^^^^^^^^^^^^^^^^

Наше первое решение задачи про анаграмму будет проверять, входит ли
каждый из символов первой строки во вторую. Если все символы будут
"отмечены", то строки являются анаграммами. "Пометка" символа будет
выполняться с помощью замены его на специальное значение Python ``None``.
Однако, поскольку строки в Python иммутабельны, первым шагом обработки будет
конвертирование второй строки в список. Каждый символ из первой строки может
быть сверен с элементами списка и, если будет найден, отмечен оговоренной заменой.
:ref:`ActiveCode 4 <lst_anagramSolution>` демонстрирует эту функцию.


.. _lst_anagramSolution:

.. activecode:: active5
    :caption: Метки

    def anagramSolution1(s1,s2):
        alist = list(s2)

        pos1 = 0
        stillOK = True

        while pos1 < len(s1) and stillOK:
            pos2 = 0
            found = False
            while pos2 < len(alist) and not found:
                if s1[pos1] == alist[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1

            if found:
                alist[pos2] = None
            else:
                stillOK = False

            pos1 = pos1 + 1

        return stillOK

    print(anagramSolution1('abcd','dcba'))

При анализе алгоритма нам стоит отметить, что каждый из *n* символов в
``s1`` вызовет цикл по *n* символам списка, полученного из ``s2``.
Каждая из *n* позиций списка будет посещена единожды, чтобы проверить её
на соответствие ``s1``. Количество таких посещений будет выражено через
сумму целых чисел от 1 до *n*. Ранее мы уже говорили, что это может быть
записано как

.. math::

   \sum_{i=1}^{n} i &= \frac {n(n+1)}{2} \\
                    &= \frac {1}{2}n^{2} + \frac {1}{2}n

С увеличением :math:`n` слагаемое :math:`n^{2}` начнёт доминировать,
так что :math:`n` и :math:`\frac {1}{2}` можно проигнорировать.
Таким образом, решение является :math:`O(n^{2})`


Решение 2: Сортируй и сравнивай
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Следующие решение задачи про анаграммы будет использовать тот факт, что
даже если ``s1`` и ``s2`` различны, они будут анаграммами только если
состоят из одинаковых символов. Следовательно, если мы отсортируем каждую
строку в алфавитном порядке от ``a`` до ``z``, то в итоге получим одинаковые
строки (если, конечно, ``s1`` и ``s2`` - анаграммы). Это решение показано
в :ref:`ActiveCode 5 <lst_ana2>`. Опять же, в Python мы можем использовать
встроенный метод ``sort``, для списков, полученных в начале функции конвертацией
каждой строки.

.. _lst_ana2:

.. activecode:: active6
    :caption: Сортируй и сравнивай

    def anagramSolution2(s1,s2):
        alist1 = list(s1)
        alist2 = list(s2)

        alist1.sort()
        alist2.sort()

        pos = 0
        matches = True

        while pos < len(s1) and matches:
            if alist1[pos]==alist2[pos]:
                pos = pos + 1
            else:
                matches = False

        return matches

    print(anagramSolution2('abcde','edcba'))

В первый момент вы можете подумать, что этот алгоритм имеет :math:`O(n)`,
поскольку у него есть всего одна простая итерация для сравнения *n* символов
после сортировки. Однако, два вызова Python-метода ``sort`` не проходят
даром. Как мы увидим в следующих главах, сортировка обычно имеет
:math:`O(n^{2})` или :math:`O(n\log n)`, так что эта операция доминирует над
циклом. В итоге алгоритм будет иметь тот же порядок операций, что и
сортировочные вычисления.


Решение 3: Полный перебор
^^^^^^^^^^^^^^^^^^^^^^^

Техника **полного перебора** для решения задач обычно используется, когда
все другие возможности уже исчерпаны. Для задачи определения анаграммы мы
можем просто сгенерировать список всех возможных строк из символов ``s1``
и посмотреть, входит ли в него ``s2``. Но в данном подходе есть одна
закавырка: при генерации всех возможных строк из ``s1`` есть *n* возможных
первых символов, :math:`n-1` возможных вторых символов и так далее. Отсюда
общее количество строк-кандидатов будет :math:`n*(n-1)*(n-2)*...*3*2*1`,
что есть :math:`n!`. Несмотря на то, что некоторые строки будут дублироваться,
программа об этом заранее знать не будет, поэтому всё равно сгенерирует
:math:`n!` различных строк.

Решение :math:`n!` с увеличением *n* возрастает быстрее, чем даже
:math:`2^{n}`. Фактически, при длине ``s1`` в 20 символов мы получим
:math:`20!=2,432,902,008,176,640,000` возможных строк-кандидатов. Если мы
будем обрабатывать одну вероятность каждую секунду, то на весь список уйдёт
77 146 816 596 лет. Похоже, это совсем не хорошее решение.


Решение 4: Подсчитывай и сравнивай
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Наше последнее решения задачи про анаграммы воспользуется преимуществом
того факта, что любые две анаграммы имеют одинаковое количество букв *a*,
*b* и так далее. Для того, чтобы решить, являются ли строки анаграммами,
мы сначала подсчитаем, сколько раз в них встречается каждый символ.
Поскольку возможных букв 26, то мы можем использовать список из 26
счётчиков - по одному на каждый символ. Каждый раз, когда мы видим конкретную
букву, мы увеличиваем соответствующий ей счётчик на единицу. В итоге, если
оба списка счётчиков идентичны, то строки - анаграммы. Это решение показано
в :ref:`ActiveCode 6 <lst_ana4>`


.. _lst_ana4:

.. activecode:: active7
    :caption: Подсчитывай и сравнивай

    def anagramSolution4(s1,s2):
        c1 = [0]*26
        c2 = [0]*26

        for i in range(len(s1)):
            pos = ord(s1[i])-ord('a')
            c1[pos] = c1[pos] + 1

        for i in range(len(s2)):
            pos = ord(s2[i])-ord('a')
            c2[pos] = c2[pos] + 1

        j = 0
        stillOK = True
        while j<26 and stillOK:
            if c1[j]==c2[j]:
                j = j + 1
            else:
                stillOK = False

        return stillOK

    print(anagramSolution4('apple','pleap'))



Решение вновь имеет некоторое количество циклов. Однако, в отличии от
первого варианта, ни один из них не является вложенным. Два первых цикла,
используемые для подсчёта символов, базируются на *n*.
Третий цикл - сравнение двух списков счётчиков - всегда состоит из 26
итераций (поскольку строки состоят из 26 возможных элементов). Складывая
всё вместе, получим :math:`T(n)=2n+26` шагов, что является :math:`O(n)`.
Мы нашли алгоритм с линейным порядком величины для решения нашей задачи.

До того, как закончить с этим примером, стоит сказать несколько слов о
пространственных требованиях. Хотя последнее решение и работает за линейное
время, оно достигает этого путём использования дополнительных хранилищ для
двух списков счётчиков. Другими словами, этот алгоритм приносит в жертву
пространство, чтобы выиграть время.

Это очень распространённый случай. Очень часто вам придётся делать выбор
между временем и пространством. В данном случае объём места был не существенен.
Однако, если основополагающий алфавит имеет миллионы символов, то это вызовет
больше беспокойства. Как у учёных-информатиков, при выборе алгоритма только от
вас будет зависеть определение наилучшего использования вычислительных ресурсов,
выделенных под конкретную задачу.

.. admonition:: Самопроверка

   .. mchoicemf:: analysis_1
       :answer_a: O(n)
       :answer_b: O(n^2)
       :answer_c: O(log n)
       :answer_d: O(n^3)
       :correct: b
       :feedback_a: In an example like this you want to count the nested loops. especially the loops that are dependent on the same variable, in this case, n.
       :feedback_b: A singly nested loop like this is O(n^2)
       :feedback_c: log n typically is indicated when the problem is iteratvely made smaller
       :feedback_d: In an example like this you want to count the nested loops. especially the loops that are dependent on the same variable, in this case, n.

       Given the following code fragment, what is its Big-O running time?

       .. code-block:: python

         test = 0
         for i in range(n):
            for j in range(n):
               test = test + i * j

   .. mchoicemf:: analysis_2
       :answer_a: O(n)
       :answer_b: O(n^2)
       :answer_c: O(log n)
       :answer_d: O(n^3)
       :correct: a
       :feedback_b: Be careful, in counting loops you want to make sure the loops are nested.
       :feedback_d: Be careful, in counting loops you want to make sure the loops are nested.
       :feedback_c: log n typically is indicated when the problem is iteratvely made smaller
       :feedback_a: Even though there are two loops they are not nested.  You might think of this as O(2n) but we can ignore the constant 2.

       Given the following code fragment what is its Big-O running time?

       .. code-block:: python

         test = 0
         for i in range(n):
            test = test + 1

         for j in range(n):
            test = test - 1

   .. mchoicemf:: analysis_3
       :answer_a: O(n)
       :answer_b: O(n^2)
       :answer_c: O(log n)
       :answer_d: O(n^3)
       :correct: c
       :feedback_a: Look carefully at the loop variable i.  Notice that the value of i is cut in half each time through the loop.  This is a big hint that the performance is better than O(n)
       :feedback_b: Check again, is this a nested loop?
       :feedback_d: Check again, is this a nested loop?       
       :feedback_c: The value of i is cut in half each time through the loop so it will only take log n iterations.

       Given the following code fragment what is its Big-O running time?

       .. code-block:: python

         i = n
         while i > 0:
            k = 2 + 2
            i = i // 2
