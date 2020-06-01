import requests
from getpass import getpass

#TASK - 1
username = input("Enter your Username - ")
response = requests.get('https://api.github.com/user/repos', auth=(username, getpass()))
json_response = response.json()
for repo in json_response:
    print(repo['name'])

print("\n--------------------------\n")
#TASK - 2

username2 = input("Enter your friend's username - ")
response = requests.get('https://api.github.com/users/' + username2 + '/repos')
json_response = response.json()

for repo in json_response:
    print(repo['name'])


