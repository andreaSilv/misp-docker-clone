from flask import Flask, request, Response
import requests

app = Flask(__name__)

HOST="localhost:8080"
HOST_FORWARD="localhost"

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    # Forward the request to localhost:8080
    url = "https://" + HOST_FORWARD + f"/{path}"

    body = request.get_data().decode("utf-8").replace(HOST, HOST_FORWARD)

    headers = dict(request.headers)
    for i in headers:
        headers[i] = headers[i].replace(HOST, HOST_FORWARD)

    # Remove host header to avoid conflicts
    headers.pop('Host', None)
    # Send the request with the same method and data
    resp = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=body,
        cookies=request.cookies,
        verify=False,
        allow_redirects=False)
    # Return a response with the same status code, headers and content
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    
    for i in range(len(headers)):
        headers[i] = (headers[i][0].replace(HOST_FORWARD, HOST), headers[i][1].replace(HOST_FORWARD, HOST))

    responseBody = resp.content.decode("utf-8").replace(HOST_FORWARD, HOST)

    return Response(responseBody, resp.status_code, headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)