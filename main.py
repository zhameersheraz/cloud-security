import argparse
import os
from code_analyzer import CodeAnalyzer
from report_generator import ReportGenerator

def analyze_directory(directory, use_ai=False, api_key=None):
    results = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    analyzer = CodeAnalyzer()
                    result = analyzer.full_analysis(filepath, use_ai, api_key)
                    results.append(result)
                    print(f"Analyzed: {filepath}")
                except Exception as e:
                    print(f"Error analyzing {filepath}: {e}")
    
    return results

def main():
    parser = argparse.ArgumentParser(
        description='CodeGuard AI - Intelligent Code Security Analyzer'
    )
    parser.add_argument('file', help='Python file or directory to analyze')
    parser.add_argument('--ai', action='store_true', help='Enable AI-powered analysis')
    parser.add_argument('--output', '-o', help='Output report file')
    parser.add_argument('--api-key', help='API key for AI analysis')
    parser.add_argument('--dir', action='store_true', help='Analyze entire directory')
    
    args = parser.parse_args()
    
    print("CodeGuard AI - Starting Analysis...")
    print(f"Target: {args.file}")
    
    if args.dir:
        if not os.path.isdir(args.file):
            print("Error: Path is not a directory")
            return
        
        results = analyze_directory(args.file, args.ai, args.api_key)
        print(f"\nAnalyzed {len(results)} files")
        
        for result in results:
            generator = ReportGenerator()
            report = generator.generate_text_report(result)
            print("\n" + report)
    else:
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