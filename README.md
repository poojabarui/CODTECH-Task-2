# CODTECH-Task-2
Vulnerabilty, port scaaning tool for scan ip address

<pre>
NAME : POOJA BARUI
COMPANY : CODTECH IT SOLUTIONS
INTERN ID : CT6WDS1952
DOMAIN : CYBER SECURITY & ETHICAL HACKING
DURATION : SEPTEMBER 20TH,2024 TO NOVEMBER 5TH,2024
</pre>

# Project Title: VULNERABILITY SCANNING TOOL

Overview: 
The VULNERABILITY SCANNING TOOL is a Python-based tool designed to scan a target (either a URL or an IP address) for open ports and identify the software running on them. It uses the nmap library for network scanning and attempts to detect software versions. This helps users assess the security status of a system by finding potential vulnerabilities in running services.

# Project Goals: 
• Port Scanning: Identify open ports on the target system. 
• Service and Version Detection: Detect the service running on each open port and its software version.
• Protocol Handling: Support multiple protocols (like TCP and UDP) during scanning. 
• Target Resolution: Convert hostnames or URLs into IP addresses for scanning.

# Prerequisites: 
• Python 3.x 
• nmap library (can be installed via pip)
• Nmap installed on the system (can be downloaded from nmap.org)

# Installation:

Install Python 3.x if not already installed.
Install the required Python package using the following command:
pip install python-nmap 3. Ensure Nmap is installed on your system by downloading it from Nmap's website or installing it using a package manager (e.g., sudo apt install nmap for Ubuntu).

# Usage:

Run the script in your terminal: python vulnerability_scanner.py

Enter the target (either a URL or an IP address) when prompted. Enter the target (URL or IP address): example.com

View the scan results which include: o Target IP address o Host status (up or down) o Protocol type (TCP, UDP, etc.) o Open ports and the services running on them o Software products and their versions (if detected)

Example Output: Enter the target (URL or IP address): example.com Target IP address: 93.184.216.34 Scanning 93.184.216.34 for open ports and software versions...

Host: 93.184.216.34 (example.com) State: up

Protocol: tcp Port: 80, State: open Service: http, Product: Apache, Version: 2.4.41 Port: 443, State: open Service: https, Product: OpenSSL, Version: 1.1.1

# Project Structure:

Main Functions: o scan_ports_and_versions(target): • Scans the target for open ports and running services using Nmap’s service version detection. • Outputs the detected services and their versions on open ports.

o resolve_target(target): • Converts a URL or hostname to its corresponding IP address using a DNS lookup.

o vulnerability_scan(target): • Main function to conduct the full vulnerability scan. It first resolves the target’s hostname to an IP, then calls the port scanning function.

# User Input: o The script prompts the user to input a URL or IP address for scanning.

# Key Features: 
• Port Scanning: Scans for open ports in the range 1-1024 using Nmap’s service version detection (-sV). 
• Protocol Handling: Supports both TCP and UDP protocols. 
• Service Detection: Identifies the type of service (e.g., HTTP, FTP) running on each port. 
• Software Version Detection: Retrieves the software product and version running on open ports (if available).
• Hostname Resolution: Automatically resolves URLs or hostnames to IP addresses using Python’s socket module.

# Code Walkthrough:

• Import Libraries: o nmap: To conduct network scanning. o socket: To perform DNS lookups and resolve target hostnames into IP addresses.

# Functions:

scan_ports_and_versions(target):  Initializes the Nmap scanner and scans ports 1-1024 using the -sV option (service version detection).  Loops through the detected hosts, ports, and protocols to retrieve information about open ports and their running services.

resolve_target(target):  Resolves the hostname or URL into an IP address using socket.gethostbyname().  Returns the IP address or handles errors if the hostname cannot be resolved.

vulnerability_scan(target):  The main function that coordinates the entire process:  First resolves the target's hostname to an IP address.  Then scans the resolved IP for open ports and services.

• Entry Point: o if name == "main": block handles the input prompt and calls the main scanning function.

Future Improvements: • Extended Port Range: Allow the user to specify a custom port range for scanning instead of the default 1-1024. • HTML/CSV Report Generation: Generate detailed scan reports in HTML or CSV format for later review. • Service Vulnerability Database: Compare the detected software versions with known vulnerabilities (e.g., via a CVE database). • Multi-threaded Scanning: Optimize performance by enabling multi-threaded or asynchronous scanning. • Authentication Support: Add authentication methods for scanning internal or protected networks.

Conclusion:

The Network Vulnerability Scanner is a simple yet powerful tool for scanning network services and detecting vulnerabilities by identifying open ports and outdated software versions. It serves as a useful tool for system administrators, ethical hackers, and security professionals to assess the security status of networked systems.
