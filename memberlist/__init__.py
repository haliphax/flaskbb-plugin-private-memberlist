'Entry point for flaskbb-plugin-private-memberlist'

# 3rd party
from flask import current_app, request
from flask_login import current_user


def flaskbb_request_processors(app):
    'Apply the login restriction'

    @app.before_request
    def before_request():
        if (request.endpoint in ('forum.memberlist', 'forum.search')
                and not current_user.is_authenticated):
            return current_app.login_manager.unauthorized()
