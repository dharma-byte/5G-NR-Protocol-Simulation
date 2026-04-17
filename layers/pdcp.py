from utils.packet import Packet

class PDCP:
    def __init__(self, logger):
        self.logger = logger

    def process(self, data, seq):
        self.logger.info(f"[PDCP] Processing data: {data}")
        return Packet(data=data, seq=seq)