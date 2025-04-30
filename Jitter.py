import sys
import subprocess
import importlib.util

# List of required packages
required_packages = ['scapy', 'numpy']

# Function to check if a package is installed
def check_and_install(package):
    if importlib.util.find_spec(package) is None:
        choice = input(f"Package '{package}' is not installed. Install it now? (Y/N): ").strip().lower()
        if choice == 'y':
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        else:
            print(f"Cannot continue without installing '{package}'. Exiting.")
            sys.exit(1)

# Check all required packages
for pkg in required_packages:
    check_and_install(pkg)

# Now safe to import
from scapy.all import rdpcap, UDP
import numpy as np
import os

# Prompt user for pcap file
while True:
    pcap_path = input("Please enter the path to your PCAP file: ").strip()
    if os.path.isfile(pcap_path):
        break
    else:
        print("File does not exist. Please try again.")

# Load packets from PCAP file
packets = rdpcap(pcap_path)

# Filter for PTP packets (ports 319 and 320)
ptp_packets = [pkt for pkt in packets if UDP in pkt and (pkt[UDP].sport in [319, 320] or pkt[UDP].dport in [319, 320])]

if len(ptp_packets) < 2:
    print("Not enough PTP packets found to calculate jitter. Exiting.")
    sys.exit(1)

# Extract the timestamps
timestamps = [float(pkt.time) for pkt in ptp_packets]

# Calculate inter-arrival times
inter_arrival_times = np.diff(timestamps)

# Calculate jitter as the standard deviation of inter-arrival times
jitter = np.std(inter_arrival_times)

print("\n--- Jitter Calculation Results ---")
print(f"Number of PTP packets analyzed: {len(timestamps)}")
print(f"Mean inter-arrival time: {np.mean(inter_arrival_times)*1000:.3f} ms")
print(f"Calculated jitter: {jitter*1000:.3f} ms")
