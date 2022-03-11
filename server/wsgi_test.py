from cookingapp import create_app

from werkzeug.exceptions import NotFound
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.middleware.shared_data import SharedDataMiddleware


frontend = SharedDataMiddleware(NotFound(), {
    '/assets/': '../client/dist/assets',
    '/': '../client/dist/index.html'
})

app = DispatcherMiddleware(frontend, {'/api': create_app()})

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 5000, app, use_debugger = True, use_reloader = True, threaded=True)