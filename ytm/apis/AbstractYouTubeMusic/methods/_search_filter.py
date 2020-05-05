from .. import decorators
from .... import constants
from .... import parsers
from ....types import SearchContinuation

@decorators.method()
def _search_filter \
        (
            self:         object,
            filter:       str,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    '''

    filter = filter.strip().lower()

    param = constants.SEARCH_PARAMS_MAP.get(filter)

    assert param, f'Invalid search filter: {repr(filter)}'

    if query:
        query  = query.strip()

        assert query,  'No search query provided'

        data = self._base.search \
        (
            query  = query,
            params = ''.join \
            (
                (
                    constants.SEARCH_PARAM_PREFIX,
                    param,
                    constants.SEARCH_PARAM_SUFFIX,
                ),
            ),
        )
    elif continuation:
        data = self._base.search \
        (
            continuation = continuation,
        )
    else:
        raise Exception \
        (
            'Missing 1 required argument: \'query\' or \'continuation\''
        )

    parsed_data = parsers._search_filter(data, filter)

    return parsed_data
