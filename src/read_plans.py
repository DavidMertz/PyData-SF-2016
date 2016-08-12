#!/usr/bin/env python

from time import ctime
import iopro
from keys import aws_access_key, aws_secret_key, bucket
from conversions import datatypes

key_name = 'PlanAttributes.csv' # 77k lines, 95MB
adapter = iopro.s3_text_adapter(aws_access_key, 
                                aws_secret_key,
                                bucket, 
                                key_name,
                                index_name='PlanAttributes.index')

adapter.set_field_types(datatypes)
row = 70000
arr = adapter[row:row+5]
print("Read %s at %s" % (key_name, ctime()))

