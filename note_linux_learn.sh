#———————————————vim———————————————————————————————————————————————————#

#———————————————git——————————————————————————————————————————————————#
git init
git config --global user.name/email '名字邮箱'
git add xxx.txt
git status #状态
git commit -m '备注' #提交
git reset --hard HEAD^/0000000 #返回版本
git reflog  #记录
git diff HEAD --XXX.txt #查看各版本不同
git checkout --xxx.txt #撤销缓存区的修改 

git push         #  update githup
git clone git@github.com:loserAI/LinuxLaern.git    # clone githup project（项目）
#———— git分支——————#
git branch  #查看分支
git branch <name>   # 创建分支：
git checkout <name> #切换分支：
git checkout -b <name> #创建+切换分支：
git merge <name> #合并某分支到当前分支：
git branch -d <name> #删除分支：


#———————————————其他———————————————————————————————————————#
nohup ssserver -c xxx.json >test.log 2>&1 &
# 后台运行并保存记录log
tail -f test.log 
#实时擦看 test.log 数据
cat test.log 
#擦看数
ssh-keygen -t rsa -C "youremail@example.com"  # 获取生产 ssh_keys

#_____________基础命令______________________________________#
find / -name my_file #查找 / 下的my_files
find / -amin -10 # 查找在系统中最后10分钟访问的文件 
find / -atime -2 # 查找在系统中最后48小时访问的文件 
find / -empty # 查找在系统中为空的文件或者文件夹 
find / -group cat # 查找在系统中属于groupcat的文件 
find / -mmin -5 # 查找在系统中最后5分钟里修改过的文件 
find / -mtime -1 #查找在系统中最后24小时里修改过的文件 
find / -nouser #查找在系统中属于作废用户的文件 
find / -user fred #查找在系统中属于FRED这个用户的文件

dpkg-reconfigure tzdata  # change time china 改时区
top  # cpu  ram
reboot
#重启
sudo apt-get updeta
#更新软件下载链接
apt-get install Python3-pip
#安装pip
