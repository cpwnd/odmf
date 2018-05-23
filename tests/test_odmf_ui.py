# Basic tests covering calls and login behaviour

import requests

# schiwngbach installation
url = 'http://fb09-pasig.umwelt.uni-giessen.de:8081'
site = lambda s: url + s

# TODO: login behaviour with selenium or splinter
pages = ['/map', '/login', '/wiki/publications', '/wiki']

error = False
errors = ""

for page in pages:
    response = requests.request('GET', site(page))
    if response.status_code is not 200:
        msg = "Failed " + page + " with status " + repr(response.status_code)
        print(msg)
        error = True
        errors += "\t* " + msg + "\n"
    else:
        print("Page\t" + page + " ... Done [with " + str((len(response.content) * 32)) + " bytes]")

if error:
    raise RuntimeError("Failing tests: \n" + errors)
