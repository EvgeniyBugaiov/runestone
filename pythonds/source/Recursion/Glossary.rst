..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Глоссарий
-----------------

.. glossary::

    базовый случай
        Ветка условного оператора рекурсивной функции, которая не делает следующий рекурсивный вызов.

    бесконечная рекурсия
        Рекурсивная функция, которая вызывает сама себя и никогда не достигает базового случая. В итоге это приводит к возникновению ошибки времени выполнения.

    рекурсия
        Процесс вызова функции, которая уже выполняется.

    рекурсивный вызов
        Опреатор, вызывающий уже выполняющуюся функцию.  Рекурсия может быть ненаправленной --- функция `f` может вызывать `g`, которая вызывает `h`, а `h`, в свою очередь, вызывает `f`.

    рекурсивное определение
        Определение, описывающее нечто в терминах самого себя. Чтобы быть пригодным к использованию, должно включать нерекурсивный *базовый случай*. В этом его отличие от *кругового определения*. Рекурсивные определния часто предоставляют элегантный способ выражения сложных структур данных.
