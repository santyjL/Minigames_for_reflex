source .venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf frontend
reflex init
API_URL=https://minigamesforreflex-production.up.railway.app reflex export --frontend-only
unzip frontend.zip -d frontend
rm -f frontend.zip
deactivate