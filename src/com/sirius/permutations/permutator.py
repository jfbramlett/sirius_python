import com.sirius.logging_config

import logging
import itertools

from com.sirius.permutations.notfoundexception import NotFoundException

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
        if id not in self.registered_collections :
            raise NotFoundException(id)

        return self.registered_collections.get(id)

    def get_permutations(self, id):
        """
        Returns the set of permutations associated with the given id

        :param id: The id for the registered set we are working with
        :return: A list of lists containing the permutations of the original list
        """
        number_set = self.get_set(id)

        logger.info("Generating permutations for set %s", str(number_set))
        return [list(x) for x in itertools.permutations(number_set)]

    def get_permutations_manual(self, id):
        """
        Instead of using build-in permutation generator, do it by hand

        :param id: The id of the set we are generating the permutations for
        :return: A list of lists containing the permutations of the original list
        """
        number_set = self.get_set(id)

        result = []
        self._permutate(number_set[:], 0, result)

        return result


    def _permutate(self, number_set, start, result):
        """
        Recursive routine used to build our permutations

        :param number_set: The original number set
        :param start: The start position from which to do our swap
        :param result: The resulting permutations
        """
        if start >= len(number_set):
            result.append(number_set[:])

        for x in range(start, len(number_set)) :
            self._swap(number_set, start, x);
            self._permutate(number_set, start + 1, result);
            self._swap(number_set, start, x);

    def _swap(self, number_set, s1, s2):
        """
        Swaps the values at the given positions

        :param number_set: The numbers list
        :param s1: The first position
        :param s2:  The second position
        """
        first = number_set[s2]
        number_set[s2] = number_set[s1]
        number_set[s1] = first

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
        self.register_set(id, [x + adjustment for x in self.get_set(id)])
        return self.get_permutations(id)