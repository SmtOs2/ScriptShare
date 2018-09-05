# 公用脚本

## 基本配置
```
请先修改下面三变量，然后在.bashrc中加上类似下面的配置:
SMT_SHELL_SHARE_HOME为克隆的ScriptShare下的bin目录
SMT_SRC_HOME为你检出的os源码的根目录
SMT_MAIN_PROJECT为你现在主要用来编译开发的项目，如:trident或ocean

例如下面这样:
SMT_SHELL_SHARE_HOME=$HOME/git_smt/ScriptShare/bin
SMT_SRC_HOME=$HOME/src
SMT_MAIN_PROJECT=trident
export SMT_SHELL_SHARE_HOME
export SMT_SRC_HOME
export SMT_MAIN_PROJECT
if test -e $SMT_SHELL_SHARE_HOME/installconfig; then
     . $SMT_SHELL_SHARE_HOME/installconfig
fi
```
## installconfig 中相关脚本
```
makeideapills makesara makesidebar maketextboom 会分别cd到你os的源码路径(SMT_SRC_HOME配置影响)
对应SMT_MAIN_PROJECT目录下编译并push，杀掉手机对应进程。比如我现在SMT_MAIN_PROJECT配置的是trident，
那就会cd到$SMT_SRC_HOME/android-trident-dev/package/apps/对应应用下去编译push。
类似：
makeideapills trident trinity 会去对应trident-trinity目录下编译push，杀进程
makeideapills ocean 会去对应ocean目录下编译push，杀进程

pushideapills pushsara pushsidebar pushtextboom 跟make...的区别是不会编译，只会push上次编译的结果
类似：
pushtextboom trident trinity
pushtextboom ocean
```      
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


## pullheap

把指定包名的 app 的 memheap dump 出来，pull 到 ~/Temp/memdump/ 目录下，并转化成能用 MAT 直接能打开的 hprof 格式。(Android/platform-tools/ 需要在环境路径里，因为要用到里面的 hprof-conv 来转换 heap 文件)

```sh
➜  ~ pullheap com.smartisanos.sara
### NOTICE ###: dumpheap begin
Dumping file...current size = 0
...
### SUCCESS ###: all done!
file location: /home/you/Temp/memdump/com.smartisanos.sara-2018-08-31/com.smartisanos.sara-conv.hprof
```

## systrace
systrace就是systrace.py把常用参数跟上的alias

```
systrace 会dump现在10秒内的trace

systrace 5 会dump5秒内的trace

```

## adbkill中相关脚本
```
  会杀掉包含关键词的进程：
  adbkill sara  会杀掉sara的进程
  adbkill sidebar  会杀掉sidebar的进程
```
## framework代码push相关脚本

```
  需要先自己cd到对应项目源码根路径, pushFrameworkJar.sh会push framework.jar, pushServiesJar.sh会push services.jar  
  pushFrameworkJar.sh trident  
  pushServiesJar.sh trident

```
