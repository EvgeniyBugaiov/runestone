..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Списки
------

В процессе обсуждения основных структур данных мы постоянно использовали
списки Python для реализации представленных абстрактных типов данных.
Списки - мощный, но простой механизм коллекций, дарующий программисту
большое разнообразие операций. Однако, не все языки программирования
имеют списки как встроенные структуры данных. В таких случаях программисту
приходится создавать их вручную.

**Список** - это коллекция элементов, каждый из которых хранится на
соответствующей позиции по отношению к остальным. Точнее, список такого
рода мы будем называть неупорядоченным списком. Можно сделать вывод, что
список имеет первый элемент, второй элемент, третий и так далее. Мы также
можем ссылаться на начало списка (первый элемент) или его конец (последний элемент).
Для простоты будем полагать, что списки не содержат дублирующихся данных.

Например, коллекция целых чисел 54, 26, 93, 17, 77 и 31 может представлять
собой простой неупорядоченный список экзаменационных оценок. Заметьте, что
мы должны записывать их как разделённые запятыми значения - общепринятым
способом изображения структуры списка. Python, естественно, :math:`[54,26,93,17,77,31]`.

