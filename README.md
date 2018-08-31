# 公用脚本

## CheckApkSignature.py

      CheckApkSignature.py test.apk
      
查看APK的签名信息，可输出MD5和SHA1。

## AdbPushChanges

    AdbPushChanges [options]
    options可以是：
    -m[in]     n    : 以分钟为单位指定筛选out目录下n分钟之内有变化的文件，默认n=1,可以为小数。
    -d[ay]     n    : 以天为单位定筛选out目录下n天之内有变化的文件，默认不使用该参数，而是使用‘-m 1’,可以为小数。
    -c[ontain] name : 限定只过滤出包含‘name’关键词的变化文件,支持正则。
    -f[ilter]  name : 限定从结果中移除包含‘name’关键词的变化文件，支持正则。
    -p[rint]        : 仅仅打印执行此命令会做的操作，不实际执行。

以改变时间为条件push文件到手机对应的目录。不加任何参数时默认筛选时间为**1分钟**。并且如果push的文件中有apk文件，会**自动查找包名并kill进程**以使push的apk生效。

### 使用示例：
* Sidebar模块开发

       $cd /data/project/android-trident-trinity/packages/apps/Sidebar
       $mm && AdbPushChanges
 
 然后等待Sidebar进程重启就好了
 
 * framework修改
 
       $cd /data/project/android-trident-trinity/frameworks/base
       $mma
       $AdbPushChanges -m 5 -p
       
加上`-m 5`，查看近5分钟改变的文件，因为framework文件比较多，不是所有生成的文件都是1分钟内生成的。另外，由于framework编译生成的文件比较多，谨慎起见，还是用`-p`参数先输出看下。得到输出（并不执行push）：

      ...
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/arm/boot-okhttp.oat /system/framework/arm
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/arm/boot-legacy-test.vdex /system/framework/arm
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/services.jar /system/framework
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/framework.jar /system/framework
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/arm/boot.oat /system/framework/arm
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/priv-app/SharedStorageBackup/oat/arm64/SharedStorageBackup.vdex /system/priv-app/SharedStorageBackup/oat/arm64
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/priv-app/LockTaskTests/oat/arm64/LockTaskTests.odex /system/priv-app/LockTaskTests/oat/arm64
      ...

发现有些priv-app的内容也被输出了，但我只想push framework下的内容。于是使用`-c`过滤下（还可以用`-f`剔除不需要的），只输出包含`/framework/`的内容：

      $AdbPushChanges -m 5 -c "/framework/" -p
      
然后得到输出：

      ...
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/arm/boot-okhttp.oat /system/framework/arm
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/arm/boot-legacy-test.vdex /system/framework/arm
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/services.jar /system/framework
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/framework.jar /system/framework
      adb push /data/project/android-trident-trinity/out/target/product/trident/system/framework/arm/boot.oat /system/framework/arm
      ...

然后就放心执行命令了，然后重启手机使新的framework生效：

      $AdbPushChanges -m 5 -c "/framework/" && adb reboot

## pcm2mp3.py

    pcm2mp3.py path

从`path`递归的把pcm转成mp3，需要apt安装ffmpeg。

