#Author:E/16/267

from urllib import request
#a
print("1.a")
response = request.urlopen("http://eng.pdn.ac.lk")
print("What is the response code you received?")
print(response.getcode())
#print('RESPONSE:', response)
print("\n")


#b
print("1.b")
header = response.headers.items()
print(header)
print("\n")
print('What is the web server and OS used to host this site?')
print('Server and Os    :', response.headers['Server'])
print("\n")

#c
print("1.c")
body = response.read()
print("The size of the response body")
print(len(body))
print("\n")

#d
print("1.d")
print("The Python type of the ‘body’ variable")
print(type(body))
response.close()
print("\n")


#f
print("1.f")
#response_2 = request.urlopen("http://eng.pdn.ac.lk/unknown")
#print('RESPONSE:', response_2)
print('For "http://eng.pdn.ac.lk/unknown" gives an error:HTTP Error 404: Not Found')


#response_4 = request.urlopen( "http://unknown.pdn.ac.lk")
#print('RESPONSE:', response_4)

print('For "http://eng.pdn.ac.lk/unknown" gives an error: URLError: <urlopen error [Errno 11001] getaddrinfo failed>')
print("\n")


#g
print("1.g")
response_5 = request.urlopen("https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D")
body_2 = response_5.read()
print(body_2)  #gives url data
print("\n")

response_3 = request.urlopen("https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D")
data = response_3.read().decode('utf-8')
print('BODY DATA    :')
print('---------')
print(data)
print("\n")

#h
print("1.h")
print("What difference do you see  if you call the method .decode(“utf-8”) on the body data received in (g) before printing it?")
response_6 = request.urlopen("https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D")
data_6 = response_6.read().decode('utf-8')
body_6 = response_6.read()
print(body_6)
