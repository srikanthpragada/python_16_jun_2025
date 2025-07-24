import requests

userid = input("Enter github userid :")
response = requests.get(f"https://api.github.com/users/{userid}/repos")
if response.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

repos = response.json()   # Convert Array of JSON  objects to list[dict]

for repo in repos:
    print(repo['name'])
    print(repo['description'])
    print('-' * 50)
