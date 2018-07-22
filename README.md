## Selenium Python 
Basically you need your environment to be set up right to make this work

`python`
`selenium`
`chromedriver` 

The above are the necessary files and to be safely installed in the env
Follow installation steps here: `http://selenium-python.readthedocs.io/installation.html`

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

*auto_post* pulls from csv file to fill up the listing details
*pull_listing* pulls data from the carousell listing url and stores the information in a csv file and saves the first photo to local directory

## Steps
1. python pull_listing.py <url_here>
2. python auto_post.py

