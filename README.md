# Test Assignment
## Docker + Python3 + Selenium + Firefox

### Quick Start
Build the docker image:

```
docker build -t testassignment .
```

Run the container:
```
docker run testassignment
```

The container is based on the official python image, with added packeges of selenium, installed Firefox-ESR browser, and added geckodriver. 
Upon running, the python based tests are executed using the geckodriver in headless mode and reported to the command line. 

Cause, the container is linux based, the following commands should be ran for Apple Silicon devices:
```
docker build --platform=linux/amd64 -t testassignment .
docker run --platform=linux/amd64 testassignment
```

#### Test Assigment text:
```
Argyle test assignment

Write small&quick test that enters ’https://console.argyle.com/’ 
and fill email field with ‘test@test.com’ and password with ‘Password123!@#’ 
and check for ‘Login Error message’

1. The python(preferrable) or java 
2. Docker
```
