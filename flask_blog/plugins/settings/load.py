

def init_app(app):
    from views import settings
    app.register_blueprint(settings)
