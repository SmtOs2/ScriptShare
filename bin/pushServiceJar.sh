#########################################################################
# File Name: pushServiceJar.sh
# Author: octopus
# mail: octopus_work.163.com
# Created Time: 2016年05月30日 星期一 19时47分10秒
#########################################################################
#!/bin/bash
if [ $# -lt 1 ];then
echo "USAGE: pushServiceJar.sh trident [-a]"
exit 1;
fi
CCA=$1
PARAM=$2
if [ "$PARAM" = "-a" ];then
adb push out/target/product/$CCA/system/lib64/libandroid_servers.so system/lib64/
adb push out/target/product/$CCA/system/lib/libandroid_servers.so system/lib/
fi
adb push out/target/product/$CCA/system/framework/services.jar system/framework/
adb push out/target/product/$CCA/system/framework/arm/  system/framework/
adb push out/target/product/$CCA/system/framework/arm64/  system/framework/
