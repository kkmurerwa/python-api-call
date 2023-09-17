from urllib import request, parse
import json

url = 'https://api.thecatapi.com/v1/images/search'

# Add Params
params = {
    'limit' : 5,
    'page' : 1,
    'order' : 'Desc'
}

querystring = parse.urlencode(params)

# Call the UI
response = request.urlopen(url + '?' + querystring)
content = response.read()

# Decode to UTF-8
decoded = content.decode('utf-8')

# Parse to JSON
data = json.loads(content)

print(data[0])