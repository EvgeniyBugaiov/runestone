..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Двоичные деревья поиска
------------------------

Мы уже видели два различных способа получить коллекцию из пар ключ-значение. Напомним, что её воплощает абстрактный тип данных **map**. Мы обсуждали две его реализации: с помощью списка и хэш-таблицы. В этом разделе мы изучим **двоичные деревья поиска**, как ещё один способ отображать ключ на значение. В этом случае нам не интересно точное расположение элементов в дереве, мы больше заинтересованы в использовании структуры двоичного дерева для эффективного поиска.

