..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Обзор основ Python
----------------------

В этом разделе мы дадим обзор языка программирования Python и заодно предоставим несколько более детальных примеров идей, сформулированных выше. Если вы новичок в Python или считаете, что вам нужно больше информации по любой из представленных здесь тем, то мы рекомендуем вам получить консультацию на ресурсах `Python Language Reference <http://docs.python.org/3/reference/index.html>`_ или `Python Tutorial <http://docs.python.org/3/tutorial/index.html>`_. Нашей целью в этом разделе будет повторное ознакомление вас с языком, а также углубление понимания некоторых концепций, которые займут центральное место в последующих главах.

Python является современным объектно-ориентированным языком программирования с низким порогом вхождения. Он обладает мощным набором встроенных типов данных и легких в использовании управляющих конструкций. Поскольку Python - интерпретируемый язык программирования, то проще всего знакомиться с ним, рассматривая и описывая интерактивные сессии. Вы должны помнить, что интерпретатор сначала выдаёт распространённое приглашение ввода ``>>>``, а затем вычисляет предоставленную вами Python-конструкцию. Например:

::

    >>> print("Algorithms and Data Structures")
    Algorithms and Data Structures
    >>>


покажет приглашение, функцию ``print``, результат её выполнения и следующее приглашение.
