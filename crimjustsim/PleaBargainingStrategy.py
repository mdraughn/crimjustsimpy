from abc import abstractmethod
from crimjustsim import Docket


class PleaBargainingStrategy:

    @abstractmethod
    def bargain(self, docket:Docket):
        """
        Compute plea bargaining for the entire docket.
        :param docket:
        :return:
        """
        pass
