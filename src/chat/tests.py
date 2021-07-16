from django.test import TestCase
from django.urls import reverse


class PageTestViewTest(TestCase):
    def setUp(self):
        pass

    def test_view_url_not_exists(self):
        pages = [
            '/some',
            '/finam/0/',
            '/finam/2/',
        ]
        for page in pages:
            resp = self.client.get(page)
            self.assertEqual(resp.status_code, 404)

    def test_view_url_exists(self):
        pages = [
            '/chat/',
        ]
        for page in pages:
            resp = self.client.get(page)
            self.assertEqual(resp.status_code, 200)

    def test_middleware(self):
        header = {'HTTP_USER_AGENT': 'iphone'}
        resp = self.client.get(reverse('index'), **header)
        self.assertEqual(resp.status_code, 200)
        string = str(resp.content)
        self.assertTrue(string.find('MOBILE') >= 0)
