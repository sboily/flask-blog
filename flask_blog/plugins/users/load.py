

def init_app(app):
    from views import users
    app.register_blueprint(users)
