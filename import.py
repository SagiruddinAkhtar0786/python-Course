""" from math import sqrt,pi

result = sqrt(9) * pi
print(result)
 """

""" import math as m

result = m.sqrt(9) * m.pi
print(result) """

import math
print(dir(math))

""" from OuterImport import welcome,sagir
welcome()
print(sagir) """

import OuterImport as OI
OI.welcome()
print(OI.sagir)


