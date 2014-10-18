..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Сортировка Шелла
~~~~~~~~~~~~~~~~~

**Сортировку Шелла** иногда называют "сортировкой с уменьшением инкремента". Она улучшает сортировку вставками, разбивая первоначальный список на несколько подсписков, каждый из которых сортируется по отдельности. Оригинальный способ выбора таких подсписков - ключевая идея сортировки Шелла. Вместо того, чтобы выделять подсписки из стоящих рядом элементов, сортировка Шелла использует инкремент ``i`` (**приращение**), чтобы создавать подсписки из значений, отстоящих на расстоянии ``i`` друг от друга.

Это можно увидеть на :ref:`рисунке 6 <fig_incrementsA>`. Изображённый на нём список состоит из девяти элементов. Если мы используем тройку в качестве инкремента, то получим три подсписка, каждый из которых можно отсортировать вставками. После завершения этих сортировок мы получим список с :ref:`рисунка 7 <fig_incrementsB>`. Хотя он ещё не отсортирован до конца, случилось нечто весьма интересное. Сортируя эти подсписки, мы переместили элементы ближе друг к другу относительно того, где они были раньше.

.. _fig_incrementsA:

.. figure:: Figures/shellsortA.png
   :align: center


   Рисунок 6: Сортировка Шелла с инкрементом 3


.. _fig_incrementsB:

.. figure:: Figures/shellsortB.png
   :align: center


   Рисунок 7: Сортировка Шелла после сортировки каждого из подсписков


:ref:`Рисунок 8 <fig_incrementsC>` демонстрирует окончательную сортировку вставками с использованием приращения 1 - другими словами, стандартную сортировку вставками. Обратите внимание, что, благодаря проведению предварительных сортировок подсписков, сейчас мы сократили общее число операций смещения, необходимых для расположения элементов списка в правильном порядке. В нашем случа требуется всего четыре сдвига, чтобы завершить процесс.

.. _fig_incrementsC:

.. figure:: Figures/shellsortC.png
   :align: center


   Рисунок 8: Сортировка Шелла: итоговая сортировка вставками с инкрементом 1


.. _fig_incrementsD:

.. figure:: Figures/shellsortD.png
   :align: center


   Рисунок 9: Начальный подсписки для сортировки Шелла


Ранее мы уже говорили, что способ, которым выбирается инкремент, - уникальное свойство сортировки Шелла. Функция, показанная в :ref:`ActiveCode 5 <lst_shell>`, использует различный набор инкрементов. Мы начинаем с :math:`\frac {n}{2}` подсписков. На следующем проходе сортируются :math:`\frac {n}{4}` подсписков. Наконец, единственный список сортируется с помощью базовой сортировки вставками. :ref:`Рисунок 9 <fig_incrementsD>` показывает первые подсписки из нашего примера, использующие этот инкремент.

Следующий вызов функции ``shellSort`` демонстрирует списки, частично отсортированные после каждого приращения, и финальную сортировку с инкрементом 1.

.. _lst_shell:

.. activecode:: lst_shellSort
    :caption: Сортировка Шелла

    def shellSort(alist):
        sublistcount = len(alist)//2
        while sublistcount > 0:

          for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

          print("After increments of size",sublistcount,
                                       "The list is",alist)

          sublistcount = sublistcount // 2

    def gapInsertionSort(alist,start,gap):
        for i in range(start+gap,len(alist),gap):

            currentvalue = alist[i]
            position = i

            while position>=gap and alist[position-gap]>currentvalue:
                alist[position]=alist[position-gap] 
                position = position-gap

            alist[position]=currentvalue
            
    alist = [54,26,93,17,77,31,44,55,20]
    shellSort(alist)
    print(alist)


.. animation:: shell_anim
   :modelfile: sortmodels.js
   :viewerfile: sortviewers.js
   :model: ShellSortModel
   :viewer: BarViewer 

Для большей детализации CodeLens 5 пошагово проведут вас через алгоритм.

.. codelens:: shellSorttrace
    :caption: Трассировка сортировки Шелла

    def shellSort(alist):
        sublistcount = len(alist)//2
        while sublistcount > 0:

          for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

          print("After increments of size",sublistcount,
                                       "The list is",alist)

          sublistcount = sublistcount // 2

    def gapInsertionSort(alist,start,gap):
        for i in range(start+gap,len(alist),gap):

            currentvalue = alist[i]
            position = i

            while position>=gap and alist[position-gap]>currentvalue:
                alist[position]=alist[position-gap] 
                position = position-gap

            alist[position]=currentvalue
            
    alist = [54,26,93,17,77,31,44,55,20]
    shellSort(alist)
    print(alist) 

На первый взгляд может показаться, что сортировка Шелла не лучше предыдущей, поскольку делает полную сортировку вставками на последнем шаге. Однако, получается так, что эта итоговая сортировка не требует большого количества сравнений (или сдвигов), так как список уже был частично отсортирован (как это описано выше). Другими словами, каждый проход делает список "более сортированным" по отношению к предыдущему. Поэтому финальный проход получается таким эффективным.

Хотя общий анализ сортировки Шелла выходит далеко за рамки этого текста, мы можем сказать, что она находится между :math:`O(n)` и :math:`O(n^{2})`, в зависимости от поведения, описанного выше. Для инкрементов, показанных в :ref:`листинге 5 <lst_shell>`, производительность будет :math:`O(n^{2})`. Изменив инкремент (например, на :math:`2^{k}-1` (1, 3, 7, 15, 31 и так далее)) получим производительность сортировки Шелла :math:`O(n^{\frac {3}{2}})`.

.. admonition:: Самопроверка

   .. mchoicemf:: question_sort_4
      :correct: a
      :answer_a: [5, 3, 8, 7, 16, 19, 9, 17, 20, 12]
      :answer_b: [3, 7, 5, 8, 9, 12, 19, 16, 20, 17]
      :answer_c: [3, 5, 7, 8, 9, 12, 16, 17, 19, 20]
      :answer_d: [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
      :feedback_a: Каждая из групп элементов, отстоящих друг от друга на величину 3, отсортирована правильно.
      :feedback_b: Это решение для интервала, равного двум. 
      :feedback_c: Этот список отсортирован полностью, вы перестарались.
      :feedback_d: Значение интервала 3 говорит о том, что в группу входит каждое третье число, т.е. 0, 3, 6, 9  и 1, 4, 7 и 2, 5, 8 отсортированы, но не с интервалом 3.
      :iscode:

      Дан следующий список чисел: [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]. Который из ответов иллюстрирует содержимое списка после всех перестановок для приращения 3?
