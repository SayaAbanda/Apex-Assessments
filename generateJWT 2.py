import jwt
import datetime

# Defining key details
key = {
    'username': 'iws-test',
    'entity': 'apex',
    'sharedSecret': '1234567890'
}

# Defining payload
payload = {
    'username': key['username'],
    'entity': key['entity'],
    'datetime': datetime.datetime.utcnow().isoformat()
}

# Defining secret
secret = key['sharedSecret']

# Encode the payload using SHA-512
token = jwt.encode(payload, secret, algorithm='HS512')

print(token)

# generated token = eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Iml3cy10ZXN0IiwiZW50aXR5IjoiYXBleCIsImRhdGV0aW1lIjoiMjAyNC0wNi0wMVQxODo1Mjo0Mi4wMzI4MjIifQ.TY8e5T8bvMx7km9QYJrODn9DydCd8Ka1BCLM5nUvBISfMSwy0NslgdFQsYREhuWzmoMIFRp9fc-HcRKqvcisFg