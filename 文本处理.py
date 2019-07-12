#!/usr/bin/python2.6
import re,datetime
file_name='/home/alzhong/logs/qtat1/R2860.01.13/sim-applycommitrollback-bld1.log'
file=open(file_name,'r')
acnum=[];time_res=[];lnum=0
def trans_time(time):
    t1=datetime.datetime.strptime(time,'%y/%m/%d %H:%M:%S')
    return t1
for (num,line) in enumerate(file):

    if(re.search(r'^(.*)BEGINNING SIM PROCEDURE(.*)$',line)):
        m=re.search(r'^(.*)BEGINNING SIM PROCEDURE(.*)$',line)
        print 'Step %d:'%(lnum), m.group(0);lnum+=1
        acnum.append(trans_time(line[0:17]))
    elif(re.search(r'^(.*)CP_W(.*)$', line)):
        m=re.search(r'^(.*)CP_W(.*)$', line)
        print 'Step %d:'%(lnum), m.group(0);lnum+=1
        acnum.append(trans_time(line[0:17]))
    elif(re.search(r"^(.*)VERIFY_S(.*)$", line)):
        m=re.search(r"^(.*)VERIFY_S(.*)$", line)
        print 'Step %d:'%(lnum), m.group(0);lnum+=1
        acnum.append(trans_time(line[0:17]))
    elif(re.search(r"^(.*)--action commit(.*)$",line)):
        m=re.search(r"^(.*)--action commit(.*)$",line)
        print 'Step %d:'%(lnum), m.group(0);lnum+=1
        acnum.append(trans_time(line[0:17]))
    elif(re.search(r"^(.*)COMPLETED SIM PROCEDURE(.*)$",line)):
        m=re.search(r"^(.*)COMPLETED SIM PROCEDURE(.*)$",line)
        print 'Step %d:'%(lnum), m.group(0);lnum+=1
        acnum.append(trans_time(line[0:17]))
    elif(re.search(r"^(.*)RESUMING SIM PROCEDURE(.*)$",line)):
        m=re.search(r"^(.*)RESUMING SIM PROCEDURE(.*)$",line)
        print 'Step %d:'%(lnum), m.group(0);lnum+=1
        acnum.append(trans_time(line[0:17]))

file.close()
if(re.search(r"^(.*)backout(.*)$",file_name)):
    time_res.append((acnum[2]-acnum[0]).seconds/60)
    time_res.append((acnum[4]-acnum[3]).seconds/60)
    time_res.append((acnum[6]-acnum[5]).seconds/60)
    time_res.append(((acnum[8]-acnum[7])+(acnum[10]-acnum[9])+(acnum[13]-acnum[11])).seconds/60)
    print "\n3). sim --proc update --action apply to \"CP_WARNING\" %s mins" %(time_res[0])
    print "4). sim --proc update --action resume to  \"VERIFY_SOFTWARE\" %s mins"%(time_res[1])
    print "5). sim --proc update --action resume to  \"COMMIT\" %s mins"%(time_res[2])
    print "8). Backout from RXX to RXX  %s mins"%(time_res[3])
elif(re.search(r"^(.*)rollback(.*)$",file_name)):
    time_res.append((acnum[2]-acnum[0]).seconds/60)
    time_res.append((acnum[4]-acnum[3]).seconds/60)
    time_res.append((acnum[6]-acnum[5]).seconds/60)
    time_res.append((acnum[8]-acnum[7]).seconds/60)
    time_res.append(((acnum[10]-acnum[9])+(acnum[12]-acnum[11])+(acnum[15]-acnum[13])).seconds/60)
    print "\n3). sim --proc update --action apply to \"CP_WARNING\" %s mins" %(time_res[0])
    print "4). sim --proc update --action resume to  \"VERIFY_SOFTWARE\" %s mins"%(time_res[1])
    print "5). sim --proc update --action resume to  \"COMMIT\" %s mins"%(time_res[2])
    print "6). sim --proc update --action commit to end of Patch %s mins"%(time_res[3])
    print "8). Rollback from RXX to RXX %s mins" %(time_res[4])
if __name__ == '__main__':
    pass
:q!
<lsslogin1-alzhong>/home/alzhong/tools: ls
simt
<lsslogin1-alzhong>/home/alzhong/tools: ./simt
Step 0: 14/06/16 12:31:32 BEGINNING SIM PROCEDURE 'update apply' type=hot ...
Step 1: 14/06/16 13:18:42 RESUMING SIM PROCEDURE 'update apply' type=hot ...
Step 2: 14/06/16 13:30:43 SIM0317 PAUSE_REQUEST: (PROCEDURE) [PAUSE(CP_WARNING): Use 'sim --proc update --action resume' to continue...] (update:1435)
Step 3: 14/06/16 13:43:40 RESUMING SIM PROCEDURE 'update apply' type=hot ...
Step 4: 14/06/16 13:47:49 SIM0343 PAUSE_REQUEST: (PROCEDURE) [PAUSE(VERIFY_SOFTWARE): Use 'sim --proc update --action resume' to continue...] (update:1634)
Step 5: 14/06/16 13:54:26 RESUMING SIM PROCEDURE 'update apply' type=hot ...
Step 6: 14/06/16 14:25:41 SIM0496 PAUSE_REQUEST: (COMMIT) [PAUSE(COMMIT): Use 'sim --proc update --action commit' to continue...] (update:2579)
Step 7: 14/06/16 14:41:51 RESUMING SIM PROCEDURE 'update commit' type=hot ...
Step 8: 14/06/16 15:18:34 COMPLETED SIM PROCEDURE 'update commit' type=hot
Step 9: 14/06/16 15:31:35 BEGINNING SIM PROCEDURE 'update rollback' type=hot level=9999 ...
Step 10: 14/06/16 15:47:34 SIM0091 PAUSE_REQUEST: (PROCEDURE) [PAUSE(CP_WARNING): Use 'sim --proc update --action resume' to continue...] (update_rlbk:421)
Step 11: 14/06/16 15:53:30 RESUMING SIM PROCEDURE 'update rollback' type=hot level=9999 ...
Step 12: 14/06/16 16:02:03 SIM0135 PAUSE_REQUEST: (PROCEDURE) [PAUSE(VERIFY_SOFTWARE): Use 'sim --proc update --action resume' to continue...] (update_rlbk:564)
Step 13: 14/06/16 16:04:22 RESUMING SIM PROCEDURE 'update rollback' type=hot level=9999 ...
Step 14: 14/06/16 16:09:42 RESUMING SIM PROCEDURE 'update rollback' type=hot level=9999 ...
Step 15: 14/06/16 16:26:56 COMPLETED SIM PROCEDURE 'update rollback' type=hot level=9999

3). sim --proc update --action apply to "CP_WARNING" 59 mins
4). sim --proc update --action resume to  "VERIFY_SOFTWARE" 4 mins
5). sim --proc update --action resume to  "COMMIT" 31 mins
6). sim --proc update --action commit to end of Patch 36 mins
8). Rollback from RXX to RXX 47 mins
--------------------- 
作者：Allen_Zhong 
来源：CSDN 
原文：https://blog.csdn.net/zhongyu211/article/details/34423213 
版权声明：本文为博主原创文章，转载请附上博文链接！