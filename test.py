#!/usr/bin/python2

import os
import time
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
time.sleep(2)

cursor.execute("show tables")
print 'show tables 2: %s' %  cursor.fetchall()
time.sleep(2)

cursor.execute("show databases")
print 'show databases 3: %s' %  cursor.fetchall()
time.sleep(2)

cursor.execute("drop table if exists tbl")
time.sleep(2)
cursor.execute("create table tbl (id integer, s string)")
time.sleep(2)

insert_parts = ["insert into tbl(id, s) values (133, 'xxx')"]
for i in range(0, 1000):
  insert_parts.append("(%s, 'bbb')" % i)
stmt = ', '.join(insert_parts)
cursor.execute(stmt)
time.sleep(2)

cursor.execute("select id, s from tbl")
print 'select id, s rom tbl: %s' %  cursor.fetchall()
