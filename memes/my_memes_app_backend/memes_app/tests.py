from .test_conf import TestSetUp
from django.urls import reverse


class TestViews(TestSetUp):

    def test_list_all_memes(self):
        """test the case whene user want to see all the memes in the db"""
        res = self.client.get(self.list_memes_url)
        self.assertEqual(res.status_code, 200)

    def test_post_meme(self):
        """test the case whene user want to add a meme in the db"""
        res = self.client.post(
            self.add_meme_url, self.test_data, format='json')
        self.assertEqual(res.status_code, 201)

    def test_edit_existed_meme(self):
        """test the case whene user want to edit an existed meme in the db"""

        edit_meme_url = reverse('memes_app:edit_meme', kwargs={'pk': "2"})
        test_data = {
            "id": 2,
            "icon_url": "icon_url test",
            "meme_value": "meme_value test"
        }
        self.client.post(
            self.add_meme_url, test_data, format='json')
        res = self.client.put(
            edit_meme_url, test_data, format='json')

        self.assertEqual(res.status_code, 200)

    def test_edit_not_existed_meme(self):
        """test the case whene user want to edit meme that dose not exists"""

        res = self.client.put(
            self.edit_meme_url, self.test_data, format='json')
        self.assertEqual(res.status_code, 404)

    def test_delete_not_existed_meme(self):
        """test the case whene user want to delete meme that dose not exists"""

        res = self.client.delete(self.delete_meme_url)
        self.assertEqual(res.status_code, 404)

    def test_delete_existed_meme(self):
        """test the case whene user want to delete existsed meme  """

        self.test_post_meme()
        res = self.client.delete(self.delete_meme_url)
        self.assertEqual(res.status_code, 204)
