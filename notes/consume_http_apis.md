MISP API documentation [here](https://www.misp-project.org/openapi) or if you want check it from your started container [here](https://localhost:8443/api/openapi)

>**IMPORTANT** - Keep in mind that between browser and MISP server there's a python forwarder that string replace the hostname to make possible to ACN's laptop the execution

# Requirements

- API_KEY ([How to create API key](./create_api_key.md))

# Headers

An example of header set could be
```
Authorization: <YOUR_API_KEY> 
Accept: application/json
Content-type: application/json
```