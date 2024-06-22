
from model import get_ip_address, check_https, traceroute, geolocate_ip
from view import print_ip_address, print_https_check, print_traceroute_output, print_hop_info, print_invalid_latency, plot_latency

def main():
    # Check IP Address
    ip_address = get_ip_address()
    print_ip_address(ip_address)

    # Check HTTPS for a common site
    url = "https://www.google.com"
    is_secure = check_https(url)
    print_https_check(url, is_secure)

    # Perform a traceroute
    traceroute_output = traceroute("www.google.com")
    print_traceroute_output(traceroute_output)

    # Analyze traceroute output
    hops = []
    latencies = []
    for line in traceroute_output:
        if line.startswith(" "):
            parts = line.split()
            if len(parts) >= 9:
                hop = parts[1]
                latency = parts[4]
                ip = parts[3]
                try:
                    latencies.append(float(latency.replace('ms', '')))
                    hops.append(hop)
                    country, description = geolocate_ip(ip)
                    print_hop_info(hop, ip, latency, country, description)
                except ValueError:
                    print_invalid_latency(line)

    # Plot latency
    if hops and latencies:
        plot_latency(hops, latencies)

if __name__ == "__main__":
    main()
