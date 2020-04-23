from .BaseType import BaseType
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class ArtistShuffleId(BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            'RDAO',
            utils.entropy(22),
        ),
    )
