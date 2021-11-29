from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):
        self.list_memes_url = reverse('memes_app:my_memes')
        self.add_meme_url = reverse('memes_app:add_meme')
        self.edit_meme_url = reverse('memes_app:edit_meme', kwargs={'pk': "1"})
        self.delete_meme_url = reverse(
            'memes_app:delete_meme', kwargs={'pk': "1"})

        self.test_data = {
            "id": 1,
            "icon_url": "icon_url test",
            "meme_value": "meme_value test"
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
