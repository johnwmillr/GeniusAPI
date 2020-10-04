import unittest

from lyricsgenius.utils import parse_redirected_url, sanitize_filename


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up ultis tests...\n")

    def test_sanitize_filename(self):
        raw = 'B@ad File#_name'
        cleaned = 'Bad File_name'
        r = sanitize_filename(raw)
        self.assertEqual(r, cleaned)

    def test_parse_redirected_url(self):
        redirected = 'https://example.com/callback?code=test'
        flow = 'code'
        code = 'test'
        r = parse_redirected_url(redirected, flow)
        self.assertEqual(r, code)

        redirected = 'https://example.com/callback#access_token=test'
        flow = 'token'
        code = 'test'
        r = parse_redirected_url(redirected, flow)
        self.assertEqual(r, code)