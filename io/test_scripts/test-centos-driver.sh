#!/bin/bash
# Copyright 2015 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -eu -o pipefail
set -x

# For kerberos support
yum install -y krb5-libs krb5-devel krb5-server krb5-workstation
export PATH="/usr/kerberos/bin:$PATH"
cp -f /io/test_scripts/krb5.conf /etc/

# thrift_whl=$(find /io/local_pip_repo/thrift-sasl/ -name "thrift_sasl-*.whl")
# impyla_whl=$(find /io/pip-dists-build/wheelhouse/ -name "impyla-*.whl")

# python3
export PATH="/opt/python/cp39-cp39/bin:$PATH"

# pip install --upgrade --upgrade-strategy eager "$thrift_whl"
# pip install --upgrade --upgrade-strategy eager "$impyla_whl"[kerberos]
pip install --upgrade --upgrade-strategy eager impyla[kerberos]==0.17a5

python /io/test_scripts/test-hive-py3-plain.py
python /io/test_scripts/test-impala-py3-nosasl.py

kinit -kt /io/test_scripts/hive.keytab hive@ROOT.HWX.SITE
python /io/test_scripts/test-hive-py3-gssapi.py

kinit -kt /io/test_scripts/impala.keytab impala@ROOT.HWX.SITE
python /io/test_scripts/test-impala-py3-gssapi.py

# python /io/test_scripts/test-impala-py3-ldap.py

# python2
yum install -y python27
export PATH="/opt/rh/python27/root/usr/bin:$PATH"
export LD_LIBRARY_PATH="/opt/rh/python27/root/usr/lib64:$LD_LIBRARY_PATH"

# pip install "$thrift_whl"
# pip install "$impyla_whl"[kerberos]
pip install impyla[kerberos]==0.17a5

python /io/test_scripts/test-hive-py2-plain.py
python /io/test_scripts/test-impala-py2-nosasl.py

kinit -kt /io/test_scripts/hive.keytab hive@ROOT.HWX.SITE
python /io/test_scripts/test-hive-py2-gssapi.py

kinit -kt /io/test_scripts/impala.keytab impala@ROOT.HWX.SITE
python /io/test_scripts/test-impala-py2-gssapi.py

# python /io/test_scripts/test-impala-py2-ldap.py
