#!/usr/bin/env python
# Filename: CheckApkSignature.py
import sys
import os

def returnSignature(apk, flag):
 cmd = 'jar xf ' + apk + ' META-INF/'
 os.system(cmd)
 filepath = ''
 for d, fd, fl in os.walk('META-INF/'):
  for f in fl:
   fname = os.path.splitext(f)[0]
   sufix = os.path.splitext(f)[1]
   if (sufix == '.RSA' or sufix == '.DSA'):
    filepath = 'META-INF/' + fname + sufix
 result = ''
 if (filepath != ''):
  cmd = 'keytool -printcert -file ' + filepath + ' | grep ' + flag + ':'
  result = os.popen(cmd).read().strip()
  cmd = 'rm -rf META-INF/'
  os.system(cmd)
 return result

def returnMD5(apk):
 return returnSignature(apk, 'MD5')

def returnSHA1(apk):
 return returnSignature(apk, 'SHA1')

def checkMD5(apk_1, apk_2):
 md5_1 = returnMD5(apk_1)
 print apk_1 + '\n\t' + md5_1
 md5_2 = returnMD5(apk_2)
 print apk_2 + '\n\t' + md5_2
 print '\033[1;31;40m'
 if (md5_1 != md5_2):
  print 'They have the different MD5'
 else:
  print 'They have the same MD5'

def checkSHA1(apk_1, apk_2):
 sha1_1 = returnSHA1(apk_1)
 print apk_1 + '\n\t' + sha1_1
 sha1_2 = returnSHA1(apk_2)
 print apk_2 + '\n\t' + sha1_2
 print '\033[1;31;40m'
 if (sha1_1 != sha1_2):
  print 'They have the different SHA1'
 else:
  print 'They have the same SHA1'

print '\033[1;37;40m'
print '====== Coder Jason <ravegenius1985@126.com> ======'
if (len(sys.argv) == 2):
 apk = sys.argv[1]
 print '\033[1;32;40m'
 print apk + '\n\t' + returnMD5(apk)
 print apk + '\n\t' + returnSHA1(apk)
 print '\033[0m'
elif (len(sys.argv) == 3):
 apk_1 = sys.argv[1]
 apk_2 = sys.argv[2]
 print '\033[1;32;40m'
 checkMD5(apk_1, apk_2)
 print '\033[0m'
 print '\033[1;32;40m'
 checkSHA1(apk_1, apk_2)
 print '\033[0m'
else:
 print '\033[1;32;40m'
 print 'parameters wrong'
 print '\033[0m'

