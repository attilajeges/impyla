from impala.dbapi import connect

def hs2_http():
  conn = connect('coordinator-denys-test1-impala.apps.dev-02.kcloud.cloudera.com',
    443,
    auth_mechanism="LDAP",
    user='cm-admin',
    password='Test123',
    use_ssl=True,
    use_http_transport=True,
    http_path='cliservice',
  )
  
  cursor = conn.cursor()
  cursor.execute("show databases;")
  res = cursor.fetchall()
  print len(res)
  
  cursor.close()
  conn.close()

hs2_http()
