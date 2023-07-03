import random

from randomize_transform_addon.domain.port.abstract_randomizer import AbstractRandomizer

class UniformRandomizer(AbstractRandomizer):

    @classmethod
    def get_random_number(cls, min_value, max_value):
        return random.uniform(min_value, max_value)