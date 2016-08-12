# 43 = "Yes"
# 45 = "$16.67"
# 48 = "\d{2}%"
# 56 = "$0.00"
# 62 = "Yes"
# 63 = "70.92%"
# 100 = "Individual"
# 101 = "Yes"
# 102 = "Yes"
# 104 = "Yes"
# 112 = "1/1/2016"
# 113 = "12/31/2050"

datatypes = {0:'f4'}

for field in (5, 6, 43, 44, 47, 45, 48, 49, 50, 51, 55, 56, 58, 
             60, 62, 63):
    datatypes[field] = 'O'
for field in range(65, 176):
    datatypes[field] = 'O'
