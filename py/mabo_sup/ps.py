import psutil

#print psutil.pids()

print psutil.boot_time()

x =  psutil.net_connections()
v = 0
print psutil.cpu_times()

for i in x:
    print i.pid, i.laddr,
    v = i.pid
    #break;


    try:
        p = psutil.Process(v)
        print  p.name()#, p.open_files()
    except:
        pass