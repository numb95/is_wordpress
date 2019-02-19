<!--
 Copyright (c) 2019 amirhossein
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->
# is_wordpress
A simple (or useless) Program to check if a website is based on wordpress or not and if it's on wordpress which version does it use.

# Installing 
``` pip install is-wordpress```

# Usage 
```
usage: main.py [-h] url

Check if selected website is based on wordpress or not.It also show the
wordpress version.

positional arguments:
  url         URL to check the website.

optional arguments:
  -h, --help  show this help message and exit
```

## Docker usage
Build docker image
```
$ docker build -t is_wordpress .
```
Now you can simply invoke `is_wordpress` by:
```
$ docker run --rm is_wordpress goodarzi.net
```

Or simply run it by **docker hub**
```
$ docker run theyahya/is_wordpress goodarzi.net
```
## Example
``` 
$ is_wordpress goodarzi.net
WordPress 4.9.8
```
# Contribution
Feel free to fork and fix problems. PRs are welcome. :heart:

# Issues
Use Issues section to report any problem.
