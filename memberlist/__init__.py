'Entry point for flaskbb-plugin-private-memberlist'

# 3rd party
from flask import current_app, request
from flask_login import current_user

endpoints = (
    'forum.memberlist',
    'forum.search',
    'user.profile',
    'user.view_all_topics',
    'user.view_all_posts',
)


def flaskbb_request_processors(app):
    'Apply the login restriction.'

    @app.before_request
    def before_request():
        'Check authentication before request is handled.'

        if (request.endpoint in endpoints
                and not current_user.is_authenticated):
            return current_app.login_manager.unauthorized()
