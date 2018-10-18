import urllib.request
import ssl

with urllib.request.urlopen('https://auth.sz.gmcc.net/dana-na/auth/url_default/welcome.cgi/') as response:
    html = response.read()
    print(html)
    print(response.geturl())
    print(response.info())

#localfilename,headers = urllib.request.urlretrieve('http://ioffice.sz.gmcc.net')

#print(localfilename)
#print(headers)
