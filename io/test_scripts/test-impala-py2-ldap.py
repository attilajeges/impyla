from impala.dbapi import connect

def binary():
  conn = connect('cardassia-1.cardassia.root.hwx.site',
    21050,
    auth_mechanism="LDAP",
    user='cm-admin',
    password='Test123',
    use_ssl=True,
  )
  
  cursor = conn.cursor()
  cursor.execute("select * from web_logs")
  res = cursor.fetchall()
  print len(res)
  
  cursor.close()
  conn.close()

def hs2_http():
  conn = connect('cardassia-1.cardassia.root.hwx.site',
    28000,
    auth_mechanism="LDAP",
    user='cm-admin',
    password='Test123',
    use_ssl=True,
    use_http_transport=True,
    http_path='cliservice',
  )
  
  cursor = conn.cursor()
  cursor.execute("select * from web_logs")
  res = cursor.fetchall()
  print len(res)
  
  cursor.close()
  conn.close()

binary()
hs2_http()
