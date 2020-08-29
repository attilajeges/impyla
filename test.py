#!/usr/bin/python

import os
from impala.dbapi import connect
from impala.util import as_pandas

import logging
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(logging.StreamHandler())

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
  http_path='cliservice',
  auth_cookie_name='hive.server2.auth')

cursor = conn.cursor()

cursor.execute("show databases")
print 'show databases 1: %s' %  cursor.fetchall()

cursor.execute("show tables")
print 'show tables 2: %s' %  cursor.fetchall()

cursor.execute("show databases")
print 'show databases 3: %s' %  cursor.fetchall()

