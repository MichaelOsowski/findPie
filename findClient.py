import sys
import threading
from fpsupport import hostHostData
threads = []
print ('Starting Process')
for x in range(0, 1000):
    t = threading.Thread(target=hostHostData.hostInfo,args=(sys.argv[1], x))
    threads.append(t)
    t.start()


print('Process Complete')
exit(0)
