
def init_app(app):
    from views import installation 
    app.register_blueprint(installation)
