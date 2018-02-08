import subprocess
import os
subnet = "192.168.1."

while True:
    if subnet == '':
        break

print "Beginning scan of: ", subnet, "x"

with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 256):
                ipList = []
                ipList.append(subnet)

                quad = "{0}".format(n)
                ipList.append(quad)
                s = ''.join(ipList)
                #print s
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", s],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print s, "inactive"
                else:
                        print s, "active"
