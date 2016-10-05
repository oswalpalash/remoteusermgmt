# Remote User Management


### About
It is a System to create/update/delete user accounts on all servers.  A server is associated with a project/projects and users are assigned project/projects.  GUI for managing the same.

### Prerequisites

    - Python >= 2.7
    - virtualenv (virtualenvwrapper is recommended)


### Features
  - Interactive GUI

### Installed apps

* Django 1.8+
* MySQLdb
* py.test_ and coverage setup

### Configured URLs

* ``Users/admin/``

### Templates

* ``add_serv.html``
* ``list_serv.html``

### Features

* Settings package


### Installation


To setup a local development environment::

    virtualenv env --prompt="({{ remoteusermgmt }})"  # or mkvirtualenv {{ remoteusermgmt }}
    source env/bin/activate

    pip install -r requirements/dev.txt
    edit {{ remoteusermgmt }}/settings/project.py    # Enter your DB credentials
    cp {{ remoteusermgmt }}/settings/local.py.example {{ remoteusermgmt }}/settings/local.py  # To enable debugging

    sudo su - postgres
    createuser {{ remoteusermgmt }}  -P   # testtest is the default password
    createdb --template=template0 --encoding='UTF-8' --lc-collate='en_US.UTF-8' --lc-ctype='en_US.UTF-8' --owner={{ remoteusermgmt }} {{ remoteusermgmt }}
    exit

    ./manage.py migrate
    ./manage.py runserver


### License

Copyright (c) 2016 oswalpalash
