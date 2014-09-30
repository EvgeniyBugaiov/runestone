..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Треугольник Серпинского
------------------------

Ещё один фрактал, обладающий свойством самоподобия, - это треугольник Серпинского. Его пример показан на :ref:`рисунке 3 <fig_sierpinski>`. Треугольник Серпинского иллюстрирует трёхходовой рекурсивный алгоритм. Процедура его отрисовки вручную очень проста. Начинаем с большого треугольника, который делим на четыре маленьких, связанных с серединами сторон первоначального. Игнорируя вновь созданный внутренний треугольник, делаем всё то же самое для каждого из трёх угловых. Каждый раз при создании нового набора треугольников, вы рекурсивно применяете эту процедуру к трём меньшим угловым фигурам. Так можно продолжать до бесконечности (если у вас достаточно острый карандаш). Перед тем, как продолжить чтение, можете попробовать самостоятельно нарисовать треугольник Серпинского, используя описанный метод.


.. _fig_sierpinski:

.. figure:: Figures/sierpinski.png
     :align: center

Рисунок 3: Треугольник Серпинского.

Поскольку мы можем повторять этот алгоритм до бесконечности, что сделать базовым случаем? Им станет произвольное число - сколько раз мы хотим разделить треугольник на части. Иногда это число называют "степенью" фрактала. Каждый раз, когда делается рекурсивный вызов, мы вычитаем из степени единицу, пока она не станет равной нулю. Тогда мы останавливаем рекурсию. Код, генерирующий треугольник Серпинского на :ref:`рисунке 3 <fig_sierpinski>`, показан в :ref:`ActiveCode 4 <lst_st>`.


.. _lst_st:

.. activecode:: lst_st
    :caption:  Рисование треугольника Серпинского

    import turtle

    def drawTriangle(points,color,myTurtle):
        myTurtle.fillcolor(color)
        myTurtle.up()
        myTurtle.goto(points[0][0],points[0][1])
        myTurtle.down()
        myTurtle.begin_fill()
        myTurtle.goto(points[1][0],points[1][1])
        myTurtle.goto(points[2][0],points[2][1])
        myTurtle.goto(points[0][0],points[0][1])
        myTurtle.end_fill()

    def getMid(p1,p2):
        return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def sierpinski(points,degree,myTurtle):
        colormap = ['blue','red','green','white','yellow',
                    'violet','orange']
        drawTriangle(points,colormap[degree],myTurtle)
        if degree > 0:
            sierpinski([points[0],
                            getMid(points[0], points[1]),
                            getMid(points[0], points[2])],
                       degree-1, myTurtle)
            sierpinski([points[1],
                            getMid(points[0], points[1]),
                            getMid(points[1], points[2])],
                       degree-1, myTurtle)
            sierpinski([points[2],
                            getMid(points[2], points[1]),
                            getMid(points[0], points[2])],
                       degree-1, myTurtle)

    def main():
       myTurtle = turtle.Turtle()
       myWin = turtle.Screen()
       myPoints = [[-100,-50],[0,100],[100,-50]]
       sierpinski(myPoints,3,myTurtle)
       myWin.exitonclick()

    main()


Программа из :ref:`ActiveCode 4 <lst_st>` следует изложенным выше идеям. Первое, что делает ``sierpinski``, - это прорисовывает внешний треугольника. Затем идут три рекурсивных вызова, по одному для каждого из новых угловых треугольников, полученных после соединения средних точек сторон. Мы снова используем стандартный модуль Python ``turtle``. Вы можете изучить в подробностях все его методы, воспользовавшись командой ``help('turtle')`` в командной строке Python.

Посмотрите на код и подумайте, в каком порядке будут прорисовываться треугольники. Поскольку точный порядок углов определяется спецификацией начального набора, давайте предположим, что углы идут в следующем порядке: нижний левый, верхний, нижний правый. Поскольку функция ``sierpinski`` вызывает сама себя, вычисление будет идти к наименьшему возможному треугольнику в левом нижнем углу, а затем уже будут заполняться остальные треугольники в обратном порядке. Потом заполнятся треугольники в верхнем углу - к наименьшему и самому верхнему. Наконец, будут заполнен правый нижний угол, опять же по направлению к наименьшему нижнему правому.

Иногда полезно думать о рекурсивных алгоритмах в терминах диаграммы вызовов функции. :ref:`Рисунок 4 <fig_stcalltree>` показывает, что рекурсивные вызовы всегда начинаются слева. Ативная функция выделена чёрным, неактивные вызовы - серым. Чем ниже вы спускаетесь по :ref:`рисунку 4 <fig_stcalltree>`, тем меньше треугольники. Функция заканчивает рисунок одного уровня за один раз; закончив с нижней левой частью, она перемещается к нижней середине и так далее.

.. _fig_stcalltree:

.. figure:: Figures/stCallTree.png
    :align: center 

Рисунок 4: Построение треугольника Серпинского.

Функция ``sierpinski`` сильно зависит от функции ``getMid``. Последняя принимает в качестве аргументов две конечные точки и возвращает точку, находящуюся по середине между ними. В дополнение, :ref:`ActiveCode 4 <lst_st>` содержит функцию раскраски треугольников, использующую методы ``begin_fill`` и ``end_fill`` из модуля ``turtle``. Это означает, что каждая степень треугольника Серпинского рисуется другим цветом.
