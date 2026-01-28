# CodeGuard AI - Intelligent Code Security Analyzer

An AI-powered tool for analyzing Python code security vulnerabilities and code quality issues.

## Features

- **Pattern-Based Detection** - Identifies common security vulnerabilities
- **AI-Powered Analysis** - Uses advanced AI for intelligent code review
- **Security Scoring** - Grades code security from A+ to F
- **Detailed Reports** - Generates comprehensive analysis reports
- **Batch Processing** - Analyze entire directories
- **CLI Interface** - Easy command-line usage

## Installation
```bash
pip install anthropic pyyaml
```

Set your API key:
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

## Usage

### Basic Analysis
```bash
python main.py mycode.py
```

### With AI Review
```bash
python main.py mycode.py --ai
```

### Save Report
```bash
python main.py mycode.py --ai --output report.txt
```

### Analyze Directory
```bash
python main.py /path/to/project --dir --ai
```

## Security Checks

- SQL Injection
- Command Injection
- Hard-coded Secrets
- Unsafe Deserialization
- Path Traversal
- Code Quality Issues

## Scoring System

- **A+ (90-100)**: Excellent security
- **A (80-89)**: Good security
- **B (70-79)**: Acceptable
- **C (60-69)**: Needs improvement
- **D (50-59)**: Poor security
- **F (<50)**: Critical issues

## Example Report
```
============================================================
CodeGuard AI - Security Analysis Report
Generated: 2026-01-29 10:30:00
============================================================

File: example.py
Lines of Code: 45
Characters: 1234

[PATTERN DETECTION] Found 2 potential issues:

  [HIGH] SQL Injection Risk
  Line 23: cursor.execute(f"SELECT * FROM users WHERE id={user_id}")

  [HIGH] Hard-coded Secrets
  Line 5: API_KEY = "sk-1234567890"

[SECURITY SCORE]
Score: 86/100 (Grade: A)
Risk Level: LOW

[AI ANALYSIS]
The code contains several areas for improvement...

============================================================
```

## Author

**Zhameer Sheraz Tampugao**
Computer Science Student | Security Researcher in Training

Built in 2026 demonstrating:
- AI API integration
- Security analysis
- Python development
- Software engineering best practices

## Technologies

- Python 3.8+
- AI API (Anthropic)
- PyYAML (configuration)

## License

MIT License - Educational purposes

---

**Note:** This tool is for educational purposes. Always manually review security findings.
```

Create NEW file: `requirements.txt`
```
anthropic>=0.18.0
pyyaml>=6.0