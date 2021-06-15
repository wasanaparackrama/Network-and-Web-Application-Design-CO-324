#Name:Parackrama G.T.W.
#E number:E/16/267

import json
import requests



#1)e
print('1).e')
with requests.Session()as session:
	session.headers['Authorization']='token  fd79a1a9dd3cc14ccbb399641f24bbedbb60598f '
	url='https://api.github.com/user/repos'
	#request body
	body={'name':'test3', 'description':'some test repo'}
	#create repository
	response=session.post(url,data=json.dumps(body))
	
	print(response.text)
print("\n")
print('status_code')
print(response.status_code)