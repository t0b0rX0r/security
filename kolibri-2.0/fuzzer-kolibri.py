#!/usr/bin/env python
#**********************************************
#For educational purposes ONLY!
#Author: T0b0rX0r
#Twitter:@T0b0rX0r
#Source: https://github.com/t0b0rX0r
#Application: Kolibri-2.0
#Exploit: SEH on GET
#KeyWords:SEH, boofuzz, long jump, badchar in address
#Fuzzed: 
# Designed for use with boofuzz v0.0.8
#**********************************************

from boofuzz import *

def banner(sock):
	sock.recv(1024)



def main():
    SLEEP_TIME=0
    SESSION_FILENAME="kolibri-3"
    TIMEOUT=5
    CRASH_THRESHOLD= 4

    """
    This example is a very simple FTP fuzzer. It uses no process monitory
    (procmon) and assumes that the FTP server is already running.
    """
#
    session = Session(
      session_filename=SESSION_FILENAME,sleep_time=SLEEP_TIME,crash_threshold=CRASH_THRESHOLD,target=Target(
            connection=SocketConnection("192.168.1.178", 8080, proto='tcp')))
#**********************************************
# HTTP GET CONNECTION AS SEEN FROM WIRESHARK...for reference in crafting crash
#GET / HTTP/1.1
#Host: 192.168.1.178:8080
#User-Agent: Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
#Accept-Language: en-US,en;q=0.5
#Accept-Encoding: gzip, deflate
#Connection: keep-alive
#Upgrade-Insecure-Requests: 1
#**********************************************

    s_initialize("get")
    s_static("GET ")
    #s_delim(" ")
    s_string("/ HTTP/1.1")
    s_static("\r\n")
    s_static("Host:")
    s_delim(" ")
    s_string("192.168.1.178:8080")
    s_static("\r\n")
    s_static("User-Agent:")
    s_delim(" ")
    s_string("Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0")
    s_static("\r\n")
    s_static("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    s_static("\r\n")
    s_static("Accept-Language: en-US,en;q=0.5")
    s_static("\r\n")
    s_static("Accept-Encoding: gzip, deflate")
    s_static("\r\n")
    s_static("Connection: keep-alive")
    s_static("\r\n")
    s_static("Upgrade-Insecure-Requests: 1")
    s_static("\r\n\r\n")
#    s_delim(" ")
 #   s_string("0")
  #  s_static("\n")

    

    session.connect(s_get("get"))


    session.fuzz()


if __name__ == "__main__":
    main()
