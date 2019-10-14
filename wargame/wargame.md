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
