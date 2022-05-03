import requests

# res = requests.get('http://127.0.0.1:3000/api/courses/1')
# print(res.json())

# res = requests.delete('http://127.0.0.1:3000/api/courses/1')
# print(res.json())

# res = requests.post('http://127.0.0.1:3000/api/courses/3', json={"name": "JS", "videos": 5})
# res = requests.post('http://127.0.0.1:3000/api/courses/4', {"name": "php", "videos": 8})

res = requests.put('http://127.0.0.1:3000/api/courses/3', json={"name": "JS", "videos": 19})


print(res.json())