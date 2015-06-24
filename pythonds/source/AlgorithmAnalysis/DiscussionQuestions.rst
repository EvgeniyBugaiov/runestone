..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Вопросы для обсуждения
----------------------

#. Какова производительность следующего фрагмента кода в терминах нотации "большое О"?

   ::

       for i in range(n):
          for j in range(n):
             k = 2 + 2

#. Какова производительность следующего фрагмента кода в терминах нотации "большое О"?

   ::

       for i in range(n):
            k = 2 + 2

#. Какова производительность следующего фрагмента кода в терминах нотации "большое О"?

   ::

       i = n
       while i > 0:
          k = 2 + 2
          i = i // 2

#. Какова производительность следующего фрагмента кода в терминах нотации "большое О"?

   ::

       for i in range(n):
          for j in range(n):
             for k in range(n):
                k = 2 + 2

#. Какова производительность следующего фрагмента кода в терминах нотации "большое О"?

   ::

       i = n
       while i > 0:
          k = 2 + 2
          i = i // 2

#. Какова производительность следующего фрагмента кода в терминах нотации "большое О"?

   ::

       for i in range(n):
          k = 2 + 2
       for j in range(n):
          k = 2 + 2
       for k in range(n):
          k = 2 + 2

.. disqus::
