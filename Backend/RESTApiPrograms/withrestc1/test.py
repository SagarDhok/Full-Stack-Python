import requests,json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'



def delete_resource(id):
    data = {
        'id':id
    }
    resp = requests.delete(BASE_URL + END_POINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
delete_resource(2)


# def update_resource(id):
#     new_emp = {
#         'id':id,
#         'ename':'sunny',
#         'esal':20000,
#         'eaddr':'xxxxxxx'
#     }
#     resp = requests.put(BASE_URL + END_POINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(2)

# def create_resource(id= None):
#             new_emp = {
#                       'eno':105,
#                       'ename':'Pinny',
#                       'esal':18000,
#                        'eaddr':'Vja'

#             }
#             resp = requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
#             print(resp.status_code)
#             print(resp.json())

# create_resource()








