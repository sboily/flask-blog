
def init_app(app):
    from views import home
    app.register_blueprint(home)
