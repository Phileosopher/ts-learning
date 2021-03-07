import subprocess

n = 11111122
m = 121
data = bytes (str(n)+ ' '+str(m), 'utf-8')
while True:
    p = subprocess.Popen('gcd.exe',
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    s = str(p.stdout.readline())
    print (s)
    if s == "b'1'":
        print ("Numbers are ", n, m)
        break
    m = m + 1
    data = bytes (str(n)+ ' '+str(m), 'utf-8')
print ("------------------------------------")

