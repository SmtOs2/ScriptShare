#########################################################################
# File Name: pushFrameworkJar.sh
# Author: octopus
# mail: octopus_work.163.com
# Created Time: 2016年07月12日 星期二 16时00分31秒
#########################################################################
#!/bin/sh
if [ $# -lt 1 ];then
echo "USAGE: pushFrameworkJar.sh trident"
exit 1;
fi
CCA=$1
adb root
adb remount
sleep 5
adb wait-for-device
adb push out/target/product/$CCA/system/framework/arm/ /system/framework/
adb push out/target/product/$CCA/system/framework/arm64/ /system/framework/
adb push out/target/product/$CCA/system/framework/framework.jar /system/framework/
