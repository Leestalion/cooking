from flask import current_app as app
from flask_assets import Bundle

DEVELOPMENT = 'development'

def compile_static_assets(assets):
    """Configure and build asset bundles."""

    # Css asset bundle
    css_bundle = Bundle(
        'src/main.css',
        filters='postcss',
        output='dist/main.css'
    )

    assets.register('css', css_bundle)

    # Do not build on production : we just send the compiled files to production server
    if (app.config["FLASK_ENV"] == DEVELOPMENT):
        css_bundle.build()