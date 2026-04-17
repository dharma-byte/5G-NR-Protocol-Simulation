import random
import time

class Channel:
    def __init__(self, logger):
        self.logger = logger

    def transmit(self, segments):
        """
        Simulates transmission over a channel with packet loss.

        Args:
            segments: List of tuples (seq, data)

        Returns:
            received: successfully received segments
            lost: lost segments
        """

        received = []
        lost = []

        for seq, seg in segments:
            # Simulate packet loss (20%)
            if random.random() > 0.2:
                time.sleep(0.05)  # simulate latency
                self.logger.info(f"[Channel] Packet received: {seg}")
                received.append((seq, seg))
            else:
                self.logger.warning(f"[Channel] Packet lost: {seg}")
                lost.append((seq, seg))

        return received, lost