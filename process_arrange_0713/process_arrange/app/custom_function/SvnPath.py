
#
# class SvnPath(object):
#
#     @staticmethod
#     def svn_update(**kwargs):
import os
import sys
# 列出当前目录下所有一级文件夹
def dirpathlist(lpath, outlist):
    file_list = os.listdir(lpath)
    for f in file_list:
        filename = os.path.join(lpath, f)
        if os.path.isdir(filename):
            outlist.append(filename)
    return outlist

# 执行SVN更新
def svnupdate(path):
    cmd = 'TortoiseProc.exe /command:update /path:"{}" /closeonend:0'.format(path)
    os.system(cmd)

if __name__ == '__main__':
    path = "F:\\test_svn_url"
    a = sys.path
    out_list = dirpathlist(path, [])
    for f in out_list:
        print('更新 {}'.format(f))
        svnupdate(f)

pass


