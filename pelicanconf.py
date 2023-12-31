from datetime import datetime

THEME = 'Flex'

AUTHOR = 'Ji Wan Koo'
# SITEURL = ''
SITEURL = 'https://haerang34.github.io/pelican-ssg'
SITENAME = "Koo's Devlog Site"
SITETITLE = "Koo's Devlog"
SITESUBTITLE = "Software Developer / Data Engineer"
SITEDESCRIPTION = "Update PortFolio And Blog"
BROWSER_COLOR = "#333333"
THEME_COLOR = 'dark'
PYGMENTS_STYLE = "monokai"
ROBOTS = "index, follow"

PATH = 'content'
TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'ko'
DEFAULT_PAGINATION = 10

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATIVE_URLS = True
STATIC_PATHS = ['images']
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blogs']
SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'

MAIN_MENU = True
HOME_HIDE_TAGS = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

LINKS = (
    ('company','https://www.syntekabio.com'),
)

SOCIAL = (
    ('github', 'https://www.github.com/haerang34'),
    ('linkedin', 'https://www.linkedin.com/in/jiwankoo92'),
    ('instagram','https://www.instagram.com/nine_jwan'),
)

COPYRIGHT_NAME = 'Ji Wan Koo'
COPYRIGHT_YEAR = '2017-{}'.format(datetime.now().year)



