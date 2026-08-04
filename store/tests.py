from django.test import SimpleTestCase
from django.urls import reverse


class PageSmokeTests(SimpleTestCase):
    """Basic route tests for PageStore public pages."""

    pages = (
        ('index', 'PageStore'),
        ('shop', 'Shop'),
        ('about', 'About'),
        ('contact', 'Contact'),
    )

    def test_named_pages_return_200_and_brand(self):
        for name, expected_text in self.pages:
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, 'PageStore')
                self.assertContains(response, expected_text)

    def test_unknown_page_returns_404(self):
        response = self.client.get('/does-not-exist/')
        self.assertEqual(response.status_code, 404)
