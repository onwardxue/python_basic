# -*- coding:utf-8 -*-
# @Time : 2022/7/18 6:10 下午
# @Author : Bin Bin Xue
# @File : project6_fileprocess
# @Project : python_basic

'''
    文件处理实战

    - 内容：创建一个小应用，用于处理一个用于训练的图片文件夹中的文件。
                该应用实现：
                （1）删除图片库中的非图片文件
                （2）对图片文件按一定规律命名
                （3）创建图片索引，方便图像识别程序能直接根据图片索引处理

'''

import os
import shutil
import time

# 可选的图片列表
IMG = ['jpg', 'jpeg', 'gif', 'png']


# 重命名图片及删除非图片文件
def rename_image(path):
    global i
    # 判断是否是文件或目录
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    # 如果是文件
    if os.path.isfile(path):
        # 分割出目录与文件名
        file_path = os.path.split(path)
        # 分割出文件与扩展名
        lists = file_path[1].split('.')
        # 取出后缀名进行判断（确定是否是图片格式）
        file_ext = lists[-1]
        if file_ext in IMG:
            # 重命名为"原名+序号i的值"
            os.rename(path, file_path[0] + '/' + lists[0] + str(i) + '.' + file_ext)
            i += 1
        else:
            # 不是图片格式的进行删除
            print(file_path)
            os.remove(os.path.join(file_path[0], file_path[1]))
    # 如果是目录，则对目录下的每个文件继续使用该函数处理
    elif os.path.isdir(path):
        for x in os.listdir(path):
            rename_image(os.path.join(path, x))


# 创建索引的txt文件
def create_index(path):
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    # 如果是目录
    if os.path.isdir(path):
        # 获取目录下所有的图片名
        lists = os.listdir(path)
        # 创建并打开index.txt文件
        with open(os.path.join(path, 'index.txt'), 'a+', encoding='utf-8') as f:
            # 将每个图片文件名都写入.txt文件
            for item in lists:
                f.write(item)
                f.write('\n')


# 压缩目录文件
def archive_dir(path):
    shutil.make_archive(path, 'zip')


# 主函数
def main(path):
    rename_image(path)
    create_index(path)
    archive_dir(path)


if __name__ == '__main__':
    img_dir = input('请输入路径：')
    start = time.time()
    i = 0
    main(img_dir)
    m = time.time() - start
    print('程序运行耗时：%0.2f' % m)
    print('总共处理了%d张图片' % i)
