# remoteusermgmt
It is a System to create/update/delete user accounts on all servers.  A server is associated with a project/projects and users are assigned project/projects.  GUI for managing the same.

## It is recommended to use Virtualenv 

### How to use 
1. Create a new virtualenv using `virtualenv <dir-name>`.
2. Cd to `<dir-name>` and activate virtualenv using `source bin/activate`.
3. Clone the project to your local computer.
4. Cd to project directory and install dependencies using `pip install -r requirements.txt`.
5. Run the server using `python manage.py runserver`

### How to use without Virtualenv
1. Clone the project to your local computer
2. Install all the dependencies using `pip install -r requirements.txt` in the project directory.
3. Run the server using `python manage.py runserver`