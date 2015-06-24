..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Заключение
-----------

- Последовательный поиск имеет :math:`O(n)` для упорядоченных и неупорядоченных списков.

- Бинарный поиск для упорядоченных списков в худшем случае имеет :math:`O(\log n)`.

- Хэш-таблицы могут предоставлять константное время поиска.

- Пузырькова сортировка, сортировка выбором и сортировка вставками - :math:`O(n^{2})` алгоритмы.

- Сортировка Шелла улучшает сортировку вставками путём дополнительной сортировки подсписков. Её производительность колеблется между :math:`O(n)` и :math:`O(n^{2})`.

- Сортировка слиянием имеет :math:`O(n \log n)`, но требует дополнительного объёма памяти.

- Быстрая сортировка имеет :math:`O(n \log n)`, но может деградировать до :math:`O(n^{2})`, если точка разбиения не находится вблизи середины списка. Не требует дополнительного объёма памяти.

.. disqus::
