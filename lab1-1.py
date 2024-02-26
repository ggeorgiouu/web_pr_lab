#zhtaw ap ton xristi URL kai epistrefw headers,psaxnw ton server kai ta cookies
import requests
import re

j=1

url=input('Give me a URL:')

if not url.startswith("http://"):
    url="http://"+url
    
r=requests.get(url)
header=r.headers
print("Website headers are:\n",header)

if 'Server' in header:
    print('\nServer used->',header.get('Server'))
else:
    print('No server detected')

if 'Set-Cookie' in header:
    print('\nUsing Cookies')
    cookies=header.get('Set-Cookie')
    cookiename=r.cookies
    for cookie in r.cookies:
        print('Cookie ',j, 'name->',cookie.name)
        j=j+1
    mylist=re.split('=|;',cookies)
    j=1
    for i in range(len(mylist)):
        if mylist[i]==' Expires' or mylist[i]==' expires':
            print('Cookie',j,'Expires->',mylist[i+1])
            j=j+1
else:
    print('It is not using Cookies')
        
        
    

    
        
    
    
    





