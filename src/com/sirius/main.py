import com.sirius.logging_config
import logging

from com.sirius.numbers.Permutator import Permutator

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    num = Permutator()
    num.register_set("1", [1, 2, 3, 4])
    permutations = num.get_permutations([1,2,3,4])
    for pm in permutations :
        logger.info("Generated permutation %s", str(pm))
        
    logger.info(num.get_sum("1"))

    newPermutations = num.adjust_permutation("1", -1)
    for pm in newPermutations :
        logger.info("New permutation %s", str(pm))


