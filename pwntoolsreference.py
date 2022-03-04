from pwn import process

path = input("Full path: ")
args = input("Arguments: ")
process([path,args]).recvall()
