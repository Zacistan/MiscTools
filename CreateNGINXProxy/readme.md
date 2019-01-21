# Usage
## Requirements
* Python 3
* Nginx
* Read and write access to the nginx sites directories

## Examples

Create a proxy configuration using the default nginx paths:
```shell
$ python3 ./create_nginx_proxy.py -p "test2.localhost.local" -u "127.0.0.1:8080"
```

Create a proxy configuration using custom nginx paths:
```shell
$ python3 python ./create_nginx_proxy.py -p "test.localhost.local" -u "http://127.0.0.1:8080/" -a "/etc/nginx/proxies-available" -e "/etc/nginx/proxies-enabled"
```

## Parameters
### Required
* -p : The hostname of the proxy.
* -u : The URL that will be proxied.
### Optional
* -a : The 'sites-available' nginx directory.
* -e : The 'sites-enabled' nginx directory.
* -t : The path to the template configuration file.