from impala.dbapi import connect

def binary():
  conn = connect('cardassia-2.cardassia.root.hwx.site',
    10000,
    auth_mechanism="LDAP",
    user='cm-admin',
    password='Test123',
    use_ssl=True,
  )

  cursor = conn.cursor()
  cursor.execute("select * from web_logs")
  res = cursor.fetchall()
  print(len(res))

  cursor.close()
  conn.close()

def hs2_http():
  conn = connect('cardassia-2.cardassia.root.hwx.site',
    10001,
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
  print(len(res))

  cursor.close()
  conn.close()

hs2_http()
binary()
