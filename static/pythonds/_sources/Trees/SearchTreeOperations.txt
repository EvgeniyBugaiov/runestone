..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Операции для дерева поиска
--------------------------

Перед тем, как рассмотреть реализацию, давайте освежим в памяти интерфейс, предоставляемый АТД ``map``. Вы можете заметить, что он очень похож на словарь Python.

-  ``Map()`` Создаёт новое пустое отображение.

-  ``put(key,val)`` Добавляет в отображение новую пару ключ-значение. Если ключ уже существует, то заменяет старое значение новым.

-  ``get(key)`` По заданному ключу возвращает значение, хранящееся в отображении, или ``None``, если такого ключа не существует.

-  ``del`` Удаляет пару ключ-значение из отображения, используя оператор вида ``del map[key]``.

-  ``len()`` Возвращает количество пар ключ-значение, хранящихся в отображении.

-  ``in`` Возвращает ``True`` для оператора вида ``key in map``, если заданный ключ присутствует в отображении.
