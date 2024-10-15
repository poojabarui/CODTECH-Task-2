# Importing necessary libraries
import nmap  
import socket  # Python module for networking functions

# Function to scan open ports and check software versions
def scan_ports_and_versions(target):
    """rrr
    Scans for open ports and checks software versions on the target.1
    """
    # Initializing the Nmap PortScanner
    nm = nmap.PortScanner()
    print(f"Scanning {target} for open ports and software versions...")

    # Scan the target with service version detection (-sV) for ports 1-1024
    nm.scan(target, '1-1024', '-sV')


    # Iterate over all hosts detected during the scan
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")  # Print the host and its hostname
        print(f"State: {nm[host].state()}")  # Print whether the host is 'up' or 'down'

        # Iterate through all protocols (e.g., TCP, UDP) discovered on the host
        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")  # Print the protocol type
            ports = nm[host][proto].keys()  # Get all the ports scanned for this protocol
            
            # Iterate over all ports and retrieve information about each port
            for port in ports:
                state = nm[host][proto][port]['state']  # Get the port state (open, closed, filtered)
                name = nm[host][proto][port]['name']  # Get the service name on the port
                version = nm[host][proto][port].get('version', 'unknown')  # Get software version (if available)
                product = nm[host][proto][port].get('product', 'unknown')  # Get the software product (if available)

                # Print information about each open port
                print(f"Port: {port}, State: {state}")
                print(f"Service: {name}, Product: {product}, Version: {version}")

                # Additional logic for version comparison or checking outdated software can be added here


# Function to resolve a URL or hostname to an IP address
def resolve_target(target):
    """
    Resolves a target URL or IP address to its IP address.
    """
    try:
        # Resolve the target (hostname or URL) to its IP address using DNS lookup
        ip = socket.gethostbyname(target)
        print(f"Target IP address: {ip}")  # Print the resolved IP address
        return ip  # Return the resolved IP address
    except socket.gaierror:
        # Handle the error if the hostname could not be resolved
        print("Error: Unable to resolve the host.")
        return None  # Return None if the resolution fails


# Main function to perform vulnerability scanning
def vulnerability_scan(target):
    """
    Main function to perform a vulnerability scan for open ports and software versions.
    """
    # Resolve the target to an IP address
    ip = resolve_target(target)
    
    # If IP resolution is successful, proceed with scanning ports and versions
    if ip:
        scan_ports_and_versions(ip)


# Entry point of the script
if __name__ == "__main__":
    # Ask the user for a target (URL or IP address)
    target = input("Enter the target (URL or IP address): ")
    vulnerability_scan(target)  # Perform the vulnerability scan on the provided target




