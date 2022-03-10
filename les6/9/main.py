#Дан текст одной из работ. Используя метод count() необходимо посчитать, сколько раз в ней встречаются следующие подстроки: ‘the’ , ‘of’ , ‘in’ и вывести результат на экран
text = "Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."
symbol_the = "Строка 'the' встречается "
symbol_of = "Строка 'of' встречается "
symbol_in ="Строка 'in' встречается "
quantity = " раз(а)"