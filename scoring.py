class SecurityScorer:
    SEVERITY_WEIGHTS = {
        'CRITICAL': 10,
        'HIGH': 7,
        'MEDIUM': 4,
        'LOW': 2
    }
    
    ISSUE_SEVERITY = {
        'SQL Injection Risk': 'CRITICAL',
        'Command Injection': 'CRITICAL',
        'Hard-coded Secrets': 'HIGH',
        'Unsafe Deserialization': 'HIGH',
        'Path Traversal': 'MEDIUM'
    }
    
    def calculate_score(self, issues):
        if not issues:
            return 100, 'A+'
        
        total_deductions = 0
        for issue in issues:
            severity = self.ISSUE_SEVERITY.get(issue['type'], 'LOW')
            total_deductions += self.SEVERITY_WEIGHTS[severity]
        
        score = max(0, 100 - total_deductions)
        grade = self.get_grade(score)
        
        return score, grade
    
    def get_grade(self, score):
        if score >= 90: return 'A+'
        if score >= 80: return 'A'
        if score >= 70: return 'B'
        if score >= 60: return 'C'
        if score >= 50: return 'D'
        return 'F'
    
    def get_risk_level(self, score):
        if score >= 80: return 'LOW'
        if score >= 60: return 'MEDIUM'
        if score >= 40: return 'HIGH'
        return 'CRITICAL'