#  Nginx Concept Examples

Configuration examples created in order to use different concepts provided by Nginx


## Installation

1. Install nginx

2. Create virtual environment and load dependencies
    
        pipenv --python 3.7
	     pipenv install
	     pipenv shell
	  

3. Run bottle server 
    
    `python3 run.py` 
    
    This starts a server on 8080, check `http://localhost:8080/say-hello-to/user`

4. Every subfolder has `nginx.conf` configuration file. Activate separate nginx configuration with 

	`nginx -c /path-to-working-dir/[subdirectory]/nginx.conf`

## Example cases
Every example requires reloading the nginx.conf from subdirectory

### 1. Create docker with nginx and index.html 

Run 

    start.sh

and then check 

    http://localhost:1234

### 2. Creating docker container with nginx

Run 

    start.sh
    
and then check 

	http://localhost:1234

### 3. Proxy from /api/headers to /headers

Adds special headers in response.

	http://localhost/api/headers


### 4. Proxy to bottle /say-hello-to/user

Check 

	http://localhost/say-hello-to-user

### 5. Proxy from /api/search to /v1 with provided path 

Check

	http://localhost/api/search/v1/some-random-path


