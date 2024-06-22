import matplotlib.pyplot as plt

# Use the 'Agg' backend for rendering plots in a headless environment
plt.switch_backend('Agg')

def print_ip_address(ip_address):
    print(f"Your IP address is: {ip_address}")

def print_https_check(url, is_secure):
    status = "secure (HTTPS)" if is_secure else "not secure (HTTP)"
    print(f"The connection to {url} is {status}.")

def print_traceroute_output(traceroute_output):
    for line in traceroute_output:
        print(line)

def print_hop_info(hop, ip, latency, country, description):
    print(f"Hop: {hop}, IP: {ip}, Latency: {latency}, Location: {country}, Description: {description}")

def print_invalid_latency(line):
    print(f"Skipping hop with invalid latency: {line}")

def plot_latency(hops, latencies):
    plt.figure(figsize=(10, 5))
    plt.plot(hops, latencies, marker='o')
    plt.title('Traceroute Latency')
    plt.xlabel('Hop')
    plt.ylabel('Latency (ms)')
    plt.grid(True)
    plt.savefig('latency_plot.png')  # Save the plot to a file
    plt.show()  # Ensure the plot is displayed

# Ensure interactive mode is enabled
plt.ion()
