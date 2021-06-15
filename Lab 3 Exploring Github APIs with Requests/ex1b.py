#Name:Parackrama G.T.W.
#E number:E/16/267

import requests

#1.b
#user name =wsna524

print("1.b")
response = requests.get("https://api.github.com/users/")


print(response)
print("\n")
print('printing response.text')
print(response.text)
print("\n")
print('printing response.headers')
print(requests.head("https://api.github.com//users/").headers)

print("\n")
