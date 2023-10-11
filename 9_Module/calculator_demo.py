# from module_demo1 import summation, subtraction
# from module_demo1 import *
from module_demo1 import summation as sm
from module_demo1 import subtraction as sb
from Functions.function_demo4 import print_animals
# import module_demo2
import module_demo2 as md2

print(sm(10, 50))
print(sb(30, 10))

print(print_animals('tiger', 'cat'))

# print(module_demo2.multiply(10, 20))
print(md2.division(20, 10))
