versioned with pyenv-win from chocolatey.
not using pipenv (more powerfull - combines pip and venv, > pipenv shell, to switch to venv, packages in another dir), using pyenv-win with venv.
not using a .gitignore, to save state of small project, all dependencies tracked.

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

VSC (setting python interpreter shell):
    - ctrl + shift + p
    - > Python: Select Interpreter

Git:
    - git remote add origin git@OTonGitHub:OTonGitHub/CWM-Django.git 
    - git branch -M main
    - git push -u origin main

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