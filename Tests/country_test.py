from Model.basemodel import BaseModel
from Model.basemodel import Country
import json
import unittest
import app


class CountryControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_post_country(self):
        data = {
            'id': '1',
            'name': 'Test Country',
            'description': 'This is a test country'
        }
        response = self.client.post('/country', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), data)

    def test_get_country(self):
        country_id = '1'
        response = self.client.get(f'/countries/{country_id}')
        self.assertEqual(response.status_code, 200)
        expected_data = {
            'id': country_id,
            'name': 'Country Test',
            'description': None
        }
        self.assertEqual(response.get_json(), expected_data)

if __name__ == '__main__':
    unittest.main()