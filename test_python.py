import os
import subprocess
print "HAi I Am here"
var = os.popen('cot install-helpers').read()
print var

var = os.popen('cot install-helpers --verify-only').read()
print var
