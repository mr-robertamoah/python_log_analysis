import re


def extract_requests_per_endpoint(log_file_path):
    # Matches all requests and captures the endpoint
    endpoint_pattern = r'"(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS) (.+?) HTTP/\d\.\d"'
    endpoints = {}

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(endpoint_pattern, line)
                if match:
                    endpoint = match.group(2)
                    endpoints[endpoint] = endpoints.get(endpoint, 0) + 1

        return endpoints
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Error processing log file: {e}")
        return {}

def main():
    log_file_path = './NodeJsApp.log'  # Replace with your log file path
    endpoints = extract_requests_per_endpoint(log_file_path)

    if endpoints:
        print("Requests per endpoint:")
        endpoints = sorted(endpoints.items(), key=lambda x: x[1], reverse=True)
        print(f"{'Endpoint':<50} {'Count':<10}")
        print("-" * 60)
        for endpoint, count in endpoints:
            print(f"{endpoint:<50} {count:<10}")
    else:
        print("No endpoints found or an error occurred.")


if __name__ == "__main__":
    main()