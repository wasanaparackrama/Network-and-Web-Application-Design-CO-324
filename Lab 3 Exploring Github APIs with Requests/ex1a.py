#Name:Parackrama G.T.W.
#E number:E/16/267


import requests

#1.a
print("1.a")
response = requests.get("https://api.github.com")

print(response)
print("\n")
print('printing response.text')
print(response.text)
print("\n")
print('printing response.headers')
print(requests.head("https://api.github.com").headers)

print("\n")