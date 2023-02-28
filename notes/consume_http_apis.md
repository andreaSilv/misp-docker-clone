MISP API documentation [here](https://www.misp-project.org/openapi) or if you want check it from your started container [here](https://localhost:8443/api/openapi)

>**IMPORTANT** - Without something in the middle that would replace the port
>you can only fire request inside the container at localhost

# Requirements

- API_KEY ([How to create API key](./create_api_key.md))

# Headers

An example of header set could be
```
Authorization: <YOUR_API_KEY> 
Accept: application/json
Content-type: application/json
```