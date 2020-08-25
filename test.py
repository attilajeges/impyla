#!/usr/bin/python

import os
from impala.dbapi import connect
from impala.util import as_pandas

# host = 'attilaj-1.attilaj.root.hwx.site'
# test_hive_port = 10000
# conn = connect(host, test_hive_port,
#   auth_mechanism="GSSAPI",
#   kerberos_service_name='hive',
#   password='Password@123')

host = 'attilaj-1.attilaj.root.hwx.site'
test_hive_port = 10001
conn = connect(host, test_hive_port,
  auth_mechanism="GSSAPI",
  kerberos_service_name='hive',
  password='Password@123',
  use_http_transport=True,
  http_path='cliservice')

cursor = conn.cursor()
cursor.execute("show databases")
print cursor.fetchall()

