from . import pipeline, language_models
from . import processing, understanding, visualisation


try:
    from .version import version as __version__
except ImportError:
    from datetime import datetime
    __version__ = 'unknown-'+datetime.today().strftime('%Y%m%d')
