..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Узлы и ссылки
~~~~~~~~~~~~~

Наш второй способ представления деревьев будет использовать узлы и ссылки. Для этого случая мы определим класс, чьими атрибутами станут корневое значение, левое и правое поддеревья. Поскольку такое представление ближе к объектно-ориентированной парадигме программирования, мы будем развивать его до конца данной главы.

Используя узлы и ссылки, о дереве можно думать, как о структуре, пример которой приведён на :ref:`рисунке 2 <fig_treerec>`.

.. _fig_treerec:

.. figure:: Figures/treerecs.png
   :align: center
   :alt: image

   Figure 2: Вариант простого дерева с использованием узлов и ссылок

Начнём с простого определения класса для варианта с узлами и ссылками (:ref:`листинг 4 <lst_nar>`). Важно помнить, что в этом представлении атрибуты ``left`` и ``right`` являются ссылками на другие сущности класса ``BinaryTree``. Например, когда мы вставляем нового левого потомка в дерево, мы создаём другой объект ``BinaryTree`` и изменяем ``self.leftChild`` корня, чтобы этот атрибут ссылался на новое дерево.

.. _lst_nar:

**Листинг 4**

::

    class BinaryTree:
        def __init__(self,rootObj):
            self.key = rootObj
            self.leftChild = None
            self.rightChild = None

Обратите внимание, что в :ref:`листинге 4 <lst_nar>` конструктор ожидает получить некий вид объекта, чтобы сохранить его в корне. Подобно тому, как вы можете хранить в списке любой объект, коренем дерева может быть любая ссылка. В наших ранних примерах в качестве корневого значения сохранялось имя узла. Используя узлы и ссылки для представления дерева (как это показано на :ref:`рисунке 2 <fig_treerec>`), нам нужно создать шесть сущностей класса ``BinaryTree ``.

Далее давайте рассмотрим функцию, которую требуется написать для строительства дерева за пределы корневого значения. Чтобы добавить левого потомка в дерево, мы создадим новый объект двоичного дерева и установим в его атрибут корня ``left``ссылку новый объект. Код для ``insertLeft`` показан в :ref:`листинге 5 <lst_insl>`.

.. _lst_insl:

**Листинг 5**

.. highlight:: python
    :linenothreshold: 5

::

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:  
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
.. highlight:: python
    :linenothreshold: 500

Нам необходимо рассмотреть два случая вставки. Первый - для узла, у которого нет левого потомка. В этом варианте узел просто вставляется в дерево. Второй вариант характеризуется узлом, имеющим левого потомка. Тогда нам надо вставить новый узел и спустить имеющегося потомка на один уровень ниже. Этот случай управляется оператором ``else`` в строке 4 :ref:`листинга 5 <lst_insl>`.

Код для ``insertRight`` должен содержать симметричный набор случаев. Здесь также может не существовать правого потомка, либо есть необходимость вставить узел между корнем и существующим правым потомком. Код операции вставки показан в :ref:`листинге 6 <lst_insr>`.

.. _lst_insr:

**Листинг 6**

::

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

Завершая наше определение простого двоичного дерева, напишем методы доступа к корню, правому и левому потомкам (см. :ref:`листинг 7 <lst_naracc>`).

.. _lst_naracc:

**Листинг 7**

::

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

Теперь у нас есть всё необходимое для создания и манипулирования двоичным деревом. Давайте используем его, чтобы исследовать структуру немного глубже. Создадим простое дерево с узлом ``a`` в качестве корня и узлами ``b`` и ``c`` в качестве потомков. :ref:`ActiveCode 4 <lst_comptest>` конструирует такое дерево и смотрит, какие значения сохранились в ``key``, ``left`` и ``right``. Обратите внимание, что и левый, и правый потомки корня - различные сущности класса ``BinaryTree``. Как мы уже говорили в нашем оригинальном рекурсивном определении дерева, это позволяет нам работать с любым потомком двоичного дерева, как с самим деревом.

.. _lst_comptest:

.. activecode:: bintree
    :caption: Использование реализации с узлами и ссылками

    class BinaryTree:
        def __init__(self,rootObj):
            self.key = rootObj
            self.leftChild = None
            self.rightChild = None

        def insertLeft(self,newNode):
            if self.leftChild == None:
                self.leftChild = BinaryTree(newNode)
            else:  
                t = BinaryTree(newNode)
                t.leftChild = self.leftChild
                self.leftChild = t

        def insertRight(self,newNode):
            if self.rightChild == None:
                self.rightChild = BinaryTree(newNode)
            else:
                t = BinaryTree(newNode)
                t.rightChild = self.rightChild
                self.rightChild = t


        def getRightChild(self):
            return self.rightChild

        def getLeftChild(self):
            return self.leftChild

        def setRootVal(self,obj):
            self.key = obj

        def getRootVal(self):
            return self.key                


    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())


.. admonition:: Самопроверка

   Напишите функцию ``buildTree``, возвращающую дерево, реализованное через узлы и ссылки, которое выглядело бы следующим образом:

   .. image:: Figures/tree_ex.png

   .. actex:: mctree_3

      from test import testEqual
      
      def buildTree():
          pass

      ttree = buildTree()

      testEqual(ttree.getRightChild().getRootVal(),'c')
      testEqual(ttree.getLeftChild().getRightChild().getRootVal(),'d')
      testEqual(ttree.getRightChild().getLeftChild().getRootVal(),'e')
