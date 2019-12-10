from pwn import *
sh = process("./ex2")
sh.sendline("ATrinityroKLMNOPQRS\notcdefghijklmno\n")
sh.interactive()