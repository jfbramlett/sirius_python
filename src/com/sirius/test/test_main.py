import unittest
import json
from com.sirius.main import app

class TestFlaskApi(unittest.TestCase):
    """
    Test case for our REST api
    """

    def setUp(self):
        self.client = app.test_client()

    def test_add_entity(self):
        """
        Tests adding a new entity
        """
        content = {
            "entityId" : 1,
            "data" : [1, 2, 3]
        }

        response = self.client.post('/addEntity', data = json.dumps(content),
                                    headers={'content-type': 'application/json'})
        self.assertEquals(201, response.status_code)

        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]

        self.assertEquals(expected, json.loads(response.data)["permutations"])

    def test_sum(self):
        """
        Tests summing our content
        """
        content = {
            "entityId" : "1",
            "data" : [1, 2, 3]
        }

        response = self.client.post('/addEntity', data = json.dumps(content),
                                    headers={'content-type': 'application/json'})
        self.assertEquals(201, response.status_code)

        response = self.client.get('/sumEntity/1')
        self.assertEquals(200, response.status_code)
        self.assertEquals(36, json.loads(response.data)["sum"])

    def test_sum_invalid_entityId(self):
        """
        Tests running our sum where the id passed in is invalid
        """
        response = self.client.get('/sumEntity/5')
        self.assertEquals(404, response.status_code)

    def test_update(self):
        """
        Tests summing our content
        """
        content = {
            "entityId" : "1",
            "data" : [1, 2, 3]
        }

        response = self.client.post('/addEntity', data = json.dumps(content),
                                    headers={'content-type': 'application/json'})
        self.assertEquals(201, response.status_code)

        update = {
            "entityId" : "1",
            "add" : -1
        }
        response = self.client.post('/updateEntity', data = json.dumps(update),
                                    headers={'content-type': 'application/json'})
        self.assertEquals(200, response.status_code)

        expected = [
            [0, 1, 2],
            [0, 2, 1],
            [1, 0, 2],
            [1, 2, 0],
            [2, 0, 1],
            [2, 1, 0]
        ]

        self.assertEquals(expected, json.loads(response.data)["permutations"])

        # now update it back to make sure our state was maintained
        update = {
            "entityId" : "1",
            "add" : 1
        }
        response = self.client.post('/updateEntity', data = json.dumps(update),
                                    headers={'content-type': 'application/json'})
        self.assertEquals(200, response.status_code)

        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]

        self.assertEquals(expected, json.loads(response.data)["permutations"])


    def test_sum_invalid_entityId(self):
        """
        Tests running our sum where the id passed in is invalid
        """
        response = self.client.get('/sumEntity/5')
        self.assertEquals(404, response.status_code)


if __name__ == "__main__":
    unittest.main()