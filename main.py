import argparse
from code_analyzer import CodeAnalyzer
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(
        description='CodeGuard AI - Intelligent Code Security Analyzer'
    )
    parser.add_argument('file', help='Python file to analyze')
    parser.add_argument('--ai', action='store_true', help='Enable AI-powered analysis')
    parser.add_argument('--output', '-o', help='Output report file')
    parser.add_argument('--api-key', help='Anthropic API key')
    
    args = parser.parse_args()
    
    print("CodeGuard AI - Starting Analysis...")
    print(f"Target: {args.file}")
    
    analyzer = CodeAnalyzer()
    result = analyzer.full_analysis(
        args.file, 
        use_ai=args.ai, 
        api_key=args.api_key
    )
    
    generator = ReportGenerator()
    report = generator.generate_text_report(result)
    
    print("\n" + report)
    
    if args.output:
        generator.save_report(report, args.output)

if __name__ == "__main__":
    main()