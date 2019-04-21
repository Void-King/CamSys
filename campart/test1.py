import subprocess
from subprocess import Popen, PIPE, STDOUT
cmd = 'python test.py'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
for line in iter(p.stdout.readline, b''):
    print (line)
p.stdout.close()
p.wait()