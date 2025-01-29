python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
py -m reflex init
API_URL=https://minigamesforreflex-production.up.railway.app reflex export
unzip frontend.zip -d frontend
unzip backend.zip -d backend
deactive
