import unittest
from code_analyzer import CodeAnalyzer

class TestCodeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = CodeAnalyzer()
    
    def test_sql_injection_detection(self):
        code = 'cursor.execute(f"SELECT * FROM users WHERE id={user_id}")'
        issues = self.analyzer.detect_security_patterns(code)
        self.assertTrue(any('SQL Injection' in i['type'] for i in issues))
    
    def test_command_injection_detection(self):
        code = 'os.system(user_input)'
        issues = self.analyzer.detect_security_patterns(code)
        self.assertTrue(len(issues) > 0)
    
    def test_hardcoded_secrets_detection(self):
        code = 'API_KEY = "secret123"'
        issues = self.analyzer.detect_security_patterns(code)
        self.assertTrue(any('Secret' in i['type'] for i in issues))

if __name__ == '__main__':
    unittest.main()