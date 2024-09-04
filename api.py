#put

import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

data = {
    'user_id':1,
    'id':1,
    'title':'Updated title',
    'body':'Updated body content'
}

response = requests.put(url,json=data)
print("status:",response.status_code)

print("put response body:",response.json())

#patch

import requests 

url = 'https://jsonplaceholder.typicode.com/posts/1'

data = {
   
    'title':'partially updated title'
}

response= requests.patch(url,json=data)
print("status code:",response.status_code)

print("status code:",response.status_code)
print("response body:",response.json())




#delete
url = 'https://jsonplaceholder.typicode.com/posts/1'


response = requests.delete(url)
print("status_code:",response.status_code)


if response.status_code==200:
    print("delete req successfull")

else:
    print("delete response body",response.text) 

    print(f"delete request error")   




