# +77785087826
import re

txt = 'The rain in Spain'
x = re.search("^The.*Spain$", txt)
print(x)


txt1 = 'The rain in Spain'
y = re.search("^The.*Italy$", txt1)
print(y)

## ^ - начало
## $ - конец
## . - любой симводл