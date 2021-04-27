#!/bin/bash

set -eu -o pipefail
set -x

apt update
apt install -y python python-pip
apt install -y python3 python3-pip

# for kerberos support
apt install -y libkrb5-dev krb5-user
cp -f /io/test_scripts/krb5.conf /etc/

# thrift_whl=$(find /io/local_pip_repo/thrift-sasl/ -name "thrift_sasl-*.whl")
# impyla_whl=$(find /io/pip-dists-build/wheelhouse/ -name "impyla-*.whl")

# pip install --upgrade --upgrade-strategy eager "$thrift_whl"
# pip install --upgrade --upgrade-strategy eager "$impyla_whl"[kerberos]
pip install --upgrade --upgrade-strategy eager impyla[kerberos]==0.17a4

# pip3 install --upgrade --upgrade-strategy eager "$thrift_whl"
# pip3 install --upgrade --upgrade-strategy eager "$impyla_whl"[kerberos]
pip3 install --upgrade --upgrade-strategy eager impyla[kerberos]==0.17a4

python /io/test_scripts/test-hive-py2-plain.py
python3 /io/test_scripts/test-hive-py3-plain.py

python /io/test_scripts/test-impala-py2-nosasl.py
python3 /io/test_scripts/test-impala-py3-nosasl.py

kinit -kt /io/test_scripts/hive.keytab hive@ROOT.HWX.SITE
python /io/test_scripts/test-hive-py2-gssapi.py
python3 /io/test_scripts/test-hive-py3-gssapi.py

kinit -kt /io/test_scripts/impala.keytab impala@ROOT.HWX.SITE
python /io/test_scripts/test-impala-py2-gssapi.py
python3 /io/test_scripts/test-impala-py3-gssapi.py

# python /io/test_scripts/test-impala-py2-ldap.py
# python3 /io/test_scripts/test-impala-py3-ldap.py
