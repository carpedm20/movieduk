SOCIAL_AUTH_FACEBOOK_KEY = '387661514698415'
SOCIAL_AUTH_FACEBOOK_SECRET = '0e4e65e38f54da96e9421284e5b89b04'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email','read_friendlists','publish_stream']

LOGIN_URL                         = '/login/'
LOGIN_ERROR_URL                   = '/login/error/'
LOGIN_REDIRECT_URL                = '/'
LOGOUT_REDIRECT_URL               = '/'

SOCIAL_AUTH_SETTINGS = {
    'SOCIAL_AUTH_LOGIN_URL': '/',
    'SOCIAL_AUTH_LOGIN_REDIRECT_URL': '/done',
    'SOCIAL_AUTH_USER_MODEL': 'example.models.User',
    'SOCIAL_AUTH_LOGIN_FUNCTION': 'example.auth.login_user',
    'SOCIAL_AUTH_LOGGEDIN_FUNCTION': 'example.auth.login_required',
}

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True

SOCIAL_AUTH_USER_MODEL = 'account.DukUser'

SOCIAL_AUTH_PIPELINE = (
  'social_auth.backends.pipeline.social.social_auth_user',
  'social_auth.backends.pipeline.social.associate_user',
  'social_auth.backends.pipeline.social.load_extra_data',
  'social_auth.backends.pipeline.user.update_user_details',
)

"""
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.misc.save_status_to_session',
)
"""
