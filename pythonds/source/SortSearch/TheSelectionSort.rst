..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Сортировка выбором
~~~~~~~~~~~~~~~~~~~

**Сортировка выбором** улучшает пузырьковую сортировку, совершая всего один обмен
за каждый проход по списку. Чтобы сделать это, она ищет наибольший элемент и
помещает его на соответствующую позицию. Как и для пузырьковой сортировки, после
первого прохода самый большой элемент находится на правильном месте. После
второго - на своё место становится следующий наибольший элемент. Процесс
продолжается, требуя :math:`n-1` проход для сортировки :math:`n` элементов,
поскольку последний из них автоматически оказывается на своём месте.

:ref:`Рисунок 3 <fig_selectionsort>` демонстрирует сортировочный процесс целиком.
На каждом проходе выбирается наибольший из несортированных элементов и помещается
на соответствующюю позицию. Первый проход разместит 93, второй - 77, третий - 55
и так далее. Функция показана в :ref:`ActiveCode 3 <lst_selectionsortcode>`.

.. _fig_selectionsort:

.. figure:: Figures/selectionsortnew.png
   :align: center


   Рисунок 3: ``selectionSort``


.. activecode:: lst_selectionsortcode
    :caption: Сортировка выбором

    def selectionSort(alist):
       for fillslot in range(len(alist)-1,0,-1):
           positionOfMax=0
           for location in range(1,fillslot+1):
               if alist[location]>alist[positionOfMax]:
                   positionOfMax = location

           temp = alist[fillslot]
           alist[fillslot] = alist[positionOfMax]
           alist[positionOfMax] = temp

    alist = [54,26,93,17,77,31,44,55,20]
    selectionSort(alist)
    print(alist)

.. animation:: selection_anim
   :modelfile: sortmodels.js
   :viewerfile: sortviewers.js
   :model: SelectionSortModel
   :viewer: BarViewer
 
Для большей детализации CodeLens 3 позволит вам пройти весь алгоритм пошагово.

.. codelens:: selectionsortcodetrace
    :caption: Трассировка сортировки выбором

    def selectionSort(alist):
       for fillslot in range(len(alist)-1,0,-1):
           positionOfMax=0
           for location in range(1,fillslot+1):
               if alist[location]>alist[positionOfMax]:
                   positionOfMax = location

           temp = alist[fillslot]
           alist[fillslot] = alist[positionOfMax]
           alist[positionOfMax] = temp

    alist = [54,26,93,17,77,31,44,55,20]
    selectionSort(alist)
    print(alist) 

Вы можете видеть, что сортировка выбором совершает то же число сравнений, что и
пузырьковая сортировка, поэтому является :math:`O(n^{2})`. Однако, из-за
уменьшения количества перестановок, на тестовых заданиях она обычно выполняется
быстрее. Фактически, для нашего списка пузырьковая сортировка сделает 20
перестановок, в то время как сортировка выбором - всего 8.



.. admonition::  Самопроверка

   .. mchoicemf:: question_sort_2
      :correct: d
      :answer_a: [7, 11, 12, 1, 6, 14, 8, 18, 19, 20]
      :answer_b: [7, 11, 12, 14, 19, 1, 6, 18, 8, 20]
      :answer_c: [11, 7, 12, 13, 1, 6, 8, 18, 19, 20]
      :answer_d: [11, 7, 12, 14, 8, 1, 6, 18, 19, 20]
      :feedback_a: Сортировка выбором аналогична пузырьковой (с которой вы уже
                   должны были разобраться), но использует меньшее количество
                   перестановок.
      :feedback_b: Это больше похоже на сортировку вставками.
      :feedback_c: Это очень похоже на правильный ответ, но вместо перестановки
                   числа сдвигались влево, чтобы освободить место для правильных
                   значений.
      :feedback_d: Сортировка выбором улучшает пузырьковую, делая меньшее число
                   перестановок.

      Предположим, у вас есть следующий список для сортировки:
      [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]. Который из представленных вариантов
      является частично отсортированным списком после трёх проходов сортировки
      выбором?

.. disqus::
