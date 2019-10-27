###  level02
attack-env-again

修改USER变量, export USER='`/bin/getflag01`'
![](img/level02.png)

### level03
attack-crontab

在writable.d下创建文件test，内容为`/bin/getflag03>/home/flag03/a.txt`
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

ls -a查看隐藏文件，将文件拷贝到home里，解压缩，ssh登录
![](img/level05.png)

### level06
crack-password

在passwd中找到flag06密码，用john破解，得到密码ftc，远程登录
vi /etc/passwd
john hash001(复制密码到该文件中)
![](img/level06.png)

### level07
cgi-vuln

在/home/flag07下找到index.cgi文件，并根据thpptd得知文件在8888端口
通过浏览器访问8888下的index.cgi文件
查询文件，得知需要Host参数，于是在后面加上?Host=127.0.0.1%26/bin/getflag07(其中%26位&的url加密格式)
![](img/level07.png)

### level08

analyze-packets

在flag08下找到数据包文件，先拷贝到level08下，再远程传送到本地，利用wireshark分析数据包
找到password后面的明文字符为：
backdoor+【del】+【del】+【del】+00R+m8+【del】+ate+【enter】
整合后，密码为`backd00Rmate`
登录后获得flag
![](img/level08.png)



