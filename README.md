git的用法
============
git的组成
-------------	
git由三部分组成，分别为目录，索引以及仓库。
目录可以存放文档的索引，并对其进行追踪，控制
索引将生成一个临时存储区域，
仓库：将索引通过commit命令提交至仓库。而进行更新。
创建版本库：
-------------
通过git init 将目录变成一可以管理的仓库
然后在github上创建自己的new repository
最后将本地文件传送至github中。

git的操作
----------

*git add *#跟踪新文件

*rm *&git rm *#移除文件

*git rm -f *#移除文件

*git rm --cached *#取消跟踪

*git mv file_from file_to#重命名跟踪文件

*git log#  查看提交记录

>git commit#提交更新  
>git commit -m 'message'  
>git commit -a#跳过使用暂存区域，把所有已经跟踪过的文件暂存起来一并提交  
>git commit --amend#修改最后一次提交  

git reset HEAD *#取消已经暂存的文件

git checkout -- file#取消对文件的修改（从暂存区去除file）
git checkout branch|tag|commit -- file_name#从仓库取出file覆盖当前分支
git checkout -- .#从暂存区去除文件覆盖工作区什么是git
git diff 查询差异
git stash 保存进度
git status 查看版本库当前状态
rm*.txt 工作区删除这些文件
git ls-files（暂存区中文件仍然存在）
git rm删除

	设置id email
git config --global user.name "zhang"
git config --global user.email yuanfan@openerp.cn

[this link](https://github.com/shineit-yuanfan/learning)


git branch -d mybranch1 删除分支 
git checkout master 切换分支





