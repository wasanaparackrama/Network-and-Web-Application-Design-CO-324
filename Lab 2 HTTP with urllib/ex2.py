#Author:E/16/267

from urllib import request
from urllib import parse

with request.urlopen("https://www.duckduckgo.com/?q=University+of+Peradeniya") as query:

    headers = query.headers.items()
    body = query.read()
    #“ & format = json & pretty = 1
#print(headers)
print(body.decode("utf-8"))
print("\n")

#i.Append the string “&format=json&pretty=1” to the search query
with request.urlopen("https://duckduckgo.com/?q=University+of+Peradeniya&ia=web&format=json&pretty=1") as query_2:

    headers_2 = query_2.headers.items()
    body_2 = query_2.read()

#print(headers_2)
print(body_2)
#print(body_2.decode("utf-8"))
print("\n")
print("i.'format=json&pretty=1' is gives text files, such as sourcecode, markup, and similar kinds of content.")
print("\n")


#j
print("J.Use request.urlopen to search for the phrase “Rocco's basilisk”.")
with request.urlopen("https://duckduckgo.com/?q=Rocco%27s+basilisk&t=hk&ia=web") as query_3:

    headers_3 = query_3.headers.items()
    body_3 = query_3.read()

#print(headers_3)
print(body_3)
#print(body_3.decode("utf-8"))
print("\n")



#l
print("l.How would you do a DDG search in Python for your name written in Tamil or Sinhala? Use this for Unicode input")
#to get sinhala url
query_3=parse.quote("වාසනා")
print("Name Unicode for search in python:")
print(query_3)
response_4=request.urlopen('https://duckduckgo.com/?q=query_3')
print(response_4.read().decode("utf-8"))