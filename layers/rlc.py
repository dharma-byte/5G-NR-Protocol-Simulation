class RLC:
    def __init__(self, logger):
        self.logger = logger

    def process(self, packet):
        self.logger.info("[RLC] Segmenting packet")

        segments = []
        chunk_size = 5

        for i in range(0, len(packet.data), chunk_size):
            segment_data = packet.data[i:i+chunk_size]
            seq = i // chunk_size
            segments.append((seq, segment_data))  # 👈 store sequence

        return segments