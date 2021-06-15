#Name:Parackrama G.T.W.
#E number:E/16/267
#part 2)b
from ex2a import *


    
# list the output function github_superstars
winner = list()

# calling function github_superstars 
winner = github_superstars('cepdnaclk')

# print the winner
print("Winner repo is")
print(winner[0])

# watch the repo of winner
with requests.Session() as session:
    session.headers["Authorization"] = 'token  fd79a1a9dd3cc14ccbb399641f24bbedbb60598f'
url_4=winner[0][0]+"/subscription"
session.put(url_4)


