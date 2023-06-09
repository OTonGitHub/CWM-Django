versioned with pyenv-win from chocolatey.
not using pipenv (more powerfull - combines pip and venv, > pipenv shell, to switch to venv, packages in another dir), using pyenv-win with venv.
not using a .gitignore, to save state of small project, all dependencies tracked.

pyenv-win installation:
- Chocolatey:
> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
> choco install pyenv-win
- Add to system path:
    > [System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
    > [System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
    > [System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
- Add to user path:
    > [System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
- restart VSC, or shell.
- Switched > Set-ExecutionPolicy to Unrestricted, (not recommended, check other options)
- If resetting PS session:
    > Get-Process -Id $PID | Select-Object -ExpandProperty Path | ForEach-Object { Invoke-Command { & "$_" } -NoNewScope }

Commands (python, PS):
> python -m venv .venv
> .venv\Scripts\activate
> python -m pip install -U pip
> python -m pip install --no-cache-dir -U django --prefer-binary
> pip list (or use pip freeze > packages.txt) to capture
    - use with pip install -r to gen dependencies
> django-admin startproject storefront .
    - some names not available?
- manage.py mod takes settings into account (smart wrapper), avoids "settings not configured err (with djang-admin after creating project)"
> python manage.py runserver 9000
    - by default -p 8000
> python manage.py startapp playground
> python -m pip install --no-cache-dir -U django-debug-toolbar --prefer-binary
    - refer to https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

VSC (setting python interpreter shell):
    - ctrl + shift + p
    - > Python: Select Interpreter
    - copy from pipenv --venv, if using pipenv, if on venv, select from .venv dir /bin/python

Git:
    - git remote add origin git@OTonGitHub:OTonGitHub/CWM-Django.git 
    - git branch -M main
    - git push -u origin main

Project Sturcture:
    - playground (startapp):
        - migrations/, admin.py, apps.py (config), models.py, tests.py, views.py (request handler, not like MVC view)
    - for django-debug-tools to work, response needs to be in proper html, with html tag, body tag etc
    - When modelling:
        - minimal coupling,
        - high focus (cohesion, unix philosophy)
        
Views.py:
    - handling requests and giving response, request handler.
    - similar to actions.
    - architecturaly, views is not the right name, as view is what user sees, in django, that is template.


VSC shortcuts:
    - ctrl + k s (save all)
    - ctrl + b (folder structure show hide)
    - ctrl + ` (terminal)
    - ctrl + p or ctrl + e (searc and go to file)

Other frameworks:
- Django
- Flask (micro framework)

Aspects:
- Maturity
- Difficulty
- Stability
- Community (hire, help)
- High salary
- Back-end only (used like an API, gateway to data, provides an interface to talk with DB for front-end (RC), swap front-end with any ex: react, vue, JS; exchange data, not code)
- Comes with many features, but optional

Used in:
- Facebook
- Dropbox
- Netflix
- Spotify

Comes with:
- admin site
- ORM
- Auth
- Caching