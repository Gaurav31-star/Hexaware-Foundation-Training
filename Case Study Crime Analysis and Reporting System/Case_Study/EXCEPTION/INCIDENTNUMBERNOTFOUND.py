class IncidentNumberNotFoundException(Exception):
    def __init__(self, msg="Incident id not found"):
        self.msg = msg
        super().__init__(msg)
