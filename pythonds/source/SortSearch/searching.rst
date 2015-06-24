..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Поиск
------

Теперь обратим наше внимание задачи, наиболее часто возникающие при вычислениях: поиск и сортировку. В этом разделе мы изучим первую из них, а ко второй вернёмся в этой главе чуть позже. Поиск - это алгоритмический процесс нахождения конкретного элемента в коллекции. Обычно он даёт результат ``True`` или ``False``, в зависимости от присутствия элемента. Иногда поиск может быть модифицирован, чтобы возвращать найденный элемент. Для наших целей будет достаточно просто решить вопрос наличия искомого.

В Python есть очень простой способ узнать, входит ли данный элемент в список. Для этого используют оператор ``in``::

::

    >>> 15 in [3,5,2,4,1]
    False
    >>> 3 in [3,5,2,4,1]
    True
    >>> 

Хотя это легко написать, для ответа на вопрос должен запуститься скрытый процесс. Оказывается, существует множество различных способов поиска элемента. Нас будет интересовать, как эти алгоритмы работают и соотносятся друг с другом.

.. disqus::
