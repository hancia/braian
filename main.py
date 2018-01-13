import requests

query={
    'sort':'pushed',
    'type':'owner',
}
message="sos"
r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/da417be9-5a0f-4e02-972a-d16c59ee77f8?subscription-key=855fe00606ef48ecb4dafc6a30b92845&verbose=true&timezoneOffset=0&q='+message)
print(r.json())
