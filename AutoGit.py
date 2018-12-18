import os
from git import Repo

#运行程序前，请保证文件 config.ini 中的内容是下面这样的（不包括引号）：
'''
path=D:\Study\GitHub\Algorithm 
remote=origin
fetch=master
'''

config = open('config.ini', 'r') #读取配置文件

path = config.readline().split('=')[1][:-1] #获取本地仓库路径，去掉末尾的换行符
remote_repo = config.readline().split('=')[1][:-1] #获取远程仓库名
fetch = config.readline().split('=')[1][:-1] #获取分支名
config.close()

repo = Repo(path) #初始化 git 仓库

git = repo.git #获取 git 对象
image_postfix = ['jpg', 'png', 'jpeg', 'gif'] #图片后缀名
needToUpdate = False #标记是否需要提交到远程仓库

while True:
        if len(repo.untracked_files) > 0:
                for file_name in repo.untracked_files:
                        if file_name.split('.')[-1] in image_postfix: #如果文件类型是图片
                                git.add(file_name)
                                needToUpdate = True
                git.commit('-m', 'git operation')
                remote = repo.remote(remote_repo) #获取远程版本库 alg
                remote.pull(fetch) #从远程版本库拉取分支
                remote.push(fetch) #推送本地分支到远程版本库
