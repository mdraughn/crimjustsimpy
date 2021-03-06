class ExperimentData:
    def __init__(self):
        self.dockets = []

    @property
    def cases(self):
        return [c for d in self.dockets for c in d.cases]

    @property
    def cases_plead(self):
        return [c for c in self.cases if c.plead]

    @property
    def cases_tried(self):
        return [c for c in self.cases if c.tried]

    @property
    def cases_decided(self):
        return [c for c in self.cases if c.tried or c.plead]

    @property
    def cases_acquitted(self):
        return [c for c in self.cases_tried if c.acquitted]

    @property
    def cases_convicted(self):
        return [c for c in self.cases_tried if c.convicted]

    @property
    def cases_guilty(self):
        return [c for c in self.cases if c.guilty]

    @property
    def cases_not_guilty(self):
        return [c for c in self.cases if not c.guilty]

    @property
    def sentences(self):
        return [c.sentence for c in self.cases_decided]
