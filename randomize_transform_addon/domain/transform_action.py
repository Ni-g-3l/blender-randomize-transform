from randomize_transform_addon.domain.port.abstract_randomizer import AbstractRandomizer

class BaseRandomAction(object):

    randomizer = AbstractRandomizer

    @classmethod
    def _randomize_value_if_enabled(cls, transform_property, default_value):
        if transform_property.enabled:
            return cls.randomizer.get_random_number(transform_property.range.min, transform_property.range.max)
        return default_value

    @classmethod
    def execute(cls, obj, transform_property):
        raise NotImplementedError()

class RandomizeLocationAction(BaseRandomAction):

    @classmethod
    def execute(cls, obj, transform_property):
        obj.location.x = cls._randomize_value_if_enabled(transform_property.x, obj.location.x)
        obj.location.y = cls._randomize_value_if_enabled(transform_property.y, obj.location.y)
        obj.location.z = cls._randomize_value_if_enabled(transform_property.z, obj.location.z)

class RandomizeRotationAction(BaseRandomAction):

    class EulerRotationContextCreator():

        PIE = 3.14

        def __init__(self, transform_property) -> None:
            self._transform_property = transform_property

        def __enter__(self):
            self._transform_property.x.range.min = self._transform_property.x.range.min * self.PIE/180
            self._transform_property.x.range.max = self._transform_property.x.range.max * self.PIE/180

            self._transform_property.y.range.min = self._transform_property.y.range.min * self.PIE/180
            self._transform_property.y.range.max = self._transform_property.y.range.max * self.PIE/180

            self._transform_property.z.range.min = self._transform_property.z.range.min * self.PIE/180
            self._transform_property.z.range.max = self._transform_property.z.range.max * self.PIE/180

        def __exit__(self, type, value, traceback):
            self._transform_property.x.range.min = self._transform_property.x.range.min * 180/self.PIE
            self._transform_property.x.range.max = self._transform_property.x.range.max * 180/self.PIE

            self._transform_property.y.range.min = self._transform_property.y.range.min * 180/self.PIE
            self._transform_property.y.range.max = self._transform_property.y.range.max * 180/self.PIE

            self._transform_property.z.range.min = self._transform_property.z.range.min * 180/self.PIE
            self._transform_property.z.range.max = self._transform_property.z.range.max * 180/self.PIE

    @classmethod
    def execute(cls, obj, transform_property):
        with cls.EulerRotationContextCreator(transform_property):
            obj.rotation_euler.x = cls._randomize_value_if_enabled(transform_property.x, obj.rotation_euler.x)
            obj.rotation_euler.y = cls._randomize_value_if_enabled(transform_property.y, obj.rotation_euler.y)
            obj.rotation_euler.z = cls._randomize_value_if_enabled(transform_property.z, obj.rotation_euler.z)


class RandomizeScaleAction(BaseRandomAction):

    @classmethod
    def execute(cls, obj, transform_property):
        obj.scale.x = cls._randomize_value_if_enabled(transform_property.x, obj.scale.x)
        obj.scale.y = cls._randomize_value_if_enabled(transform_property.y, obj.scale.y)
        obj.scale.z = cls._randomize_value_if_enabled(transform_property.z, obj.scale.z)
