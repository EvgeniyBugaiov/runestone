..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Заключение по реализациям АТД ``Map``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

На протяжении двух последних глав мы рассмотрели несколько структур данных, подходящих для реализации АТД ``Map``: бинарный поиск на списках, хэш-таблицы, двоичное дерево поиска и сбалансированное двоичное дерево поиска. В заключение этого раздела, давайте подытожим производительности для каждой из перечисленных структур данных (см. :ref:`таблицу 1 <tab_compare>`).

.. _tab_compare:

.. table:: **Таблица 1: Сравнение производительности различных реализаций Map**

    =========== ======================  ============   =======================  ====================
    Операция    Сортированный список    Хэш-таблица    Бинарное дерево поиска   АВЛ-дерево
    =========== ======================  ============   =======================  ====================
         put    :math:`O(n)`            :math:`O(1)`       :math:`O(n)`         :math:`O(\log_2{n})`   
         get    :math:`O(\log_2{n})`    :math:`O(1)`       :math:`O(n)`         :math:`O(\log_2{n})`   
         in     :math:`O(\log_2{n})`    :math:`O(1)`       :math:`O(n)`         :math:`O(\log_2{n})`   
         del    :math:`O(n))`           :math:`O(1)`       :math:`O(n)`         :math:`O(\log_2{n})`   
    =========== ======================  ============   =======================  ====================
