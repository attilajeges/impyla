from impala.dbapi import connect
  
# binary
def binary():
  conn = connect('attilaj-2.attilaj.root.hwx.site',
    21050,
    auth_mechanism="NOSASL",
  )

  cursor = conn.cursor()
  cursor.execute("select * from web_logs")
  res = cursor.fetchall()
  print(len(res))

  cursor.close()
  conn.close()

# hs2-hhtp
def hs2_http():
  conn = connect('attilaj-2.attilaj.root.hwx.site',
    28000,
    auth_mechanism="NOSASL",
    use_http_transport=True,
    http_path='cliservice',
  )

  cursor = conn.cursor()
  cursor.execute("select * from web_logs")
  res = cursor.fetchall()
  print(len(res))

  cursor.close()
  conn.close()

binary()
hs2_http()
