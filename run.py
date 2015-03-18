from flask_blog.main import create_app
from stevedore.extension import ExtensionManager

application = create_app()

def plugins_fail(manager, entrypoint, exception):
    print "There is an error with this module: ", manager
    print "The entry point is: ", entrypoint
    print "The exception is: ", exception

if __name__ == "__main__":
    ext = ExtensionManager(namespace='flask_blog.plugins',
                     on_load_failure_callback=plugins_fail,
                     invoke_on_load=True,
                     invoke_args=(application,))
    application.run(host='0.0.0.0', port=8080)

