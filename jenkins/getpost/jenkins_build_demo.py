#incoding=utf-8
import requests
url = 'http://localhost:8080/job/check_python_version/build'
r = requests.get(url,data={},auth=('admin','111111b'))
print r.text