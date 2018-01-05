
#———————————————git———————————————————#
git init
git config --global user.name/email '名字邮箱'
git add xxx.txt
git status #状态
git commit -m '备注' #提交
git reset --hard HEAD^/0000000 #返回版本
git reflog  #记录
git diff HEAD --XXX.txt #查看各版本不同
git checkout --xxx.txt #撤销缓存区的修改 



#———————————————其他——————————————————#
nohup ssserver -c xxx.json >test.log 2>&1 &
# 后台运行并保存记录log
tail -f test.log 
#实时擦看 test.log 数据
cat test.log 
#擦看数
ssh-keygen -t rsa -C "youremail@example.com"  # 获取生产 ssh_keys

#_____________基础命令________________#

reboot
#重启
sudo apt-get updeta
#更新软件下载链接
apt-get install Python3-pip
#安装pip
