# -*- coding:utf-8 -*-
# @Time : 2022/7/18 3:13 下午
# @Author : Bin Bin Xue
# @File : 11_file&content
# @Project : python_basic

'''
    文件/目录处理的相关模块：
        os模块：文件的基本处理
        shutil模块：文件和目录的复制、移动、删除、压缩、解压等高级处理

    11.1 文件的处理（介绍os的常用属性或函数）
        1_获取系统类型
            os.name
            注：当该属性值为nt时，表示为windows系统；posix表示Linux系统
            想要更详细的查看系统：
            sys.platform
            注：当该属性值为darwin时，表示mac系统

        2_获取系统环境
            os.environ
            os.getenv('PATH') - 系统变量

        3_执行系统命令
            os.system('bash command') - 使用os模块的system方法执行shell命令
            os.popen('bash command') - 读取系统命令的执行结果

        4_操作目录及文件
        （1）获取当前目录
                os.getcwd()
        （2）更改目录
                os.chdir('E:')
        （3）列举目录下的所有文件
                os.listdir('E:\\testdir')
        （4）创建及删除目录
                os.mkdir(path) - 创建单个目录
                os.makedirs(path) - 创建多级目录
                os.rmdir() - 删除单级空目录
                os.removedirs - 删除多级空目录
        （5）重命名目录或文件
                os.rename('原文件/目录名','修改后的文件/目录名')
        （6）获取文件的绝对路径
                os.path.abspath(path)
        （7）路径分解与组合
                os.path.split(path) - 将路径分解为目录和文件两个部分（二元组），根据'\'划分
                os.path.join(path1,path2..) - 按顺序合并，中间自动补上'\'
        （8）返回目录和文件名
                os.path.dirname(path) - 获取路径中的目录部分
                os.path.basename(path) - 获取path中的文件部分
        （9）判断及获取文件或文件夹信息
                os.path.exists(path) - 判断文件或文件夹是否存在
                os.path.isfile(path) - 判断路径是否是一个文件
                os.path.isdir(path) - 判断路径是否是一个目录
                os.path.isabs(path) - 判断路径是否是绝对路径
                os.path.getsize(path) - 获取文件或文件夹的大小
                os.path.getctime(path) - 获取文件/目录的创建时间
                os.path.getmtime(path) - 获取文件或目录的最后修改时间

    11.2 文件和目录的高级处理
        使用shutil模块进行文件复制、移动、删除、压缩、解压等高级操作
        11.2.1 复制文件
            (1)shutil.copyfileobj(sfile,dfile) - 将file1内容复制到file2中（覆盖，需要先创建两
                                                个文件并打开，且file2可写入）
            (2)shutil.copyfile(sfile,dfile) - 无需打开文件，直接用文件名进行覆盖
            (3)shutil.copymode(sfile,dfile) - 复制文件权限，其他不变
            (4)shutil.copystat(sfile,dfile) - 复制文件状态(权限、组、用户和时间等)
            (5)shutil.copy(sfile,dfile) - 复制内容和权限（前面两个的结合）
            (6)shutil.copy2(sfile,dfile) - 复制文件的内容和状态信息
            (7)shutil.copytree() - 递归地复制文件内容及状态信息

        11.2.2 移动文件
            shutil.move(src,dst,copy_function=copy2) - 递归地移动文件或重命名，
        并返回目标（若目标是现有目录，则移动文件到目录；若有同名文件，
        可能会覆盖）

        11.2.3 读取压缩及归档压缩文件
        shutil.make_archive(base_name,format,root_dir) - 按指定格式压缩文件
            三个参数分别是压缩后文件名、压缩格式、归档目录
            目前支持的压缩格式为zip,tar,bztar

        11.2.4 解压文件
        shutil.unpack_archive(filename,extract_dir) - 解压文件
            两个参数分别是要解压的文件、解压后的存档目录


'''

import os
import sys
import shutil

print('----------查看系统----------')
print(os.name)
print(sys.platform)

print('----------查看环境----------')
env = os.environ
for e in env:
    print(e)
print(os.getenv('PATH'))

print('----------执行系统命令----------')
# os.system('ping www.baidu.com')
# os.popen('ping www.baidu.com').read()

print('----------操作目录及文件----------')
cc = os.getcwd()
print('当前目录：\n'+ cc)
print('列举目录下的所有文件：')
print(os.listdir())
# 创建及删除目录:
# os.mkdir('./dir1')
# os.makedirs('./dir1/dir2/dir3')
# os.rmdir('./dir1')
# os.removedirs('./dir1/dir2/dir3')
print('文件的绝对路径：')
# 一个点到上当前的上一级，两个点到上两级
print(os.path.abspath('.'))
print('文件路径分解：')
print(os.path.split(cc))
print('文件路径组合：')
# 不会创建文件
print(os.path.join(os.path.abspath('.'),'hello.py'))
print('返回目录和文件名：')
print(os.path.dirname(cc))
print(os.path.basename(cc))
print('判断文件或目录是否存在：')
print(os.path.exists(cc))
print('判断是否是文件：')
print(os.path.isfile(cc))
print('获取文件大小：')
print(os.path.getsize(cc))
print('获取文件创建时间：')
print(os.path.getctime(cc))
print('获取文件最后的修改时间：')
print(os.path.getatime(cc))

print('----------文件的高级操作----------')
# print('复制文件：')
# f1 = shutil.copy('11_file&content.py','10_file.py')
# print('压缩文件：')
# new_path = shutil.make_archive(cc,'zip')
# print('解压文件：')
# shutil.unpack_archive()
