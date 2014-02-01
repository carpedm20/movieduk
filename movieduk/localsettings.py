SOCIAL_AUTH_FACEBOOK_KEY = '387661514698415'
SOCIAL_AUTH_FACEBOOK_SECRET = '0e4e65e38f54da96e9421284e5b89b04'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email','read_friendlists','publish_stream']

FACEBOOK_APP_ID='387661514698415'
FACEBOOK_API_SECRET='0e4e65e38f54da96e9421284e5b89b04'
FACEBOOK_EXTENDED_PERMISSIONS = ['email','read_friendlists','publish_stream']

LOGIN_URL                         = '/login/'
LOGIN_ERROR_URL                   = '/login/error/'
LOGIN_REDIRECT_URL                = '/'
LOGOUT_REDIRECT_URL               = '/'

FACEBOOK_REDIRECT_URI = 'http://movieduk.us.to:8000/login/facebook/'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_FORCE_POST_DISCONNECT = True

SOCIAL_AUTH_USER_MODEL = 'account.DukUser'
SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_DEFAULT_USERNAME      = 'DukUser'

VKONTAKTE_APP_AUTH                = None

SOCIAL_AUTH_FORCE_POST_DISCONNECT = True

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    #'account.backends.FacebookBackend',
)

SOCIAL_AUTH_FORCE_POST_DISCONNECT = True
