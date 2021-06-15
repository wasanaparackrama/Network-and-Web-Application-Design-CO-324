#Name:Parackrama G.T.W.
#E number:E/16/267
#part 2)a
import requests
from typing import List, Tuple

# function to return the list sorted in descending order of stars of repos of members
def github_superstars(organization:str)-> List[Tuple]:

    
	url="https://api.github.com/orgs/"+organization+"/members"
	# starting the session
	with requests.Session() as session:
		session.headers['Authorization'] = 'token  '
        
        # requesting the url
		response = session.get(url)
		data_json_1 = response.json()
		details=[]
	#get the members
		for i in data_json_1:
			details.append(i["login"])
    
	#print(details)
	members = list() 
	members = data_json_1
	maximum_repos = list()  
	
         
	for m in members :
		repo_list = list() 
		member_name = m['login'] 
		mem_repo_url = m['repos_url'] 
		
		url_repo=mem_repo_url+"?page=l&per_page=68"
		response2 = session.get(url_repo)
		stars=0
		
		data_2 = response2.json()
		
        
		for j in data_2:
			url2 = j['url']
			#calling mem_repo_url	
			response3 = session.get(url2)
			data_3 = response3.json()
			
            
			for repo in data_3:
				stars = data_3['stargazers_count']   
			repo_list.append((url2, stars))  
            
		repos_sorted = sorted(repo_list, key = lambda p: p[1], reverse = True) 
		
		
		maximum_repos.append(repos_sorted[0])
		maximum_sortedrepos=sorted(maximum_repos, key = lambda p: p[1], reverse = True)
#Return the list sorted in descending order of stars.        
	return  maximum_sortedrepos
    
# calling function github_superstars for organization 'cepdnaclk'
#print(github_superstars('cepdnaclk'))


