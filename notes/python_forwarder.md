The script is located [here](../container/proxy.py)

# Imported components

- Flask framework - Expose http endpoints
- requests - Flexible library for http consumes

# Why is this script needed ?

Our Accenture's laptops have port 80 and 443 blocked by the organization. Looking in the [repository](https://github.com/harvard-itsecurity/docker-misp) the readme says:

>We always recommend building your own Docker MISP image using our "build.sh" script. This allows you to change all the passwords and customize a few config options.

Between theese option there's the FQDN and in the dockerfile is specified the port.

With this in mind i tried to change those values, build the container and run. The result was the web app works but the api  the *API_KEY* is binded to *localhost:443* and this cause unauthorized issue because the host that sending the request is *localhost:8443* in my case.

# The architecture

![](./res/python_forwarder_1.svg)

The forwarder expose a generic endpoint using flask, takes the uri, headers and body, string replace `localhost:8080` with `localhost` and send the http request using requests.

The response get string replace `localhost` with `localhost:8080` and put them in the response for the client

To makes everithing work some particulare scenarios are handled:

- **Binary resource (images, videos, etc)**
  For those the string replace is in a try-except block, because them are not decodable as utf-8 string. The except part just return the body as it comes.
- **The uri** `/css/bootstrap.css.map`
  Looks like during development is easy that ides or devtool create those resources that ends with `.map`. The code add location header to `localhost:8080` to just redirect to the index page