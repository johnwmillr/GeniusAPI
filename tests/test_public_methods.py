import unittest

from .test_genius import genius


class TestAlbumMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up album methods tests...\n")
        cls.album_id = 104614

    def test_album(self):
        msg = "Album ID did not match."
        r = genius.album(self.album_id)
        self.assertEqual(r['album']['id'], self.album_id, msg)

    def test_albums_charts(self):
        msg = "Album charts were empty."
        r = genius.albums_charts()
        self.assertTrue("chart_items" in r, msg)

    def test_album_comments(self):
        msg = "Album comments were empty."
        r = genius.album_comments(self.album_id)
        self.assertTrue("comments" in r, msg)

    def test_album_cover_arts(self):
        msg = "Album cover arts were empty."
        r = genius.album_cover_arts(self.album_id)
        self.assertTrue("cover_arts" in r, msg)

    def test_album_leaderboard(self):
        msg = "Album leaderboard was empty."
        r = genius.album_leaderboard(self.album_id)
        self.assertTrue("leaderboard" in r, msg)

    def test_album_tracks(self):
        msg = "Album tracks were empty."
        r = genius.album_tracks(self.album_id)
        self.assertTrue("tracks" in r, msg)


class TestAnnotationMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up annotation methods tests...\n")
        cls.annotation_id = 10225840

    def test_annotation(self):
        msg = "annotation ID did not match."
        r = genius.annotation(self.annotation_id, public_api=True)
        self.assertEqual(r['annotation']['id'], self.annotation_id, msg)

    def test_annotation_edits(self):
        msg = "annotation edits were empty."
        r = genius.annotation_edits(self.annotation_id)
        self.assertTrue("versions" in r, msg)

    def test_annotation_comments(self):
        msg = "annotation comments were empty."
        r = genius.annotation_comments(self.annotation_id)
        self.assertTrue("comments" in r, msg)


class TestArticleMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up article methods tests...\n")
        cls.article_id = 11880

    def test_article(self):
        msg = "article ID did not match."
        r = genius.article(self.article_id)
        self.assertEqual(r['article']['id'], self.article_id, msg)

    def test_article_comments(self):
        msg = "article comments were empty."
        r = genius.article_comments(self.article_id)
        self.assertTrue("comments" in r, msg)

    def test_latest_articles(self):
        msg = "latest articles were empty."
        r = genius.latest_articles()
        self.assertTrue("editorial_placements" in r, msg)


class TestArtistMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up artist methods tests...\n")
        cls.artist_id = 1665

    def test_artist(self):
        r = genius.artist(self.artist_id)
        self.assertEqual(r['artist']['id'], self.artist_id)

    def test_artist_activity(self):
        r = genius.artist_activity(self.artist_id)
        self.assertTrue("line_items" in r)

    def test_artist_albums(self):
        r = genius.artist_albums(self.artist_id)
        self.assertTrue("albums" in r)

    # def test_artist_contribution_opportunities(self):
    #     r = genius.artist_contribution_opportunities(self.artist_id)
    #     self.assertIsNotNone(r.get('contribution_opportunities'))

    def test_artist_followers(self):
        r = genius.artist_followers(self.artist_id)
        self.assertTrue("followers" in r)

    def test_artist_leaderboard(self):
        r = genius.artist_leaderboard(self.artist_id)
        self.assertTrue("leaderboard" in r)

    def test_artist_songs(self):
        r = genius.artist_songs(self.artist_id)
        self.assertTrue("songs" in r)

    def test_search_artist_songs(self):
        r = genius.search_artist_songs(self.artist_id, 'test')
        self.assertTrue("songs" in r)


class TestCoverArtMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up cover arts methods tests...\n")
        cls.album_id = 104614

    def test_cover_arts(self):
        r = genius.cover_arts(self.album_id)
        self.assertTrue("cover_arts" in r)


class TestDiscussionMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up discussion methods tests...\n")
        cls.discussion_id = 123

    def test_discussion(self):
        r = genius.discussion(self.discussion_id)
        self.assertEqual(r['discussion']['id'], self.discussion_id)

    def test_discussion_replies(self):
        r = genius.discussion_replies(self.discussion_id)
        self.assertTrue("forum_posts" in r)


class TestLeaderboardMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up leaerboard methods tests...\n")

    def test_leaderboard(self):
        r = genius.leaderboard()
        self.assertTrue("leaderboard" in r)

    def test_charts(self):
        r = genius.charts()
        self.assertTrue("chart_items" in r)


class TestQuestionMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up question methods tests...\n")
        cls.album_id = 104614

    def test_questions(self):
        r = genius.questions(self.album_id)
        self.assertIsNotNone(r.get('questions'))


class TestReferentMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up referent methods tests...\n")
        cls.web_page_id = 10347
        cls.referent_ids = [20793764, 20641014]

    def test_referent(self):
        r = genius.referent(self.referent_ids)
        self.assertTrue(str(self.referent_ids[0]) in r['referents'])
        self.assertTrue(str(self.referent_ids[1]) in r['referents'])

    def test_referents(self):
        r = genius.referents(web_page_id=self.web_page_id, public_api=True)
        self.assertIsNotNone(r.get('referents'))


class TestSearchMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up search methods tests...\n")
        cls.search_term = 'test'

    def test_search(self):
        r = genius.search(self.search_term)
        self.assertIsNotNone(r['hits'])

    def test_search_albums(self):
        r = genius.search_albums(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'album')

    def test_search_articles(self):
        r = genius.search_articles(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'article')

    def test_search_artists(self):
        r = genius.search_artists(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'artist')

    def test_search_lyrics(self):
        r = genius.search_lyrics(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'lyric')

    def test_search_songs(self):
        r = genius.search_songs(self.search_term, public_api=True)
        self.assertEqual(r['sections'][0]['type'], 'song')

    def test_search_users(self):
        r = genius.search_users(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'user')

    def test_search_videos(self):
        r = genius.search_videos(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'video')

    def test_search_all(self):
        r = genius.search_all(self.search_term)
        self.assertEqual(r['sections'][0]['type'], 'top_hit')


class TestSongMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up song methods tests...\n")
        cls.song_id = 378195

    def test_song(self):
        r = genius.song(self.song_id, public_api=True)
        self.assertEqual(r['song']['id'], self.song_id)

    def test_song_activity(self):
        r = genius.song_activity(self.song_id)
        self.assertTrue("line_items" in r)

    def test_song_comments(self):
        r = genius.song_comments(self.song_id)
        self.assertTrue("comments" in r)

    def test_song_contributors(self):
        r = genius.song_contributors(self.song_id)
        self.assertTrue("contributors" in r)


class TestUserMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up user methods tests...\n")
        cls.user_id = 1

    def test_user(self):
        r = genius.user(self.user_id)
        self.assertEqual(r['user']['id'], self.user_id)

    def test_user_accomplishments(self):
        r = genius.user_accomplishments(self.user_id)
        self.assertTrue("accomplishments" in r)

    def test_user_following(self):
        r = genius.user_following(self.user_id)
        self.assertTrue("followed_users" in r)

    def test_user_followers(self):
        r = genius.user_followers(self.user_id)
        self.assertTrue("followers" in r)

    def test_user_contributions(self):
        r = genius.user_contributions(self.user_id)
        self.assertTrue("contribution_groups" in r)

    def test_user_annotations(self):
        r = genius.user_annotations(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'annotation')

    def test_user_articles(self):
        r = genius.user_articles(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'article')

    def test_user_pyongs(self):
        r = genius.user_pyongs(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'pyong')

    def test_user_questions_and_answers(self):
        r = genius.user_questions_and_answers(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'answer')

    def test_user_suggestions(self):
        r = genius.user_suggestions(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'comment')

    def test_user_transcriptions(self):
        r = genius.user_transcriptions(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'song')

    def test_user_unreviewed(self):
        r = genius.user_unreviewed(self.user_id)
        type = r['contribution_groups'][0]['contribution_type']
        self.assertEqual(type, 'annotation')


class TestVideoMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up video methods tests...\n")
        cls.video_id = 18681

    def test_video(self):
        r = genius.video(self.video_id)
        self.assertEqual(r['video']['id'], self.video_id)

    def test_videos(self):
        r = genius.videos(video_id=self.video_id, series=True)
        self.assertTrue("video_lists" in r)

        r = genius.videos(video_id=self.video_id)
        self.assertTrue("videos" in r)


class TestMiscMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up misc methods tests...\n")
        # cls.line_item_id = 146262999
        cls.annotation_id = 10225840

    # def test_line_item(self):
    #    r = genius.line_item(self.line_item_id)
    #    self.assertTrue("line_item" in r)

    def test_voters(self):
        r = genius.voters(annotation_id=self.annotation_id)
        self.assertTrue("voters" in r)
