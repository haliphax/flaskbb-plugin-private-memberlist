'Entry point for flaskbb-plugin-private-memberlist'

# 3rd party
from flask import abort, request
from flask_login import current_user


def flaskbb_request_processors(app):
    'Apply the login restriction'

    @app.before_request
    def before_request():
        if (request.endpoint == 'forum.memberlist'
                and not current_user.is_authenticated):
           abort(401)

