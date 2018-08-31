#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys, os
from os import path


def format_output(msg, color=31):
    return '''\033[0;%d;1m%s\033[0m''' % (color, msg)


def convert(fn):
    if path.splitext(fn)[1] == '.pcm':
        mp3 = path.splitext(fn)[0] + '.mp3'
        # echo -e '\e[0;37;1mThis is print\e[0m' 带颜色的echo输出
        # os.system('''echo -e "\033[0;37;1mconvert %s to %s\033[0m"''' % (fn, mp3))
        print('\n\nconvert %s to %s' % (format_output(fn), format_output(mp3, 36)))
        os.system('ffmpeg -y -f s16le -ar 8000 -ac 2 -i "%s" -acodec libmp3lame "%s"' % (fn, mp3))


def convert_dir(dn):
    for fn in [path.join(dn, fn) for fn in os.listdir(dn)]:
        if path.isdir(fn):
            convert_dir(fn)
        else:
            convert(fn)

if __name__ == "__main__":
    convert_dir(sys.argv[1])
