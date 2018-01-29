import unittest

from com.sirius.permutations.permutator import Permutator
from com.sirius.permutations.notfoundexception import NotFoundException

class Permutatortest(unittest.TestCase) :
    """
    Test case for our Permutator class
    """

    def test_register_set(self):
        """
        Tests registering a new list and then retrieving it back
        """
        permutator = Permutator()

        collection = [1, 2, 3]
        id = "1"

        permutator.register_set(id, collection)

        self.assertIsNotNone(permutator.get_set(id))
        self.assertEqual(collection, permutator.get_set(id))

    def test_get_missing(self):
        """
        Tests trying to get a collection which doesn't exist
        """
        permutator = Permutator()

        collection = [1, 2, 3]
        id = "1"
        missing_id = "2"

        permutator.register_set(id, collection)

        with self.assertRaises(NotFoundException) :
            permutator.get_set(missing_id)

    def test_sum(self):
        """
        Tests summing the values in our permutations
        """
        permutator = Permutator()

        collection = [1, 2, 3]
        id = "1"
        permutator.register_set(id, collection)

        self.assertEquals(36, permutator.get_sum(id))


    def test_sum_missing(self):
        """
        Tests summing the values in our permutations where the collection requested isn't registered
        """
        permutator = Permutator()

        collection = [1, 2, 3]
        id = "1"
        missing_id = "2"
        permutator.register_set(id, collection)

        with self.assertRaises(NotFoundException) :
            permutator.get_sum(missing_id)

    def test_permutations(self):
        """
        Tests getting the permutations from a given set
        """
        permutator = Permutator()
        collection = [1, 2, 3]
        id = "1"
        permutator.register_set(id, collection)

        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]

        self.assertEquals(expected, permutator.get_permutations(id))

    def test_permutations_empty_input(self):
        """
        Tests getting the permutations from a given set where our input is empty
        """
        permutator = Permutator()
        id = "1"
        collection = []
        permutator.register_set(id, collection)

        expected = [[]]

        self.assertEquals(expected, permutator.get_permutations(id))


    def test_permutations_none_input(self):
        """
        Tests getting the permutations from a given set where our input is None
        """
        permutator = Permutator()
        id = "2"

        with self.assertRaises(NotFoundException) :
            permutator.get_permutations(id)

    def test_add_negative(self):
        """
        Tests getting an adjusted permutations where we are adding a negative value
        """
        permutator = Permutator()

        collection = [1, 2, 3]
        id = "1"
        permutator.register_set(id, collection)

        expected = [
            [0, 1, 2],
            [0, 2, 1],
            [1, 0, 2],
            [1, 2, 0],
            [2, 0, 1],
            [2, 1, 0]
        ]

        self.assertEquals(expected, permutator.adjust_permutation(id, -1))

        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]

        self.assertEquals(expected, permutator.adjust_permutation(id, 1))

    def test_add_positive(self):
        """
        Tests getting an adjusted permutations where we are adding a positive value
        """
        permutator = Permutator()

        collection = [1, 2, 3]
        id = "1"
        permutator.register_set(id, collection)

        expected = [
            [2, 3, 4],
            [2, 4, 3],
            [3, 2, 4],
            [3, 4, 2],
            [4, 2, 3],
            [4, 3, 2]
        ]

        self.assertEquals(expected, permutator.adjust_permutation(id, 1))


    def test_add_collection_not_found(self):
        """
        Tests getting an adjusted permutations where we request an id that is not registered
        """
        permutator = Permutator()

        id = "2"

        with self.assertRaises(NotFoundException) :
            permutator.adjust_permutation(id, 1)

    def test_permutations_manual(self):
        """
        Tests getting the permutations from a given set using our manual routine
        """
        permutator = Permutator()
        collection = [1, 2, 3]
        id = "1"
        permutator.register_set(id, collection)

        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 2, 1],
            [3, 1, 2]
        ]

        self.assertEquals(expected, permutator.get_permutations_manual(id))



if __name__ == '__main__':
    unittest.main()



