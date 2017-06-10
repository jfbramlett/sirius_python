import com.sirius.logging_config

import logging
import itertools

logger = logging.getLogger(__name__)

class Permutator(object) :
    """
    Class responsible for managing our permutations
    """

    def __init__(self):
        self.registered_collections = {}

    def register_set(self, id, number_set):
        """
        Adds a new set

        :param id: The unique id for the set
        :param number_set: A collection of numbers
        :return: nothing
        """
        logger.info("Adding new set with id %s", id)
        self.registered_collections[id] = number_set


    def get_set(self, id):
        """
        Gets the registered set with the given id

        :param id: The id of the set
        :return: the list associated with the given id or none if the id is not registered
        """
        logger.info("Looking up set with id %s", id)
        return self.registered_collections.get(id)

    def get_permutations(self, id):
        """
        Returns the set of permutations associated with the given id

        :param id: The id for the registered set we are working with
        :return: A list of lists containing the permutations of the original list
        """
        number_set = self.get_set(id)
        if number_set is None :
            return [[]]

        logger.info("Generating permutations for set %s", str(number_set))
        return [list(x) for x in itertools.permutations(number_set)]

    def get_sum(self, id):
        """
        Get the sum of all the numbers across all permutations

        :param id: The id of the set we are working with
        :return: long The sum of all permutations
        """
        permutations = self.get_permutations(id)
        return sum([sum(x) for x in permutations])

    def adjust_permutation(self, id, adjustment):
        """
        Gets the permutations associated with the set with the given id and then adjust
        all the values by the given adjustment

        :param id: The id of the set we are working with
        :param adjustment: An integer which is the adjustment amount
        :return: A list of list containing the adjusted permutations
        """
        permutations = self.get_permutations(id)
        return [[x + adjustment for x in perm] for perm in permutations]
