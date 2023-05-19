versioned with pyenv-win from chocolatey.
not using pipenv, but pyenv-win with venv.
not using a .gitignore, to save state of small project, all dependencies tracked.

Commands (python, PS):
python -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip
python -m pip install --no-cache-dir -U django --prefer-binary
pip list (or use pip freeze > packages.txt) to capture
    - use with pip install -r to gen dependencies

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