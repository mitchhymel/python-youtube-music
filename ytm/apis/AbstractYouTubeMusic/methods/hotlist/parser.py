from ... import utils

__parser__ = __name__.split('.')[-1]
__all__ = (__parser__,)

def parse(data):
    grid_items = utils.get_nested \
    (
        data,
        'contents',
        'singleColumnBrowseResultsRenderer',
        'tabs',
        0,
        'tabRenderer',
        'content',
        'sectionListRenderer',
        'contents',
        0,
        'itemSectionRenderer',
        'contents',
        0,
        'gridRenderer',
        'items',
        default = (),
    )

    tracks = []

    for track in grid_items:
        track = utils.first_key(track)

        track_title = utils.get_nested \
        (
            track,
            'title',
            'runs',
            0,
            'text',
        )
        track_views = utils.get_nested \
        (
            track,
            'subtitle',
            'runs',
            -1,
            'text',
        )
        track_artist_id = utils.get_nested \
        (
            track,
            'menu',
            'menuRenderer',
            'items',
            5,
            'menuNavigationItemRenderer',
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        track_thumbnail = utils.get_nested \
        (
            track,
            'backgroundImage',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        track_id = utils.get_nested \
        (
            track,
            'onTap',
            'watchEndpoint',
            'videoId',
        )
        track_music_video_type = utils.get_nested \
        (
            track,
            'onTap',
            'watchEndpoint',
            'watchEndpointMusicSupportedConfigs',
            'watchEndpointMusicConfig',
            'musicVideoType',
        )

        raw_track_artists = utils.get_nested \
        (
            track,
            'subtitle',
            'runs',
            default = (),
        )[:-1:2]

        track_artists = []

        for track_artist in raw_track_artists:
            track_artist_title = utils.get_nested \
            (
                track_artist,
                'text',
            )

            track_artists.append(track_artist_title)

        track_data = \
        {
            'title':            track_title,
            'views':            track_views,
            'artists':          track_artists,
            'artist_id':        track_artist_id,
            'thumbnail':        track_thumbnail,
            'id':               track_id,
            'music_video_type': track_music_video_type,
        }

        tracks.append(track_data)

    return tracks