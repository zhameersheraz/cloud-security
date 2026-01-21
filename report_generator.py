from datetime import datetime
from scoring import SecurityScorer

class ReportGenerator:
    def generate_text_report(self, analysis_result):
        report = []
        report.append("=" * 60)
        report.append("CodeGuard AI - Security Analysis Report")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 60)
        
        info = analysis_result['file_info']
        report.append(f"\nFile: {info['filepath']}")
        report.append(f"Lines of Code: {info['lines']}")
        report.append(f"Characters: {info['characters']}")
        
        patterns = analysis_result['pattern_issues']
        report.append(f"\n[PATTERN DETECTION] Found {len(patterns)} potential issues:")
        
        if patterns:
            for issue in patterns:
                report.append(f"\n  [{issue['severity']}] {issue['type']}")
                report.append(f"  Line {issue['line']}: {issue['code']}")
        else:
            report.append("  No issues detected")
        
        scorer = SecurityScorer()
        score, grade = scorer.calculate_score(patterns)
        risk = scorer.get_risk_level(score)
        
        report.append(f"\n[SECURITY SCORE]")
        report.append(f"Score: {score}/100 (Grade: {grade})")
        report.append(f"Risk Level: {risk}")
        
        if analysis_result['ai_review']:
            report.append("\n[AI ANALYSIS]")
            report.append(analysis_result['ai_review'])
        
        report.append("\n" + "=" * 60)
        return "\n".join(report)
    
    def save_report(self, report, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to: {output_file}")