class Case:
    """
    Represents a case working its way through the justice system
    """
    def __init__(self, *, id:int, prob_convict: float, docket=None):
        """
        :param prob_convict: Probability of a conviction at trial.
        """
        assert 0 <= prob_convict <= 1
        self.docket = docket
        self.id = id
        self.prob_convict = prob_convict
        self.sentence_if_convicted = 60.0

        # State of progress through the system.
        self.time_entered = None
        self.plead:bool = False
        self.time_plead = None
        self.tried:bool = False
        self.acquitted:bool = False
        self.convicted:bool = False
        self.guilty:bool = False
        self.time_tried = None
        self.sentence:int = None
        self.time_released = None
