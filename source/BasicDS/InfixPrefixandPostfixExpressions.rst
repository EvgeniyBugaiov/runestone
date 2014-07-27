..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Инфиксные, префиксные и постфиксные выражения
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Когда вы записываете арифметическое выражение вроде B \* C, то его форма
предоставляет вам достаточно информации для корректной интерпретации. В
данном случае мы знаем, что переменная B умножается на переменную C,
поскольку оператор умножения \* находится в выражении между ними. Такой
тип записи называется **инфиксной**, поскольку оператор расположен *между*
(*in between*) двух операндов, с которыми он работает.

Рассмотрим другой инфиксный пример: A + B \* C. Операторы + и \* по-прежнему
располагаются между операндами, но тут уже есть проблема. С какими операндами
они будут работать? + работает с A и B или \* принимает B и C? Выражение
выглядит неоднозначно.

Фактически, вы можете читать и писать выражения такого типа долгое время,
и они не будут вызывать у вас вопросов. Причина в том, что вы кое-что знаете
о + и \*. Каждый оператор имеет свой **приоритет**. Операторы с высоким
приоритетом используются прежде операторов с низким. Единственной вещью,
которая может изменить порядок приоритетов, являются скобки. Для
арифметических операций умножение и деление стоят выше сложения и вычитания.
Если появляются два оператора одинакового приоритета, то используются порядок
слева направо или их ассоциативность.

Давайте интерпретируем вызвавшее затруднение выражение A + B \* C, используя
приоритет операторов. B и C перемножаются первыми, затем к результату
добавляется A. (A + B) \* C заставит выполнить сложение A и B перед умножением.
В выражении A + B + C по очерёдности (через ассоциативность) первым будет
вычисляться самый левый +.

Хотя это и может быть очевидным для вас, помните, что компьютер нуждается в
точном знании того, как и в какой последовательности вычисляются операторы.
Одним из способов записи выражения, гарантирующим, что не возникнет путаницы
по отношению к порядку операций, является создание того, что называется
выражением **с полностью расставленными скобками**. Такой тип выражения
использует пару скобок для каждого оператора. Скобки диктуют порядок операций,
так что здесь не возникает многозначности. Так же отпадает необходимость
помнить правила расстановки приоритетов.

Выражение A + B \* C может быть переписано как ((A + (B \* C)) + D) с целью
показать, что умножение происходит в первую очередь, а затем следует крайнее
левое сложение. A + B + C + D перепишется в (((A + B) + C) + D), поскольку
операции сложения ассоциируются слева направо.

Существует ещё два очень важных формата выражений, которые на первый взгляд
могут показаться вам неочевидными. Рассмотрим инфиксную запись A + B. Что
произойдёт, если мы поместим оператор перед двумя операндами? Результирующее
выражение будет  + A B. Также мы можем переместить оператор в конец, получив
A B +. Всё это выглядит несколько странным.

Эти изменения позиции оператора по отношению к операндам создают два новых
формата - **префиксный** и **постфиксный**. Префиксная запись выражения требует,
чтобы все операторы предшествовали двум операндам, с которыми они работают.
Постфиксная, в свою очередь, требует, чтобы операторы шли после соответствующих
операндов. Несколько дополнительных примеров помогут прояснить этот момент
(см. :ref:`Таблицу 2 <tbl_example1>`).

A + B \* C можно переписать как + A \* B C в префиксной нотации. Оператор умножения
ставится непосредственно перед операндами B и C, указывая на приоритет \* над +.
Затем следует оператор сложения перед A и результатом умножения.

В постфиксной записи выражение выглядит как A B C \* +. Порядок операций вновь
сохраняется, поскольку \* находится непосредственно после B и C, обозначая, что
он имеет приоритет выше следующего +. Хотя операторы перемещаются и теперь
находятся до или после соответствующих операндов, порядок последних по отношению
друг к другу остаётся в точности таким, как был.

.. _tbl_example1:

.. table:: **Таблица 2: Примеры инфиксной, префиксной и постфиксной записи**

    ============================ ======================= ========================
            **Инфиксная запись**   **Префиксная запись**   **Постфиксная запись**
    ============================ ======================= ========================
                           A + B                  \+ A B                    A B +
                      A + B \* C             \+ A \* B C               A B C \* +
    ============================ ======================= ========================


А сейчас рассмотрим инфиксное выражение (A + B) \* C. Напомним, что в
этом случае запись требует наличия скобок для указания выполнить сложение
перед умножением. Однако, когда A + B записывается в префиксной форме, то
оператор сложения просто помещается перед операндами:  + A B. Результат
этой операции является первым операндом для умножения. Оператор умножения
перемещается в начало всего выражения, давая нам \* + A B C. Аналогично, в
постфиксной записи A B + явно указывается, что первым происходит сложение.
Умножение может быть выполнено для получившегося результата и оставшегося
операнда C. Соответствующим постфиксным выражением будет A B + C \*.


Рассмотрим эти три выражения ещё раз (см. :ref:`Таблицу 3 <tbl_parexample>`).
Происходит что-то очень важное. Куда ушли скобки? Почему они не нужны нам в
префиксной и постфиксной записи? Ответ в том, что операторы больше не являются
неоднозначными по отношению к своим операндам. Только инфиксная запись требует
дополнительных символов. Порядок операций внутри префиксного и постфиксного
выражений полностью определён позицией операторов и ничем иным. Во многом именно
это делает инфиксную запись наименее желательной нотацией для использования.

.. _tbl_parexample:

.. table:: **Таблица 3: Выражение со скобками**

    ============================ ========================== ==========================
       **Инфиксное выражение**    **Префиксное выражение**   **Постфиксное выражение**
    ============================ ========================== ==========================
                    (A + B) \* C              \* + A B C               A B + C \*
    ============================ ========================== ==========================


:ref:`Таблица 4 <tbl_example3>` демонстрирует некоторые дополнительные примеры
инфиксных выражений и эквивалентных им префиксных и постфиксных записей.
Убедитесь, что вы понимаете, почему они эквивалентны с точки зрения порядка
выполнения операций.


.. _tbl_example3:

.. table:: **Таблица 4: Дополнительные примеры инфиксной, префиксной и постфиксной записи**

    ============================ ========================== ===========================
       **Инфиксное выражение**    **Префиксное выражение**   **Постфиксное выражение**
    ============================ ========================== ===========================
                  A + B \* C + D        \+ \+ A \* B C D           A B C \* + D +
              (A + B) \* (C + D)          \* + A B + C D           A B + C D + \*
                 A \* B + C \* D        \+ \* A B \* C D          A B \* C D \* +
                   A + B + C + D          \+ + + A B C D            A B + C + D +
    ============================ ========================== ===========================


Преобразование инфиксного выражения в префиксное и постфиксное
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

До сих пор мы использовали специальные методы для преобразования между
инфиксными выражениями и эквивалентными им префиксной и постфикской
записями. Как вы можете ожидать, существуют алгоритмические способы
выполнения таких преобразований, позволяющие корректно трансформировать
любое выражение любой сложности.

Первой из рассматриваемых нами техник будет использование идеи полной
расстановки скобок в выражении, рассмотренной нами ранее. Напомним, что
A + B \* C можно записать как (A + (B \* C)), чтобы явно показать приоритет
умножения перед сложением. Однако, при более близком рассмотрении вы увидите,
что каждая пара скобок также отмечает начало и конец пары операндов с
соответствующим оператором по середине.

Взгляните на правую скобку в подвыражении (B \* C) выше. Если мы передвинем
символ умножения с его позиции и удалим соответствующую левую скобку, получив
B C \*, то полученный эффект конвертирует подвыражение в постфиксную нотацию.
Если оператор сложения тоже передвинуть к соответствующей правой скобке и удалить
связанную с ним левую скобку, то результатом станет полное постфиксное выражение
(см. :ref:`Изображение 6 <fig_moveright>`).</p>

.. _fig_moveright:

.. figure:: Figures/moveright.png
   :align: center

   Рисунок 6: Перемещение операторов вправо для постфиксной записи

Если мы сделаем тоже самое, но вместо передвижения символа на позицию к правой
скобке, сдвинем его к левой, то получим префиксную нотацию
(см. :ref:`Рисунок 7 <fig_moveleft>`). Позиция пары скобок на самом деле является
ключом к окончательной позиции заключённого между ними оператора.

.. _fig_moveleft:

.. figure:: Figures/moveleft.png
   :align: center

   Рисунок 7: Перемещение операторов влево для префиксной записи.


Таким образом, с целью преобразования выражения (неважно, насколько сложного) в
префиксную или постфиксную запись, для установления порядка выполнения операций
используется полная расстановка скобок. Затем передвигайте находящийся внутри
них оператор на крайнюю левую или крайнюю правую позицию - в зависимости от
того, префиксную или постфиксную запись вы хотите получить.

Вот более сложное выражение: (A + B) \* C - (D - E) \* (F + G).
:ref:`Рисунок 8 <fig_complexmove>` демонстрирует его преобразование в постфиксный
и префиксный виды.

.. _fig_complexmove:

.. figure:: Figures/complexmove.png
   :align: center

   Рисунок 8: Преобразование сложного выражения к префиксной и постфиксной записи.

Обобщённое преобразование из инфиксного в постфиксный вид
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Нам необходимо разработать алгоритм преобразования любого инфиксного выражения
в постфиксное. Для этого посмотрим ближе на сам процесс конвертирования.

Рассмотрим ещё раз выражение A + B \* C. Как было показано выше, его постфиксным
эквивалентом является A B C \* +. Мы уже отмечали, что операнды A, B и C остаются
на своих местах, а местоположение меняют только операторы. Ещё раз взглянем на
операторы в инфиксном выражении. Первым при проходе слева направо нам попадётся +.
Однако, в постфиксном выражении + находится в конце, так как следующий оператор,
\*, имеет приоритет над сложением. Порядок операторов в первоначальном выражении
обратен результирующему постфиксному выражению.

В процессе обработки выражения операторы должны где-то храниться, пока не найден
их соответствующий правый операнд. Также порядок этих сохраняемых операторов может
быть обратным (из-за их приоритета). Это случай со сложением и умножением в данном
примере. Поскольку оператор сложения, появляющийся перед оператором умножения, имеет
более низкий приоритет, то он должен появиться после использования оператора умножения.
Из-за такого обратного порядка имеет смысл рассмотреть использование стека для хранения
операторов до тех пор, пока они не понадобятся.

Что насчёт (A + B) \* C? Напомним, что его постфиксный эквивалент A B + C \*.
Повторимся, что обрабатывая это инфиксное выражение слева направо, первым мы
встретим +. В этом случае, когда мы увидим \*, + уже будет помещён в результирующее
выражение, поскольку имеет преимущество над \* в силу использования скобок. Теперь
можно начать рассматривать, как будет работать алгоритм преобразования. Когда мы
видим левую скобку, мы сохраняем её как знак, что должен будет появиться другой
оператор с высоким приоритетом. Он будет ожидать, пока не появится соответствующая
правая скобка, чтобы отметить его местоположение (вспомните технику полной расстановки
скобок). После появления правой скобки оператор выталкивается из стека.

Поскольку мы сканируем инфиксное выражение слева направо, то будем использовать
стек для хранения операторов. Это предоставит нам обратный порядок, который мы
отмечали в первом примере. На вершине стека всегда будет последний сохранённый
оператор. Когда бы мы не прочитали новый оператор, мы должны сравнить его по
приоритету с операторами в стеке (если таковые имеются).

Предположим, что инфиксное выражение есть строка токенов, разделённых пробелами.
Токенами операторов являются \*, /, + и - вместе с правой и левой скобками, ( и ).
Токены операндов - это однобуквенные идентификаторы A, B, C и так далее.
Следующая последовательность шагов даст строку токенов в постфиксном порядке.

#. Создать пустой стек с названием ``opstack`` для хранения операторов.
   Создать пустой список для вывода.

#. Преобразовать инфиксную строку в список, используя строковый метод
   ``split``.

#. Сканировать список токенов слева направо.

   -  Если токен является операндом, то добавить его в конец выходного
      списка.

   -  Если токен является левой скобкой, положить его в ``opstack``.

   -  Если токен является правой скобкой, то выталкивать элементы из
      ``opstack`` пока не будет найдена соответствующая левая скобка.
      Каждый оператор добавлять в конец выходного списка.

   -  Если токен является оператором \*, /, + или -, поместить его в
      ``opstack``. Однако, перед этим удалить любой из операторов, уже
      находящихся в ``opstack``, который имеет больший или равный
      приоритет, и добавить его в выходной список.

#. Когда входное выражение будет полностью обработано, проверить ``opstack``.
Любые операторы, всё ещё находящиеся в нём, следует удалить и добавить в конец
результирующего списка.

:ref:`Рисунок 9 <fig_intopost>` демонстрирует алгоритм преобразования, работающий
над выражением A \* B + C \* D. Заметьте, что первый оператор \* удаляется до того,
как мы встречаем оператор +. Также + остаётся в стеке, когда появляется второй \*,
поскольку умножение имеет приоритет перед сложением. В конце инфиксного выражения
из стека дважды происходит выталкивание, удаляя оба оператора и помещая + как
последний элемент в результирующее постфиксное выражение.

.. _fig_intopost:

.. figure:: Figures/intopost.png
   :align: center

   Рисунок 9: Преобразование A \* B + C \* D в постфиксную запись

Для того, чтобы закодировать алгоритм на Python, мы будем использовать словарь под
именем ``prec`` для хранения значений приоритета операторов. Он связывает каждый
оператор с целым числом, которые можно сравнивать с другими операторами как уровень
приоритетности (мы произвольно выбрали для этого целые числа 3, 2 и 1). Левая скобка
получит самое низкое значение. Таким образом, любой сравниваемый с ней оператор будет
иметь приоритет выше и располагаться над ней. Строка 15 определяет, что операнды могут
быть любыми символами в верхнем регистре или цифрами. Полная функция преобразования
показана в :ref:`ActiveCode 8 <lst_intopost>`.


.. _lst_intopost:

.. activecode:: intopost
   :caption: Преобразование инфиксного выражения в постфиксное

   from pythonds.basic.stack import Stack

   def infixToPostfix(infixexpr):
       prec = {}
       prec["*"] = 3
       prec["/"] = 3
       prec["+"] = 2
       prec["-"] = 2
       prec["("] = 1
       opStack = Stack()
       postfixList = []
       tokenList = infixexpr.split()

       for token in tokenList:
           if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
               postfixList.append(token)
           elif token == '(':
               opStack.push(token)
           elif token == ')':
               topToken = opStack.pop()
               while topToken != '(':
                   postfixList.append(topToken)
                   topToken = opStack.pop()
           else:
               while (not opStack.isEmpty()) and \
                  (prec[opStack.peek()] >= prec[token]):
                     postfixList.append(opStack.pop())
               opStack.push(token)

       while not opStack.isEmpty():
           postfixList.append(opStack.pop())
       return " ".join(postfixList)

   print(infixToPostfix("A * B + C * D"))
   print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

--------------

Ниже показаны ещё несколько примеров выполнения кода в оболочке Python.

::

    >>> infixtopostfix("( A + B ) * ( C + D )")
    'A B + C D + *'
    >>> infixtopostfix("( A + B ) * C")
    'A B + C *'
    >>> infixtopostfix("A + B * C")
    'A B C * +'
    >>>

Постфиксные вычисления
^^^^^^^^^^^^^^^^^^^^^^

As a final stack example, we will consider the evaluation of an
expression that is already in postfix notation. In this case, a stack is
again the data structure of choice. However, as you scan the postfix
expression, it is the operands that must wait, not the operators as in
the conversion algorithm above. Another way to think about the solution
is that whenever an operator is seen on the input, the two most recent
operands will be used in the evaluation.

To see this in more detail, consider the postfix expression
``4 5 6 * +``. As you scan the expression from left to right, you first
encounter the operands 4 and 5. At this point, you are still unsure what
to do with them until you see the next symbol. Placing each on the stack
ensures that they are available if an operator comes next.

In this case, the next symbol is another operand. So, as before, push it
and check the next symbol. Now we see an operator, \*. This means that
the two most recent operands need to be used in a multiplication
operation. By popping the stack twice, we can get the proper operands
and then perform the multiplication (in this case getting the result
30).

We can now handle this result by placing it back on the stack so that it
can be used as an operand for the later operators in the expression.
When the final operator is processed, there will be only one value left
on the stack. Pop and return it as the result of the expression.
:ref:`Figure 10 <fig_evalpost1>` shows the stack contents as this entire example
expression is being processed.

.. _fig_evalpost1:

.. figure:: Figures/evalpostfix1.png
   :align: center

   Figure 10: Stack Contents During Evaluation


:ref:`Figure 11 <fig_evalpost2>` shows a slightly more complex example, 7 8 + 3 2
+ /. There are two things to note in this example. First, the stack size
grows, shrinks, and then grows again as the subexpressions are
evaluated. Second, the division operation needs to be handled carefully.
Recall that the operands in the postfix expression are in their original
order since postfix changes only the placement of operators. When the
operands for the division are popped from the stack, they are reversed.
Since division is *not* a commutative operator, in other words
:math:`15/5` is not the same as :math:`5/15`, we must be sure that
the order of the operands is not switched.

.. _fig_evalpost2:

.. figure:: Figures/evalpostfix2.png
   :align: center

   Figure 11: A More Complex Example of Evaluation


Assume the postfix expression is a string of tokens delimited by spaces.
The operators are \*, /, +, and - and the operands are assumed to be
single-digit integer values. The output will be an integer result.

#. Create an empty stack called ``operandStack``.

#. Convert the string to a list by using the string method ``split``.

#. Scan the token list from left to right.

   -  If the token is an operand, convert it from a string to an integer
      and push the value onto the ``operandStack``.

   -  If the token is an operator, \*, /, +, or -, it will need two
      operands. Pop the ``operandStack`` twice. The first pop is the
      second operand and the second pop is the first operand. Perform
      the arithmetic operation. Push the result back on the
      ``operandStack``.

#. When the input expression has been completely processed, the result
   is on the stack. Pop the ``operandStack`` and return the value.

The complete function for the evaluation of postfix expressions is shown
in :ref:`ActiveCode 9 <lst_postfixeval>`. To assist with the arithmetic, a helper
function ``doMath`` is defined that will take two operands and an
operator and then perform the proper arithmetic operation.

.. _lst_postfixeval:

.. activecode:: postfixeval
   :caption: Postfix Evaluation

   from pythonds.basic.stack import Stack

   def postfixEval(postfixExpr):
       operandStack = Stack()
       tokenList = postfixExpr.split()

       for token in tokenList:
           if token in "0123456789":
               operandStack.push(int(token))
           else:
               operand2 = operandStack.pop()
               operand1 = operandStack.pop()
               result = doMath(token,operand1,operand2)
               operandStack.push(result)
       return operandStack.pop()

   def doMath(op, op1, op2):
       if op == "*":
           return op1 * op2
       elif op == "/":
           return op1 / op2
       elif op == "+":
           return op1 + op2
       else:
           return op1 - op2

   print(postfixEval('7 8 + 3 2 + /'))

It is important to note that in both the postfix conversion and the
postfix evaluation programs we assumed that there were no errors in the
input expression. Using these programs as a starting point, you can
easily see how error detection and reporting can be included. We leave
this as an exercise at the end of the chapter.

.. admonition:: Self Check

   .. fillintheblank:: postfix1
      :casei:
      :correct: \\b10\\s+3\\s+5\\s*\\*\\s*16\\s+4\\s*-\\s*/\\s*\\+
      :feedback1:  ('10.*3.*5.*16.*4', 'The numbers appear to be in the correct order check your operators')
      :feedback2: ('.*', 'Remember the numbers will be in the same order as the original equation')
      :blankid: pfblank1

      Without using the activecode infixToPostfix function, convert the following expression to postfix  ``10 + 3 * 5 / (16 - 4)`` :textfield:`pfblank1::xlarge`

   .. fillintheblank:: postfix2
      :correct: \\b9\\b
      :feedback1: ('.*', "Remember to push each intermediate result back on the stack" )
      :blankid: pfblank2

      ``17 10 + 3 * 9 / ==`` :textfield:`pfblank2::mini`

   .. fillintheblank:: postfix3
      :correct: 5\\s+3\\s+4\\s+2\\s*-\\s*\\^\\s*\\*
      :feedback1: ('.*', 'Hint: You only need to add one line to the function!!')
      :blankid: pfblank3

      Modify the infixToPostfix function so that it can convert the following expression:  ``5 * 3 ^ (4 - 2)``   Paste the answer here: :textfield:`pfblank3::large`


.. video:: video_Stack3
    :controls:
    :thumb: ../_static/activecodethumb.png

    http://media.interactivepython.org/pythondsVideos/Stack3.mov
    http://media.interactivepython.org/pythondsVideos/Stack3.webm
