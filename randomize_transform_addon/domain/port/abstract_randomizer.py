class AbstractRandomizer(object):

    @classmethod
    def get_random_number(cls, min_value, max_value):
        raise NotImplementedError()