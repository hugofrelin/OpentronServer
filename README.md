# Opentron Server

This is a Flask Server that can be used as the back end of a custom made Opentron Robot app.

## Functionality

The server has calls for:
* Uploading and deleting protocols
* Creating and deleting sessions
* Starting, resuming and canceling runs
* Scanning the local network for robots


## Setting up the server
The command:
```
sudo python3 manage.py
```
will run the server locally. The Sudo is needed to give the server root privileges which is required in order to scan the network for robots.
