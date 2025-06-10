#!/usr/bin/env python3
import re
import datetime

log_pattern = r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z) (\d+\.\d+\.\d+\.\d+)'


def get_list_of_ips_and_timestamps(log_file_path):

    try:
        with open(log_file_path, 'r') as file:
            ip_timestamps = []
            for line in file:
                # Extract timestamp and IP address
                match = re.search(log_pattern, line)
                if match:
                    timestamp_str, ip_address = match.groups()
                    timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                    ip_timestamps.append((ip_address, timestamp))
            return ip_timestamps
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
        return []

def get_lowest_timestamp(ip_address, ips_and_timestamps):
    
    lowest_timestamp = None
    for ip, timestamp in ips_and_timestamps:
        if ip == ip_address:
            if lowest_timestamp is None or timestamp < lowest_timestamp:
                lowest_timestamp = timestamp
    return lowest_timestamp

def analyze_log_file(log_file_path):
    
    ip_hits = {}
    try:
            
        ips_and_timestamps = get_list_of_ips_and_timestamps(log_file_path)

        for ip_address, timestamp in ips_and_timestamps:
            if ip_address in ip_hits:
                continue

            lowest_timestamp = get_lowest_timestamp(ip_address, ips_and_timestamps)
            # If this is the first hit, set the start time and calculate end time
            ip_hits[ip_address] = get_ip_hits(lowest_timestamp, lowest_timestamp + datetime.timedelta(seconds=10), ip_address, ips_and_timestamps)

        return ip_hits
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
    except Exception as e:
        print(f"Error processing log file: {e}")

def get_ip_hits(start_timpestamp, end_timestamp, ip, ips_and_timestamps):
    
    # Dictionary to store hits per IP address
    ip_hits = 0
    
    try:
        for ip_address, timestamp in ips_and_timestamps:
                
            # Count hits within the 10-second window
            if timestamp <= end_timestamp and timestamp >= start_timpestamp and ip_address == ip:
                ip_hits += 1
            else:
                # We've gone beyond our 10-second window, no need to process further
                continue

        return ip_hits - 1  # Subtract 1 because we're not counting the first hit
        
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
    except Exception as e:
        print(f"Error processing log file: {e}")

if __name__ == "__main__":
    log_file_path = "./NodeJsApp.log"
    hits = analyze_log_file(log_file_path)

    print("\nFinal Hits Dictionary:")
    print("=" * 50)
    for ip, count in hits.items():
        print(f"{ip}: {count} hits")
    print("=" * 50)