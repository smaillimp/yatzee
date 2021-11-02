# yatzyee
My first game

To work on the project do the following:

To activate the virtual environment on windows
```
python -m venv venv
source venv/Scripts/activate
```

To activate the virtual environment on Linux
```
python -m venv venv
Source venv/bin/activate
```

To add a file to git, do the following:

```
touch filename.py
git add filename.py
```

Save a change in git and push it to the origin:

```
git commit -am "add functionality"
git push origin HEAD
```

To get a version from git:

```
git fetch
git pull
```

To check the current status, type

`git status`

For testing, install the following modules:

`pytest`, `mock`

You might do so using pip:

`pip install -U pytest mock`

To run the tests

`python -m pytest`

to reset local

`git reset --hard`