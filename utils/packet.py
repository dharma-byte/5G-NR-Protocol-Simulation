class Packet:
    def __init__(self, data, seq):
        self.data = data
        self.seq = seq
        self.timestamp = None