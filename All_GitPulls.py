import requests

response=requests.get("http://api.github.com/repos/kubernetes/kubernetes/pulls")
output=response.json()

for list in range(len(output)):
    print(f'For pull request {list} the id is: {output[list]["id"]}')