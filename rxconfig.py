import reflex as rx

config = rx.Config(
    app_name="MiniGames",
    api_url="https://minigamesforreflex-production.up.railway.app",  # URL que te dio Railway
    deploy_url="https://minijuegos-reflex.vercel.app/",
    cors_allowed_origins=["https://minigames-with-reflex.vercel.app"]
)