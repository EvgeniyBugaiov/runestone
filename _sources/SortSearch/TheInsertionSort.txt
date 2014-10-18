..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Сортировка вставками
~~~~~~~~~~~~~~~~~~~~~

**Сортировка вставками**, имея по-прежнему :math:`O(n^{2})`, работает несколько иначе. Она всегда поддерживает в сортированном виде подсписок на нижних индексах списка. Каждый новый элемент "вставляется" в упорядоченный на прошлой итерации подсписок так, чтобы тот остался сортированным и стал на один элемент больше. :ref:`Рисунок 4 <fig_insertionsort>`  демонстрирует процесс сортировки вставками. Затенённые элементы представляют собой упорядоченные подсписки, которые алгоритм создаёт на каждом проходе.

.. _fig_insertionsort:

.. figure:: Figures/insertionsort.png
   :align: center


   Рисунок 4: ``insertionSort``


Начнём с предположения, что список из одного элемента (под номером 0) уже отсортирован. На каждом проходе, для каждого элемента с первого по :math:`n-1`, текущий элемент сравнивается с уже отсортированными. Поскольку мы просматриваем отсортированный подсписок в обратном порядке, то сдвигаем большие элементы вправо. При обнаружении меньшего элемента или конца подсписка текущий элемент вставляется на соответствующую позицию.

На :ref:`рисунке 5 <fig_insertionpass>` детально показан пятый проход. В этой точке алгоритма сортированный список из пяти элементов содержит 17, 26, 54, 77 и 93. Мы хотим вставить в него 31. Первое сравнение с 93 приводит к тому, что 93 сдвигается вправо. Так же сдвигаются 77 и 54. Когда мы наталкиваемся на элемент 26, процесс смещения прекращается, и 31 становится на свободное место. Теперь у нас есть отсортированный список из шести элементов.

.. _fig_insertionpass:

.. figure:: Figures/insertionpass.png
   :align: center


   Рисунок 5: ``insertionSort``: пятый проход сортировки


Реализация ``insertionSort`` (:ref:`ActiveCode 4 <lst_insertion>`) демонстрирует, что вновь выполняется :math:`n-1` проход для сортировки :math:`n` элементов. Итерации начинаются с индекса 1 и движутся до :math:`n-1` позиции, поскольку все эти элементы должны быть вставлены в отсортированный список. В строке 8 происходит операция сдвига, которая перемещает значение на одну позицию вверх по списку, создавая место для вставки. Помните, что полноценный обмен, как в предыдущих алгоритмах, здесь не происходит.

Максимальное количество сравнений для сортировки вставками равно сумме первых :math:`n-1` целых. Т.е. снова :math:`O(n^{2})`. Однако, в наилучшем случае на каждом проходе потребуется всего одно сравнение. Это произойдёт, когда список уже отсортирован.

Важное замечание о противопоставлении сдвига и обмена: в общем операция сдвига требует приблизительно трети от вычислительной работы обмена, поскольку делается всего одно присваивание. В контрольных исследованиях сортировка вставками имеет очень хорошую производительность.

.. _lst_insertion:

.. activecode:: lst_insertion
    :caption: Сортировка вставками

    def insertionSort(alist):
       for index in range(1,len(alist)):

         currentvalue = alist[index]
         position = index

         while position>0 and alist[position-1]>currentvalue:
             alist[position]=alist[position-1]
             position = position-1

         alist[position]=currentvalue

    alist = [54,26,93,17,77,31,44,55,20]
    insertionSort(alist)
    print(alist)

.. animation:: insertion_anim
   :modelfile: sortmodels.js
   :viewerfile: sortviewers.js
   :model: InsertionSortModel
   :viewer: BarViewer

Для большей детализации, CodeLens 4 позволят вам пошагово пройти весь алгоритм.

.. codelens:: insertionsortcodetrace
    :caption: Трассировка сортировки вставками

    def insertionSort(alist):
       for index in range(1,len(alist)):

         currentvalue = alist[index]
         position = index

         while position>0 and alist[position-1]>currentvalue:
             alist[position]=alist[position-1]
             position = position-1

         alist[position]=currentvalue

    alist = [54,26,93,17,77,31,44,55,20]
    insertionSort(alist)
    print(alist) 

.. admonition:: Самопроверка

   .. mchoicemf:: question_sort_3
      :correct: c
      :answer_a: [4, 5, 12, 15, 14, 10, 8, 18, 19, 20]
      :answer_b: [15, 5, 4, 10, 12, 8, 14, 18, 19, 20]
      :answer_c: [4, 5, 15, 18, 12, 19, 14, 10, 8, 20]
      :answer_d: [15, 5, 4, 18, 12, 19, 14, 8, 10, 20]
      :feedback_a: Это пузырьковая сортировка.
      :feedback_b: Это результат сортировки выбором.
      :feedback_c: Сортировка вставками работает от начала спска. Каждый проход удлинняет отсортированный список.
      :feedback_d: Сортировка вставками работает от начала, а не от конца списка.

      Предположим, у вас есть следующий список чисел для сортировки: [15, 5, 4, 18, 12, 19, 14, 10, 8, 20] Какой из вариантов ниже соответствует частично отсортированному списку после третьего прохода сортировки вставками?
