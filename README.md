## MKV

#### Prepare

```bash
  git clone git@github.com:AlexKorob/mkv.git
  cd mkv
  python3 -m venv ./venv
  . venv/bin/activate
  pip3 install -r requirements.txt
```

#### Configure Postgresql:

```bash
  sudo su - postgres
  psql
  CREATE DATABASE mkv;
  CREATE USER alex WITH PASSWORD '123';
  GRANT ALL PRIVILEGES ON DATABASE mkv TO alex;
  \q
  logout
```

#### Create Group (in django-admin) with name: Employees
