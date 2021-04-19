# LyricsGenius: a Python client for the Genius.com API
[![Build Status](https://travis-ci.org/johnwmillr/LyricsGenius.svg?branch=master)](https://travis-ci.org/johnwmillr/LyricsGenius)
[![Documentation Status](https://readthedocs.org/projects/lyricsgenius/badge/?version=master)](https://lyricsgenius.readthedocs.io/en/latest/?badge=master)
[![PyPI version](https://badge.fury.io/py/lyricsgenius.svg)](https://pypi.org/project/lyricsgenius/)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/lyricsgenius/)

`lyricsgenius` provides a simple interface to the song, artist, and lyrics data stored on [Genius.com](https://www.genius.com).

The full documentation for `lyricsgenius` is available online at [Read the Docs](https://lyricsgenius.readthedocs.io/en/master/).

## Setup
Before using this package you'll need to sign up for a (free) account that authorizes access to [the Genius API](http://genius.com/api-clients). The Genius account provides a `access_token` that is required by the package. See the [Usage section](https://github.com/johnwmillr/LyricsGenius#usage) below for examples.

## Installation
`lyricsgenius` requires Python 3.

Use `pip` to install the package from PyPI:

```bash
pip install lyricsgenius
```

Or, install the latest version of the package from GitHub:

```bash
pip install git+https://github.com/johnwmillr/LyricsGenius.git
```

## Usage
Import the package and initiate Genius:

```python
import lyricsgenius
genius = lyricsgenius.Genius(token)
```

If you don't pass a token to the `Genius` class, `lyricsgenus` will look for an environment variable called `GENIUS_ACCESS_TOKEN` and attempt to use that for authentication.

```python
genius = Genius()
```

Search for songs by a given artist:

```python
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
```
By default, the `search_artist()` only returns songs where the given artist is the primary artist.
However, there may be instances where it is desirable to get all of the songs that the artist appears on.
You can do this by setting the `include_features` argument to `True`.

```python
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title", include_features=True)
print(artist.songs)
```

Search for a single song by the same artist:

```python
song = artist.song("To You")
# or:
# song = genius.search_song("To You", artist.name)
print(song.lyrics)
```

Add the song to the artist object:

```python
artist.add_song(song)
# the Artist object also accepts song names:
# artist.add_song("To You")
```

Save the artist's songs to a JSON file:

```python
artist.save_lyrics()
```

Searching for an album and saving it:

```python
album = genius.search_album("The Party", "Andy Shauf")
album.save_lyrics()
```

There are various options configurable as parameters within the `Genius` class:

```python
genius.verbose = False # Turn off status messages
genius.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = False # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)"] # Exclude songs with these words in their title
```

You can also call the package from the command line:

```bash
export GENIUS_ACCESS_TOKEN="my_access_token_here"
python3 -m lyricsgenius --help
```

Search for and save lyrics to a given song and album:

```bash
python3 -m lyricsgenius song "Begin Again" "Andy Shauf" --save
python3 -m lyricsgenius album "The Party" "Andy Shauf" --save
```

Search for five songs by 'The Beatles' and save the lyrics:

```bash
python3 -m lyricsgenius artist "The Beatles" --max-songs 5 --save
```

## Example projects

  - [Trucks and Beer: A textual analysis of popular country music](http://www.johnwmillr.com/trucks-and-beer/)
  - [Neural machine translation: Explaining the Meaning Behind Lyrics](https://github.com/tsandefer/dsi_capstone_3)
  - [What makes some blink-182 songs more popular than others?](http://jdaytn.com/posts/download-blink-182-data/)
  - [Sentiment analysis on hip-hop lyrics](https://github.com/Hugo-Nattagh/2017-Hip-Hop)
  - [Does Country Music Drink More Than Other Genres?](https://towardsdatascience.com/does-country-music-drink-more-than-other-genres-a21db901940b)
  - [49 Years of Lyrics: Why So Angry?](https://towardsdatascience.com/49-years-of-lyrics-why-so-angry-1adf0a3fa2b4)

## Contributing
If you'd like to contribute to `LyricsGenius` by fixing a bug, introducing
a new feature, improving the docs or anything else, you can follow the
steps below:

First, clone the repository and install in editable mode with dev dependencies:
```bash
git clone https://github.com/johnwmillr/LyricsGenius
cd LyricsGenius
pip install -e .[dev]
```
You will need the dev dependencies to run the tests.

Now you can make the changes you intended. Before or after committing your changes, you can run our tests to make sure everything is working okay. We use `tox` to manage our tests and you can use it to run all the tests at once:

```bash
tox
```
But depending on your changes you may not need to run all the tests and our unit tests require extra setup before working. Read the sections below to test different parts of the package.

### Documentation
We use `sphinx` to build the documentation. You can easily build the docs offline:
```bash
cd docs
make html
```
The output will be available in the `build/html` folder and you can navigate the docs from `build/html/index.html`. You can also create the docs using the `tox -e docs` command.

If you've made any changes to the docs, make sure the linting tests below.

### Linting
We use `flake8` for code quality checks, and `doc8` for style checking the docs. You can run both using `tox`:
```bash
tox -e lint
```

### Tests
At the moment we're using Python's own `unittest` for the unit tests but will probably migrate to `pytest` in the future.

The unit tests require some setup before running. These tests interact with Genius and therefore require a network connection. Furthermore, some of the tests try creating, manipulating, and finally removing annotations, but in case of an unforeseen failure in those tests, you might end up with some annotations on your profile that you can delete later manually. You'll need to set the following environment variables:

 - `GENIUS_CLIENT_ID`
 - `GENIUS_CLIENT_SECRET`
 - `GENIUS_REDIRECT_URI`
 - `GENIUS_ACCESS_TOKEN`

To get your client's credentials, visit the [API Clients](https://genius.com/api-clients) page. There you can view your client ID and client password. If you haven't set a redirect URI, click on Edit and enter any valid URL (e.g. `http://example.com`). Now save these in the respective env variables mentioned above.

The Genius token needed for the tests isn't the usual client access token. The tests need a _user token_, like the one the interactive console at [Genius Docs](http://docs.genius.com/) uses. `LyricsGenius` already has some utility functions to help get one of these. Just start `python` from your terminal and then type in the code below:
```python
import lyricsgenius as lg
client_id, redirect_uri, _ = lg.auth_from_environment()
auth = lg.OAuth2.client_only_app(client_id=client_id, redirect_uri=redirect_uri, scope="all")
auth.prompt_user()
```
This will open up your browser and you'll be asked to allow access to your client and then you'll be redirected to your redirect URI. After entering it into the console, the package will print your user token. Save that token in the env variable `GENIUS_ACCESS_TOKEN`. Now, you're ready to run the unit tests.
```bash
tox -e tests
```
