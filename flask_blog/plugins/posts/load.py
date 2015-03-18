import logging

def init_app(app):
    from views import posts
    app.register_blueprint(posts)
