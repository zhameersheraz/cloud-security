import os

class CodeAnalyzer:
    def __init__(self):
        self.supported_extensions = ['.py']
    
    def read_file(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        if not any(filepath.endswith(ext) for ext in self.supported_extensions):
            raise ValueError(f"Unsupported file type. Supported: {self.supported_extensions}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def get_file_info(self, filepath):
        code = self.read_file(filepath)
        lines = code.split('\n')
        
        return {
            'filepath': filepath,
            'lines': len(lines),
            'characters': len(code),
            'empty_lines': sum(1 for line in lines if not line.strip())
        }
    
    def detect_security_patterns(self, code):
        issues = []
        lines = code.split('\n')
        
        patterns = {
            'SQL Injection Risk': ['execute(', 'executemany(', 'cursor.execute'],
            'Command Injection': ['os.system(', 'subprocess.call(', 'eval('],
            'Hard-coded Secrets': ['password =', 'api_key =', 'secret =', 'token ='],
            'Unsafe Deserialization': ['pickle.loads(', 'yaml.load('],
            'Path Traversal': ['open(', 'file(']
        }
        
        for line_num, line in enumerate(lines, 1):
            for issue_type, keywords in patterns.items():
                for keyword in keywords:
                    if keyword in line.lower():
                        issues.append({
                            'type': issue_type,
                            'line': line_num,
                            'code': line.strip(),
                            'severity': 'HIGH'
                        })
        
        return issues
    
    def full_analysis(self, filepath, use_ai=False, api_key=None):
        code = self.read_file(filepath)
        info = self.get_file_info(filepath)
        patterns = self.detect_security_patterns(code)
        
        result = {
            'file_info': info,
            'pattern_issues': patterns,
            'ai_review': None
        }
        
        if use_ai:
            from ai_reviewer import AIReviewer
            reviewer = AIReviewer(api_key)
            result['ai_review'] = reviewer.review_code(code, filepath)
        
        return result


if __name__ == "__main__":
    analyzer = CodeAnalyzer()
    
    test_file = input("Enter Python file path: ")
    try:
        analysis = analyzer.full_analysis(test_file)
        info = analysis['file_info']
        issues = analysis['pattern_issues']

        print("\nFile Analysis:")
        print(f"Path: {info['filepath']}")
        print(f"Lines: {info['lines']}")
        print(f"Characters: {info['characters']}")
        print(f"Empty lines: {info['empty_lines']}")
        
        print(f"\nSecurity Issues Found: {len(issues)}")
        for issue in issues:
            print(f"[{issue['severity']}] Line {issue['line']}: {issue['type']}")

        if analysis['ai_review']:
            print("\nAI Review:")
            print(analysis['ai_review'])
            
    except Exception as e:
        print(f"Error: {e}")
