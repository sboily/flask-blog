import logging, time
from flask import Flask, render_template
from flask_blog.extensions import mongo, login_manager
from flask.ext.wtf.csrf import CsrfProtect
from flask.ext.markdown import Markdown
from flask_blog.utils.mdx_github_gists import GitHubGistExtension
from flask_blog.utils.mdx_strike import StrikeExtension
from flask_blog.utils.mdx_quote import QuoteExtension
from flask_blog.utils.mdx_code_multiline import MultilineCodeExtension


def create_app():
    app = Flask(__name__)
    configure_logging(app)
    configure_app(app)
    configure_extensions(app)
    configure_hooks(app)
    configure_filter(app)
    configure_error_handlers(app)

    return app


def configure_app(app):
    app.logger.info("Loading configuration")
    app.config.from_object('settings')


def configure_logging(app):
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    app.logger.info("Logger started")


def configure_hooks(app):
    @app.before_request
    def before_request():
        app.logger.debug("Hooks started")


def configure_filter(app):
    @app.template_filter('formatdate')
    def format_datetime_filter(value, format_="%a, %d %b %Y"):
        return value.strftime(format_)


def configure_extensions(app):
    db_init(app)
    CsrfProtect(app)

    login_manager.init_app(app)

    md = Markdown(app)
    md.register_extension(GitHubGistExtension)
    md.register_extension(StrikeExtension)
    md.register_extension(QuoteExtension)
    md.register_extension(MultilineCodeExtension)


def configure_error_handlers(app):
    @app.errorhandler(401)
    def page_not_found(e):
        return render_template('401.html'), 401

    @app.errorhandler(403)
    def page_not_authorized(e):
        return render_template('403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

def db_init(app):
    init_conn = 0
    while init_conn < 5:
        try:
            mongo.init_app(app)
            return True
        except:
            init_conn = init_conn+1
            app.logger.info("Connexion failure... (retry)")
            time.sleep(5)
    app.logger.error("There is a problem to connecting to the mongo database...")
    raise Exception("Database connection error...")
