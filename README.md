### Note to take
Carousell now carries out image recognition and remembers that you have previously deleted a listing that looks similar.
Best to use a different image each time, saved as c1.jpg

Your Carousell account must be linked to Facebook due to Carousell's captcha blocking

## Selenium Python 
Basically you need your environment to be set up right to make this work

`python` -> 2.7 or above
`chromedriver` -> google how to install and make a symlink in the path to the file itself for python to run

### Pip modules required
`selenium`
`requests`

The above are the necessary files and to be safely installed in the env
Follow installation steps here: 
[Selenium Python Installation Guide](http://selenium-python.readthedocs.io/installation.html)

(Also recommended to install virtualenv)

### Login Credentials
These are not stored in the repo, saved in the terminal as environment variables
Before running the code do the following 
```
export FUSER=<email>
export FPASS=<pass>
```
#### Scripts
The codebase is split into two main scripts, the rest are for testing purposes
1. auto_post.py
2. pull_listing.py

**auto_post** pulls from csv file to fill up the listing details

**pull_listing**
 pulls data from the carousell listing url and stores the information in a csv file and saves the first photo to local directory

## Steps
1. python pull_listing.py <url_here>
2. python auto_post.py

