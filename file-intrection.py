import requests

url = "http://testphp.vulnweb.com/admin/create.sql"
respanse = requests.get(url)

if respanse.status_code==200:
    with open(r"D:\Cyber Security\web-scrapping\file-intrection\\dow.sql","wb") as f:
        f.write(respanse.content)
    print("ok")
else : 
    print("error")        
