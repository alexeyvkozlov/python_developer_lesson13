#~ USAGE
# cd c:\python_developer
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd c:\python_developer\lesson_12
# cd d:\python_developer\lesson_12
#~~~~~~~~~~~~~~~~~~~~~~~~
# python hh_request.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from pprint import pprint
from requests import get

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url = 'https://api.hh.ru/vacancies'
params = {'text': 'python'}
res = get(url, params=params).json()
print(res['found'])
pprint(res['items'])