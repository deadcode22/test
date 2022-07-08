from datetime import datetime
import os
os.system('git pull')
i = int(input(" ENTER YOUR DTE OF BERTH : "))
day = datetime.today()
year = day.year
age = int(year)-int(i)
print(" YOUR AGE IS : \033[1;36m",age)