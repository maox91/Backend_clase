from abc import ABCMeta

class AbstractModel(metaclass=ABCMeta):

    def __int__(self, data: dict):
        """
        this method is a contructor where a dict is parsed to an object
        :param data:
        :return:
        """
        for key, value in data.items():
            setattr(self, key, value)