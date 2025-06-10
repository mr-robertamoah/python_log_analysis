import re

pattern = r'"([^"]+)"$'
def extract_user_agents(log_file_path):
    user_agents = {}
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    user_agent = match.group(1)

                    user_agents[user_agent] = user_agents.get(user_agent, 0) + 1
                    
        return user_agents
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
        return set()
    except Exception as e:
        print(f"Error processing log file: {e}")
        return set()
def main():
    log_file_path = './NodeJsApp.log'  # Replace with your log file path
    user_agents = extract_user_agents(log_file_path)
    
    if user_agents:
        print("Unique User Agents and their counts:")
        user_agents = sorted(user_agents.items(), key=lambda x: x[1], reverse=True)
        print(f"{'User Agent':<50} {'Count':<10}")
        print("-" * 60)
        for user_agent, count in user_agents:
            print(f"{user_agent:<50} {count:<10}", '\n')
    else:
        print("No user agents found or an error occurred.")


if __name__ == "__main__":
    main()