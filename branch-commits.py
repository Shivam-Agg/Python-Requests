import requests

username = input("Enter username - ")
repo = input("Enter repository name - ")

#LISTING ALL BRANCHES
response = requests.get('https://api.github.com/repos/' + username + '/' + repo + '/branches')
json_response = response.json()
print(f"{repo} has following branches - ")
for branch in json_response:
    print(branch['name'])

#LISTING ALL COMMITS FOR A GIVEN BRANCH
branch = input('Enter the branch name - ')
response2 = requests.get('https://api.github.com/repos/' + username + '/' + repo + '/commits')
json_response_2 = response.json()
for commit in json_response_2:
    if commit['name']==branch:
        url = commit['commit']['url']
        while True:
            url_response = requests.get(url).json()
            print("\n-----------------\n")
            print(f"SHA : {url_response['sha']} \nAuthor : {url_response['commit']['author']['name']} \nMessage : {url_response['commit']['message']}")
            if len(url_response['parents'])==0:
                break
            url = url_response['parents'][0]['url']
