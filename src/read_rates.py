#!/usr/bin/env python

import iopro
from os.path import exists

path = '/Users/dmertz/Data/health-insurance-marketplace/'
filename = 'Rate.csv.gz'   # 13M lines, 2GB raw, 110MB compressed

adapter = iopro.text_adapter(path+filename,
                             compression='gzip',
                             parser='csv',
                             index_name='Rate.index')

datatypes = dict()
for field in (0, 1, 3, 5, 7, 8, 9, 10, 11, 12, 14, 15):
    datatypes[field] = 'O'
adapter.set_field_types(datatypes)

row = int(9e6)
arr = adapter[row:row+5]
print("Read %s" % filename)
