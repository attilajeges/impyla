from impala.dbapi import connect

def binary():
  conn = connect('attilaj-1.attilaj.root.hwx.site',
    10000,
    auth_mechanism="PLAIN",
  )

  cursor = conn.cursor()
  cursor.execute("select * from web_logs")
  res = cursor.fetchall()
  print(len(res))

  cursor.close()
  conn.close()

def hs2_http():
  conn = connect('attilaj-1.attilaj.root.hwx.site',
    10001,
    auth_mechanism="PLAIN",
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
