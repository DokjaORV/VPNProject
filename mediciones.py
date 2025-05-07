from pythonping import ping

def ping_host(host):
    ping_result = ping(target=host, count=10, timeout=2)

    return {
        'host': host,
        'avg_latency': ping_result.rtt_avg_ms,
        'min_latency': ping_result.rtt_min_ms,
        'max_latency': ping_result.rtt_max_ms,
        'packet_loss': ping_result.packet_loss
    }

hosts = [
    '100.124.230.9',
    '100.113.73.88',
    '100.93.134.60',
    '100.113.141.37'
]

for host in hosts:
    print(ping_host(host))