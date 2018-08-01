import os
import subprocess
print "HAi I Am here"
var = os.popen('cot install-helpers').read()
print var

var = os.popen('cot install-helpers --verify-only').read()
print var

loopn = os.popen("/sbin/losetup -f", "r").read().strip()
if(loopn):
    print loopn
else:
    print "Unable to Get the Free Loop Device" ;
