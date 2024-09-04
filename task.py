#put 
import requests

url = 'https://httpbin.org/put'

data ={
    'name':'Purva',
    'id': 123
}

response = requests.put(url,json=data)
print(response.status_code)

print("json.response=",response.json())



#patch

import requests

url = 'https://httpbin.org/patch'

data ={
    'name':'Purva ganeshkar',
    'pswd': 112233
}

response = requests.patch(url,json=data)

print ("response status:",response.status_code)

print("json resq:",response.json())


#delete

import requests
url = 'https://httpbin.org/delete'

data ={
    'pswd':112233
}


response = requests.delete(url,json=data)

print("status code:",response.status_code)

print("response:", response.json())





