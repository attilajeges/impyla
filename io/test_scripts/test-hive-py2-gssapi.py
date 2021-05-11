from impala.dbapi import connect

def binary():
  conn = connect('betazoid-1.betazoid.root.hwx.site',
    10000,
    auth_mechanism="GSSAPI",
    kerberos_service_name='hive',
    use_ssl=True
  )
  
  cursor = conn.cursor()
  cursor.execute("select * from web_logs")
  res = cursor.fetchall()
  print len(res)
  
  cursor.close()
  conn.close()

def hs2_http():
  conn = connect('betazoid-1.betazoid.root.hwx.site',
    10001,
    auth_mechanism="GSSAPI",
    kerberos_service_name='hive',
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
