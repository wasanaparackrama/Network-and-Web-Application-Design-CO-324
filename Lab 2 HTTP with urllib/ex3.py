#Author:E/16/267
from urllib import request
import requests

import json
from urllib import parse
from typing import List

#a
def ddg_query(url: str, nr_results: int) -> List[str]:


    query=parse.quote(url)
    url="https://www.duckduckgo.com/?q="+query+"&format=json&pretty=1"
    response=request.urlopen(url)
    body=response.read()
    #parsing json body
    data=json.loads(body.decode("utf-8"))
    details=[]

    for i in data["Results"]:
        details.append(i["FirstURL"])
    for i in data["RelatedTopics"]:
        details.append(i["FirstURL"])

    return details[0:nr_results]

#b
def spider_metadata(urls: List[str]) -> List[List]:
    '''Returns the HTTP headers for each of the URLs in the list.'''
    headers = []
    for k in urls:
        response = request.urlopen(k)
        header = response.headers.items()
        headers.append(header)
    return(headers)

#c
def spider_metadata_c(urls: List[str]) -> List[List]:
    '''Returns the HTTP headers for each of the URLs in the list.'''
    h = []
    #using head method when we need only headers
    for k in urls:
        h.append((requests.head(k)).headers)
    return h


print("3.a")
print(ddg_query("University of Peradeniya", 3))
print("\n")
# to print urls which we get from function ddg_query
#urls=[]
#urls=ddg_query("University of Peradeniya", 3)
#print(spider_metadata(urls))

print("3.b")
print(spider_metadata(['http://www.pdn.ac.lk','https://duckduckgo.com/c/University_of_Peradeniya'] ))
print("\n")
print("3.c")
print(spider_metadata_c(['http://www.pdn.ac.lk','https://duckduckgo.com/c/University_of_Peradeniya'] ))
