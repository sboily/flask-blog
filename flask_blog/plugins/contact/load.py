

def init_app(app):
    from views import contact
    app.register_blueprint(contact)
