import reflex as rx

config = rx.Config(
    app_name="MiniGames",
    api_url="minigamesforreflex-production.up.railway.app",  # URL que te dio Railway
    deploy_url="https://minigames-with-reflex.vercel.app",
    cors_allowed_origins=["https://minigames-with-reflex.vercel.app"]
)