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

以改变时间为条件push文件到手机对应的目录。并且如果push的文件中有apk文件，会自动查找包名并kill进程以使push的apk生效。
比如我常用的命令是`mm && AdbPushChanges`，就会以当前项目为锚，找到out目录下1分钟内变化的文件并push到手机。
如果我此时在`packages/apps/sidebar`下，那么应该会push Sidebar的apk，并kill com.smartisanos.sidebar进程。


## pcm2mp3.py

    pcm2mp3.py path

从`path`递归的把pcm转成mp3，需要apt安装ffmpeg。

