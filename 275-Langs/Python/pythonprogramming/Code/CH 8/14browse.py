import webbrowser
f = open ("other.html")
html = False
while True:
    s = f.readline()
    s = s.strip()
    s = s.lower()
    k = (s.find("doctype"))
    if k>0:
        kk = s.find("html")
        if kk >= k+7:
            html = True
            break
    else:
        k = s.find("html")
        if k>0 and s[k-1] == "<":
            html = True
            break
    if len(s) > 0:
        html = False
        break

if html:
    webbrowser.open_new_tab('other.html')
else:
    print ("This is not an HTML file.")