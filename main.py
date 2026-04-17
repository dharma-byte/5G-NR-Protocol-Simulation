from layers.pdcp import PDCP
from layers.rlc import RLC
from layers.mac import MAC
from simulation.channel import Channel
from utils.logger import setup_logger

import time

logger = setup_logger()

pdcp = PDCP(logger)
rlc = RLC(logger)
mac = MAC(logger)
channel = Channel(logger)

data = "HELLO_5G_NETWORK_SIMULATION"
seq = 1

logger.info("Starting 5G Simulation")

# ⏱ Start timing
start_time = time.time()

# Step 1: PDCP
packet = pdcp.process(data, seq)

# Step 2: RLC
segments = rlc.process(packet)

# Step 3: MAC
scheduled = mac.schedule(segments)

# Step 4: Channel Transmission
received, lost = channel.transmit(scheduled)

# Step 5: Retransmission (until all received)
while lost:
    logger.info(f"Retransmitting lost packets: {lost}")
    received_new, lost = channel.transmit(lost)
    received.extend(received_new)

# Step 6: Sort by sequence
received.sort(key=lambda x: x[0])
ordered_data = [seg for _, seg in received]

logger.info(f"Final Received Data: {ordered_data}")

# Step 7: Reconstruct message
final_message = ''.join(ordered_data)
logger.info(f"Reconstructed Message: {final_message}")

# ⏱ End timing
end_time = time.time()

# Step 8: Metrics
latency = end_time - start_time
throughput = len(final_message) / latency

logger.info(f"Latency: {latency:.4f} sec")
logger.info(f"Throughput: {throughput:.2f} chars/sec")