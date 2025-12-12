import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
x = re.findall('@([^ ]*)', lin)
y = re.findall('^From .*@([^ ]*)', lin)
print(x)
print(y)