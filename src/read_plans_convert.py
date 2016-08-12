#!/usr/bin/env python

import iopro
from conversions import datatypes

path = '/Users/dmertz/Data/health-insurance-marketplace/'
filename = 'PlanAttributes.csv' # 77k lines, 95MB

adapter = iopro.text_adapter(path+filename, 
                             index_name='PlanAttributes.index')
adapter.create_index('PlanAttributes.index')

adapter.set_field_types(datatypes)
row = 70000
arr = adapter[row:row+5]
print("Read %s" % (filename))

