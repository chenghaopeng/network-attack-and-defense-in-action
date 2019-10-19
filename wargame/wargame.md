###  level02
attack-env-again

修改USER变量, export USER='`/bin/getflag01`'
![](img/level02.png)

### level03
attack-crontab

在writable.d下创建文件test,内容为`/bin/getflag03>/home/flag03/a.txt`
程序会不定期调用该test文件
在a.txt中查看flag
![](img/level03.png)

### level04
get-token

用ln -s /home/flag04/token /home/level04/test1创建链接
执行flag04 获得密码
登录flag04用户获取flag
![](img/level04.png)

### level05
steal-key

ls -a查看隐藏文件,将文件拷贝到home里,解压缩,ssh登录
![](img/level05.png)

### level06
crack-password

在passwd中找到flag06密码,用john破解,得到密码ftc,远程登录
vi /etc/passwd
john hash001(复制密码到该文件中)
![](img/level06.png)