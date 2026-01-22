VULNERABILITY_DB = {
    'sql_injection': {
        'name': 'SQL Injection',
        'severity': 'CRITICAL',
        'description': 'User input directly used in SQL query',
        'example': 'cursor.execute(f"SELECT * FROM users WHERE id={user_id}")',
        'fix': 'Use parameterized queries: cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))'
    },
    'command_injection': {
        'name': 'Command Injection',
        'severity': 'CRITICAL',
        'description': 'User input passed to system command',
        'example': 'os.system(f"ping {user_input}")',
        'fix': 'Use subprocess with list arguments: subprocess.run(["ping", user_input])'
    },
    'hardcoded_secrets': {
        'name': 'Hard-coded Credentials',
        'severity': 'HIGH',
        'description': 'Secrets stored directly in code',
        'example': 'API_KEY = "sk-1234567890"',
        'fix': 'Use environment variables: API_KEY = os.getenv("API_KEY")'
    },
    'path_traversal': {
        'name': 'Path Traversal',
        'severity': 'MEDIUM',
        'description': 'File path not validated',
        'example': 'open(user_filename)',
        'fix': 'Validate path: os.path.abspath() and check if in allowed directory'
    }
}

def get_vulnerability_details(vuln_type):
    return VULNERABILITY_DB.get(vuln_type.lower().replace(' ', '_'))