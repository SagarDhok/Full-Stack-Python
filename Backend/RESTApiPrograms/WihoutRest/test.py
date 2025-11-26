import requests
# BASE_URL = 'http://127.0.0.1:8000/'
# END_POINT = 'apijson2'
# resp = requests.get(BASE_URL + END_POINT)
# data = resp.json()
# print('Data from django application')
# print('*'*30)
# print('Employee Number:',data['eno'])
# print('Employee Name:',data['ename'])
# print('Employee Salary:',data['esal'])
# print('Employee Address:',data['eaddr'])

# import requests
# BASE_URL = 'http://127.0.0.1:8000/'
# END_POINT = 'apijsoncbv/'
# resp = requests.get(BASE_URL + END_POINT)
# data = resp.json()
# print(data)


# import requests
# BASE_URL = 'http://127.0.0.1:8000/'
# END_POINT = 'apijsoncbv/'
# resp = requests.delete(BASE_URL + END_POINT)
# data = resp.json()
# print(data)

# import requests
# BASE_URL = 'http://127.0.0.1:8000/'
# END_POINT = 'apijsoncbv/'
# resp = requests.put(BASE_URL + END_POINT)
# data = resp.json()
# print(data)


import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apijsoncbv/'
resp = requests.post(BASE_URL + END_POINT)
data = resp.json()
print(data)


