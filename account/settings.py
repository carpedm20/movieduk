from os.path import abspath, dirname, basename, join

ROOT_PATH = abspath(dirname(__file__))
TEMPLATE_DIRS = (
    join(ROOT_PATH, 'templates'),
)

FACEBOOK_APP_ID = '387661514698415'
FACEBOOK_API_SECRET = '0e4e65e38f54da96e9421284e5b89b04'
#FACEBOOK_REDIRECT_URI = 'http://carpedm20.qc.to/login/'
FACEBOOK_REDIRECT_URI = 'http://movieduk.us.to:8000/login/'
