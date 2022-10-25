# docker-api-countries-pyflask

Docker - simple API returning a static list of five countries; implemented 
using python flask.

## Prerequisite

- Python environment 
  - Note: linux (Ubuntu) comes with python pre-installed; for example,
    the following linux runs on Windows WSL
```
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.4 LTS
Release:        20.04
Codename:       focal

$ python --version
Python 3.8.10

$ pip --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```
  - Note: one option for running linux on the Windows computer is to use WSL; 
    see [Install Linux on Windows with WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

- Docker Engine - see [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

## Setup

- Clone this repo


## Develop & Test

**NOTE:** this repo contains codes for building the docker image; but the image
has been built and deployed to [Docker Hub](https://hub.docker.com/repository/docker/gabepublic/api-countries-pyflask).

There is no need to rebuild the docker image unless, you plan to modify the 
code, or deploy to your own docker image repo.

Use the following step-by-step instructions to: test outside docker container, 
rebuild the docker image, and test it locally.

- Run outside the docker container
```
$ cd [projects-dir]/docker-api-countries-pyflask
$ virtualenv ./.venv
$ source .venv/bin/activate
(.venv) $ cd [projects-dir]/docker-api-countries-pyflask/flaskapp
(.venv) $ pip install -r requirements.txt
Successfully installed Flask-2.0.3 Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.2 certifi-2022.6.15 charset-normalizer-2.0.12 click-8.1.3 idna-3.3 itsdangerous-2.1.2 requests-2.27.1 urllib3-1.26.12

(.venv) $ python app.py
loading country data...
API Port:  5000
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.31.53.207:5000
Press CTRL+C to quit
```

- Test outside the docker container
```
$ curl http://127.0.0.1:5000/
{"msg":"URIs: /countries /debug /error","status":"success"}

$ curl http://127.0.0.1:5000/countries
{"countries":[{"capital":"Amsterdam","code":"NL","currency":"EUR","emoji":"\ud83c\uddf3\ud83c\uddf1","name":"Netherlands","native":"Nederland","phone":"31"},{"capital":"Washington D.C.","code":"US","currency":"USD,USN,USS","emoji":"\ud83c\uddfa\ud83c\uddf8","name":"United States","native":"United States","phone":"1"},{"capital":"Ottawa","code":"CA","currency":"CAD","emoji":"\ud83c\udde8\ud83c\udde6","name":"Canada","native":"Canada","phone":"1"},{"capital":"London","code":"GB","currency":"GBP","emoji":"\ud83c\uddec\ud83c\udde7","name":"United Kingdom","native":"United Kingdom","phone":"44"},{"capital":"Jakarta","code":"ID","currency":"IDR","emoji":"\ud83c\uddee\ud83c\udde9","name":"Indonesia","native":"Indonesia","phone":"62"}],"msg":"Found 5 countries","status":"success"}
```

- Build the docker image
```
$ cd [projects-dir]/docker-api-countries-pyflask
$ chmod +x 01-build-image.sh
$ ./01-build-image.sh
[...]
Successfully tagged gabepublic/api-countries-pyflask:0.1.0-linux-amd64

$ docker images
REPOSITORY                                      TAG                 IMAGE ID       CREATED         SIZE
gabepublic/api-countries-pyflask                0.1.0-linux-amd64   a10499da2df9   4 seconds ago   497MB
$
```

- Run the docker application
```
$ cd <project_folder>/docker-api-countries-pyflask
$ chmod +x 02-run.sh
$ ./02-run.sh
eebb33a4801c36d30306d8f45e583f8b0a911ab3[...]

$ docker ps
CONTAINER ID   IMAGE                                                COMMAND              CREATED         STATUS         PORTS                                   NAMES
bbd8ff686d3c   gabepublic/api-countries-pyflask:0.1.0-linux-amd64   "python3 ./app.py"   8 seconds ago   Up 6 seconds   0.0.0.0:80->5000/tcp, :::80->5000/tcp   api-countries
```

- - Test the docker container
```
$ curl http://127.0.0.1:80/
{"msg":"URIs: /countries /debug /error","status":"success"}

$ curl http://127.0.0.1:80/countries
{"countries":[{"capital":"Amsterdam","code":"NL","currency":"EUR","emoji":"\ud83c\uddf3\ud83c\uddf1","name":"Netherlands","native":"Nederland","phone":"31"},{"capital":"Washington D.C.","code":"US","currency":"USD,USN,USS","emoji":"\ud83c\uddfa\ud83c\uddf8","name":"United States","native":"United States","phone":"1"},{"capital":"Ottawa","code":"CA","currency":"CAD","emoji":"\ud83c\udde8\ud83c\udde6","name":"Canada","native":"Canada","phone":"1"},{"capital":"London","code":"GB","currency":"GBP","emoji":"\ud83c\uddec\ud83c\udde7","name":"United Kingdom","native":"United Kingdom","phone":"44"},{"capital":"Jakarta","code":"ID","currency":"IDR","emoji":"\ud83c\uddee\ud83c\udde9","name":"Indonesia","native":"Indonesia","phone":"62"}],"msg":"Found 5 countries","status":"success"}
```

- Stop the docker application
```
$ docker stop <CONTAINER-ID>

$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

- Deploy to Docker Hub
```
$ docker login
#provide Docker Hub id and password
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

$ docker push gabepublic/api-countries-pyflask:0.1.0-linux-amd64
[...]
0.1.0-linux-amd64: digest: sha256:d7848521e8636ef80fc931abe7f42f858ea75474dca41d5128f803a6226c67fa size: 1372

$ docker logout
```


## CLEANUP

- Delete docker image
```
$ docker image rm <IMAGE-ID>
```



