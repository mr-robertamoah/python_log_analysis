# Python Log Analysis

This repository contains scripts for analyzing web server logs to extract various metrics and insights.

## Log File

The log file used for analysis is located at:
```
./NodeJsApp.log
```

### Log Format

The log file follows this format:
```
<timestamp> <ip_address> - - [<date>:<time> +<timezone>] "<method> <endpoint> <protocol>" <status_code> <bytes> "<referrer>" "<user_agent>"
```

### Example Log Entry
```
2025-06-03T10:09:28.126Z 185.195.59.88 - - [03/Jun/2025:10:09:28 +0000] "GET / HTTP/1.1" 200 - "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15"
```

In this example:
- Timestamp: `2025-06-03T10:09:28.126Z`
- IP Address: `185.195.59.88`
- Date/Time: `03/Jun/2025:10:09:28 +0000`
- Request: `GET / HTTP/1.1`
- Status Code: `200`
- Bytes: `-` (not specified)
- Referrer: `-` (none)
- User Agent: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15`

## Scripts

### 1. 10-Second Window Analysis (`scripts/10_second_window.py`)

This script analyzes how many requests came in after the first request in a 10-second window for each IP address.

#### Usage
```bash
python3 scripts/10_second_window.py
```

#### Output
The script outputs a table showing each IP address and the number of requests that occurred within 10 seconds after its first request:
```
Final Hits Dictionary:
==================================================
192.168.1.1: 24 hits
10.0.0.1: 15 hits
...
==================================================
```

#### Potential Errors
- `FileNotFoundError`: If the log file is not found at the specified path
- Parsing errors if the log format doesn't match the expected pattern

### 2. User Agent Analysis (`scripts/request_per_user_agent.py`)

This script determines the number of requests from each user agent type.

#### Usage
```bash
python3 scripts/request_per_user_agent.py
```

#### Output
The script outputs a sorted list of user agents and their request counts:
```
Unique User Agents and their counts:
User Agent                                         Count     
------------------------------------------------------------
Mozilla/5.0 (X11; Linux x86_64)...                 150       
Mozilla/5.0 (Windows NT 10.0; Win64; x64)...       75        
...
```

#### Potential Errors
- `FileNotFoundError`: If the log file is not found at the specified path
- Regex matching errors if user agent format is unexpected

### 3. Endpoint Access Analysis (`scripts/request_per_endpoint.py`)

This script counts the number of times each endpoint was accessed.

#### Usage
```bash
python3 scripts/request_per_endpoint.py
```

#### Output
The script outputs a sorted list of endpoints and their access counts:
```
Requests per endpoint:
Endpoint                                           Count     
------------------------------------------------------------
/                                                  250       
/favicon.ico                                       180       
...
```

#### Potential Errors
- `FileNotFoundError`: If the log file is not found at the specified path
- Regex matching errors if request format is unexpected

## Common Issues

1. All scripts assume the log file is in the current directory. If the log file is elsewhere, you'll need to modify the `log_file_path` variable in each script.

2. The scripts are designed for a specific log format. If your logs have a different format, you may need to adjust the regular expressions used for parsing.

3. For large log files, these scripts may consume significant memory as they process the entire file at once.