..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Быстрая сортировка
~~~~~~~~~~~~~~~~~~~

**Быстрая сортировка** использует технику "разделяй и властвуй", чтобы получить те же преимущества, что и сортировка слиянием, но при этом не использовать дополнительное место. Однако, ценой за это станет то, что список может не поделиться пополам, приводя к уменьшению производительности.

Сначала быстрая сортировка выбирает значение, которое называется **опорным элементом**. Несмотря на то, что есть много способов выбрать его, мы будем просто использовать первое значение в списке. Роль опорного элемента заключается в помощи при разбиении списка. Позиция, на которой он окажется в итоговом сортированном списке, обычно называемая **точкой разбиения**, будет использоваться для разделения списка при последующих вызовах быстрой сортировки.

:ref:`Рисунок 12 <fig_splitvalue>` показывает, как 54 выступает в роли первого опорного значения. Поскольку мы уже рассматривали этот пример несколько раз, то знаем, что 54 в итоге окажется на позиции, занятой сейчас 31. Далее происходит процесс **разделения**. Он находит точку разделения и одновременно перемещает элементы по соответствующим сторонам списка, в зависимости от того, больше они или меньше опорной величины.

.. _fig_splitvalue:


.. figure:: Figures/firstsplit.png
   :align: center

    Рисунок 12: Первая опорная величина для быстрой сортировки

Разбиение начинается с определения двух маркеров положения - назовём их ``leftmark`` и ``rightmark`` - в начале и в конце оставшихся элементов списка (позиции 1 и 8 на :ref:`рисунке 13 <fig_partitionA>`). Целью процесса разбиения является перемещать элементы, лежащие по неправильным сторонам от опорного, пока они не сойдутся в точке разделения. :ref:`Рисунок 13 <fig_partitionA>` показывает этот процесс, когда мы находимся на позиции 54-го элемента.

.. _fig_partitionA:

.. figure:: Figures/partitionA.png
   :align: center

    Рисунок 13: Поиск точки разделения для 54

Мы начинаем с увеличения на единицу ``leftmark``, пока не находим значение, большее опорного. Тогда мы уменьшаем на единицу ``rightmark``, пока не находим значение, меньшее опорного. В этот момент мы имеем два элемента, находящихся на своих местах относительно итоговой точки разбиения. В нашем примере таковыми являются 93 и 20. Теперь можно поменять их местами и повторить процесс заново.

Когда ``rightmark`` становится меньше ``leftmark``, мы останавливаемся. Позиция ``rightmark`` в данный момент - точка разбиения. Опорное значение следует поменять местами с её содержимым, и тогда оно будет стоять на своём месте (:ref:`рисунок 14 <fig_partitionB>`). В дополнение, все элементы слева от точки разбиения теперь меньше опорного значения, а справа - больше. Список поделен на две части, и быстрая сортировка может быть рекурсивно применена к каждой из них.

.. _fig_partitionB:

.. figure:: Figures/partitionB.png
   :align: center

    Рисунок 14: Завершение процесса с целью поиска точки разбиения для 54

Функция ``quickSort``, показанная в :ref:`CodeLens 7 <lst_quick>`, вызывает другую рекурсивную функцию - ``quickSortHelper``. Она начинает рабоать с базового случая, аналогичного сортировке слиянием. Если длина списка меньше или равна единице, то он уже отсортирован. Если больше, то он может быть разделен и рекурсивно отсортирован. Функция ``partition`` воплощает описанный ранее процесс.

.. _lst_quick:

.. activecode:: lst_quick
    :caption: Быстрая сортировка

    def quickSort(alist):
       quickSortHelper(alist,0,len(alist)-1)

    def quickSortHelper(alist,first,last):
       if first<last:

           splitpoint = partition(alist,first,last)

           quickSortHelper(alist,first,splitpoint-1)
           quickSortHelper(alist,splitpoint+1,last)


    def partition(alist,first,last):
       pivotvalue = alist[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and \
                   alist[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while alist[rightmark] >= pivotvalue and \
                   rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = alist[leftmark]
               alist[leftmark] = alist[rightmark]
               alist[rightmark] = temp

       temp = alist[first]
       alist[first] = alist[rightmark]
       alist[rightmark] = temp


       return rightmark

    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist)



.. animation:: quick_anim
   :modelfile: sortmodels.js
   :viewerfile: sortviewers.js
   :model: QuickSortModel
   :viewer: BarViewer 

Для большей детализации, CodeLens 7 помогут вам пошагово пройти весь алгоритм.

.. codelens:: quicktrace
    :caption: Трассировка быстрой сортировки

    def quickSort(alist):
       quickSortHelper(alist,0,len(alist)-1)

    def quickSortHelper(alist,first,last):
       if first<last:

           splitpoint = partition(alist,first,last)

           quickSortHelper(alist,first,splitpoint-1)
           quickSortHelper(alist,splitpoint+1,last)


    def partition(alist,first,last):
       pivotvalue = alist[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and \
                   alist[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while alist[rightmark] >= pivotvalue and \
                   rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = alist[leftmark]
               alist[leftmark] = alist[rightmark]
               alist[rightmark] = temp

       temp = alist[first]
       alist[first] = alist[rightmark]
       alist[rightmark] = temp


       return rightmark

    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist) 

Для анализа функции ``quickSort`` стоит отметить, что для списка длиной *n*, если деление приходится на его середину, мы вновь получим :math:`\log n` разделений. С целью найти точку разбиения, каждый из *n* элементов нуждается в сравнении с опорным значением. Результатом станет :math:`n\log n`. При этом не требуется дополнительной памяти, как в сортировке слиянием.

К сожалению, в наихудшем случае точка разбиения может быть не по середине, а скакать слева направо, делая разделение очень неравномерным. В этом случае сортировка списка из *n* элементов разделится на сортировку списков размером 0 и :math:`n-1` элементов. Далее сортировка списка длиной :math:`n-1` опять даст подсписки из 0 и :math:`n-2` элементов, и так далее. Результат: :math:`O(n^{2})` со всеми накладными расходами, требуемыми для рекурсии.

Ранее мы упоминали, что есть несколько способов выбора опорного значения. В частности, мы можем попытаться сгладить потенциальный дисбаланс в разбиении с помощью метода, называемого **медианой трёх**. Чтобы выбрать опорное значение, мы рассматриваем первый, средний и последний элементы списка. В нашем примере это будут 54, 77 и 20. Теперь определим из них медиану - 54 в данном случае - и используем её в качестве опоры (естественно, это было опорное значение, которое мы использовали первоначально). Идея в том, что когда первый элемент списка не принадлежит его середине, медиана трёх станет лучшим "срединным" значением. Особенно это полезно, если первоначальный список уже подвергался частичной сортировке. Мы вам оставляем реализацию такого выбора опорного значения в качестве упражнения.

.. admonition:: Самопроверка

   .. mchoicemf:: question_sort_7
      :correct: d
      :answer_a: [9, 3, 10, 13, 12]
      :answer_b: [9, 3, 10, 13, 12, 14]
      :answer_c: [9, 3, 10, 13, 12, 14, 17, 16, 15, 19]
      :answer_d: [9, 3, 10, 13, 12, 14, 19, 16, 15, 17]
      :feedback_a: Важно помнить, что быстрая сортировка работает со списком целиком, и сортирует его "по месту".
      :feedback_b: Помните, что быстрая сортировка работает со списком целиком, и сортирует его "по месту".
      :feedback_c: Первое разбиение работает со списком целиком, второе - с полученной левой (не правой) частью.
      :feedback_d: Первое разбиение работает со списком целиком, второе - с полученной левой частью.

      Какой из ответов показывает содержимое списка после второго разбиения с помощью алгоритма быстрой сортировки для следующего списка чисел [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]?

   .. mchoicemf:: question_sort_8
       :correct: b
       :answer_a: 1
       :answer_b: 9
       :answer_c: 16
       :answer_d: 19
       :feedback_a: Три числа, из которых выбирается опорное значение, - это 1, 9, 19.  1 - не медиана и будет в принципе плохим опорным значением, потому как является наименьшим элементом.
       :feedback_b:  Отлично!
       :feedback_c: Хотя 16 - медиана для 1, 16, 19, середина списка - len(list) // 2.
       :feedback_d: Три числа, используемые для выбора опорного значения -это 1, 9, 19.  9 - медиана.  19 будет плохим выбором, потому что это - наибольшее значение.

        Для следующего списка чисел [1, 20, 11, 5, 2, 9, 16, 14, 13, 19] каким будет первый опорный элемент при использовании метода "медиана трёх"?

   .. mchoicema:: question_sort_9
       :answer_a: Shell Sort
       :answer_b: Quick Sort
       :answer_c: Merge Sort
       :answer_d: Insertion Sort
       :correct: c
       :feedback_a: Сортировка Шелла порядка ``n^1.5``
       :feedback_b: Быстрая сортировка может иметь O(n log n), но если опорная величина выбрана плохо, то она O(n^2).
       :feedback_c: Сортировка слия нием единственная гарантирует O(n log n) даже в наихудшем случае.  Цена этого - использование дополнительного объёма памяти.
       :feedback_d: Сортировка вставками имеет ``O(n^2)``.

        Какие из следующих алгоритмов сортировки гарантированно имеют *O(n log n)* даже для наихудшего случая?
