import time

class MAC:
    def __init__(self, logger):
        self.logger = logger

    def schedule(self, segments):
        self.logger.info("[MAC] Scheduling transmission")
        time.sleep(0.1)
        return segments