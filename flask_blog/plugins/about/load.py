

def init_app(app):
    from views import about
    app.register_blueprint(about)
