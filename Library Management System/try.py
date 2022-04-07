from datetime import datetime
from time import strftime
date_format = "%d/%m/%Y"
x = strftime("%d/%m/%Y")
a = datetime.strptime(str(x), date_format)
b = datetime.strptime('27/09/2021', date_format)
delta = b - a
u=(delta.days)%30
print(u)