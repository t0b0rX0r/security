#!/usr/bin/env python
# Designed for use with boofuzz v0.0.8
from boofuzz import *

def banner(sock):
	sock.recv(1024)



def main():
    SLEEP_TIME=0.5
    SESSION_FILENAME="vulnserver-gter"
    TIMEOUT=5
    CRASH_THRESHOLD= 4

    """
    This example is a very simple FTP fuzzer. It uses no process monitory
    (procmon) and assumes that the FTP server is already running.
    """
    session = Session(
        session_filename=SESSION_FILENAME,sleep_time=SLEEP_TIME,crash_threshold=CRASH_THRESHOLD,target=Target(
            connection=SocketConnection("192.168.1.179", 9999, proto='tcp')))
 
#    HELP
#STATS [stat_value]
#RTIME [rtime_value]
#LTIME [ltime_value]
#SRUN [srun_value]
#TRUN [trun_value]
#GMON [gmon_value]
#GDOG [gdog_value]
#KSTET [kstet_value]
#GTER [gter_value]
#HTER [hter_value]
#LTER [lter_value]
#KSTAN [lstan_value]

    s_initialize("stats")
    s_static("STATS")
    s_delim(" ")
    s_string("blah")
    s_static("\r\n")

    s_initialize("gter")
    s_static("GTER")
    s_delim(" ")
    s_string("blah")
    s_static("\r\n")

    s_initialize("rtime")
    s_static("RTIME")
    s_delim(" ")
    s_string("blah")
    s_static("\r\n")

    s_initialize("ltime")
    s_static("LTIME")
    s_delim(" ")
    s_string("0")
    s_static("\n")
   
    s_initialize("trun")
    s_static("TRUN")
    s_delim(" ")
    s_string("0")
    s_static("\n")

    s_initialize("gmon")
    s_static("GMON")
    s_delim(" ")
    s_string("0")
    s_static("\n")

    s_initialize("gdog")
    s_static("GDOG")
    s_delim(" ")
    s_string("0")
    s_static("\n")


    s_initialize("kstet")
    s_static("KSTET")
    s_delim(" ")
    s_string("0")
    s_static("\n")

    s_initialize("hter")
    s_static("HTER")
    s_delim(" ")
    s_string("0")
    s_static("\n")

    s_initialize("srun")
    s_static("SRUN")
    s_delim(" ")
    s_string("0")
    s_static("\n")
    s_initialize("kstan")
    s_static("KSTAN")
    s_delim(" ")
    s_string("0")
    s_static("\n")
    s_initialize("lter")
    s_static("LTER")
    s_delim(" ")
    s_string("0")
    s_static("\n")
    session.pre_send=banner
    session.connect(s_get("gter"))
    #session.connect(s_get("rtime"))
    #session.connect(s_get("ltime"))
#    session.connect(s_get("stats"))
 #   session.connect(s_get("trun"))
    #session.connect(s_get("gmon"))
    #session.connect(s_get("kstet"))
    #session.connect(s_get("hter"))
    #session.connect(s_get("gmon"))
    #session.connect(s_get("srun"))
    #session.connect(s_get("kstan"))
    #session.connect(s_get("lter"))
    #session.connect(s_get("user"), s_get("pass"))
    #session.connect(s_get("list"))
    #session.connect( s_get("pass"),s_get("list"))
    #session.connect(s_get("pass"), s_get("stor"))
    #session.connect(s_get("pass"), s_get("retr"))

    session.fuzz()


if __name__ == "__main__":
    main()
