..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Производительность структур данных в Python
-------------------------------------------

Теперь, когда у вас есть общее представление о том, что же такое нотация
"большое О" и в чём заключаются различия между разными функциями, наша цель
в этом разделе - рассказать вам о производительности операций над списками
и словарями в Python. Мы проведём несколько временн*ы*х экспериментов, чтобы
продемонстрировать затраты и выгоды при использовании конкретных операций
каждой из озвученных структур данных. Понимать эффективность этих структур
- очень важно для вас, поскольку они являются строительными блоками,
которые мы будем использовать при реализации других структур данных на
протяжении оставшихся глав этой книги. В этом разделе мы не планируем
объяснять, почему производительность такова, какова она есть. Позднее вы
сами увидите возможные реализации списков и словарей, и как от этого зависит производительность.

.. disqus::
