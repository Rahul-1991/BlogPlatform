from config import Config
from app.app_config import configure_app, register_versions, app

configure_app(app)
register_versions(Config.VERSIONS_ALLOWED)