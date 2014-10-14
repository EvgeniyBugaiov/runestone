..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Фрейм стека: реализация рекурсии
---------------------------------

Предположим, что вместо объединения результатов рекурсивных вызовов ``toStr`` со строкой из ``convertString``, мы изменим наш алгоритм таким образом, чтобы он складывал строки в стек перед тем, как сделать рекурсивный вызов. Код такого алгоритма показан в :ref:`ActiveCode 6 <lst_recstack>`.

.. _lst_recstack:

.. activecode:: lst_recstack
    :caption: Преобразование целого числа в строку с использованием стека

    from pythonds.basic.stack import Stack

    rStack = Stack()

    def toStr(n,base):
        convertString = "0123456789ABCDEF"
        while n > 0:
            if n < base:
                rStack.push(convertString[n])
            else:
                rStack.push(convertString[n % base])
            n = n // base
        res = ""
        while not rStack.isEmpty():
            res = res + str(rStack.pop())
        return res

    print(toStr(1453,16)) 

Каждый раз, когда вызывается ``toStr``, в стек помещается символ. Возвращаясь к предыдущему примеру, мы можем увидеть, что после четвёртого вызова ``toStr`` стек будет выглядеть, как показано на :ref:`рисунке 5 <fig_recstack>`. Обратите внимание: теперь мы можем просто вытолкнуть символы из стека и объединить их в итоговый результат ``"1010"``.

 .. _fig_recstack:

.. figure:: Figures/recstack.png
   :align: center

    Рисунок 5: Строки, помещённые в стек во время преобразования.

Предыдущий пример даёт нам некоторое представление о том, как в Python реализованы рекурсивные вызовы. При вызове функции для управления её локальными переменными выделяется **фрейм стека**. Возвращаемое значение к моменту окончания работы функции будет лежать на вершине стека, доступное для вызывающей части программы. :ref:`Рисунок 6 <fig_callstack>` иллюстрирует стек после оператора ``return`` в строке 4.

.. _fig_callstack:

.. figure:: Figures/newcallstack.png
   :align: center

    Рисунок 6: Стек вызовов, сгенерированный ``toStr(10, 2)``.


Обратите внимание, что вызов ``toStr(2//2, 2)`` оставляет возвращаемое значение ``"1"`` в стеке. Затем оно подставляется вместо функции ``toStr(1, 2)`` в выражение ``"1" + convertString[2%2]``, которое оставляет на вершине стека ``"10"``. Таким образом, стек вызовов Python работает так же, как и стек, который мы явно использовали в :ref:`листинге 4 <lst_recstack>`. В нашем суммирующем список примере вы можете думать о возвращаемом значении в стеке, как об аккумулирующей переменной.


Также фрейм стека предоставляет область видимости для переменных, используемых функцией. Несмотря на то, что мы вновь и вновь вызываем одну и ту же функцию, каждый вызов создаёт новую область видимости для её локальных переменных.

Если вы хорошо уясните для себя идею стека, то вам будет намного легче писать соответствующие рекурсивные функции.
