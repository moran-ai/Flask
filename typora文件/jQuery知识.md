# jQuery知识

jQuery中$和$.的区别

$ 是jQuery的别称

jQuery是jQuery库中提供的一个函数，例如：$.ajax(options)等同于 jQuery.ajax(options)

$():这个函数的作用是根据()里的参数进行查找和选择html文档中的元素，函数作用之一就是GetElementByID的代替，但是()内不仅仅可以是元素，还可以是各类选择器

例如：$(document)就是选择整个文档对象

区别：

​			**$就是jQuery对象，**

​			**$()就是jQuey(),里面可以传参数，作用是获取元素**

