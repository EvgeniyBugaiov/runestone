..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Список смежности
~~~~~~~~~~~~~~~~

Более пространственно-экономичным способом реализации разреженного графа является использование списка смежности. В таком представлении мы храним основной список из всех вершин объекта ``Graph``, каждый из элементов которого поддерживает перечень из связанных с ним вершин. В нашей реализации класса ``Vertex`` в качестве последнего будет использоваться словарь, где ключами станут вершины, а значениями - веса. :ref:`Рисунок 4 <fig_adjlist>` иллюстрирует представление графа с :ref:`рисунка 2 <fig_dgsimple>` в виде списка смежности.

.. _fig_adjlist:

.. figure:: Figures/adjlist.png
   :align: center

   Рисунок 4: Представление графа в виде списка смежности.

Преимуществом такой реализации является то, что она позволяет нам компактно представлять разреженные графы. Также в списке смежности легко найти все ссылки, непосредственно связанные с конкретной вершиной.

.. disqus::
