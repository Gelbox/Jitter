# Jitter

PTP Jitter Analyzer

This Python script analyzes a PCAP file to calculate jitter for Precision Time Protocol (PTP) packets (UDP ports 319 and 320). It is intended for users who need to evaluate network timing precision in environments where PTP is used.
Features

    Automatically checks for required Python packages (scapy, numpy) and prompts for installation if missing.

    Prompts the user to input a valid PCAP file path.

    Extracts UDP packets on PTP-specific ports (319, 320).

    Calculates:

        Inter-arrival times between packets

        Mean inter-arrival time

        Jitter (as the standard deviation of inter-arrival times)

Requirements

    Python 3.x

    scapy

    numpy

These packages will be installed automatically if not present.
Usage

Run the script in a terminal:

You will be prompted to enter the path to your .pcap file. The script will then analyze the file and print jitter statistics.
