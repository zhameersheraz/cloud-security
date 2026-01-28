import anthropic
import os

class AIReviewer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("API key not found. Set ANTHROPIC_API_KEY environment variable or pass api_key parameter.")
        
        try:
            self.client = anthropic.Anthropic(api_key=self.api_key)
        except Exception as e:
            raise ValueError(f"Failed to initialize AI client: {str(e)}")
    
    def review_code(self, code, filename):
        if not code or not code.strip():
            return "Error: Empty code provided for analysis"
        
        prompt = f"""Analyze this Python code for security vulnerabilities and code quality issues.

Filename: {filename}

Code:
```python
{code}
```

Provide:
1. Security vulnerabilities (if any)
2. Code quality issues
3. Best practice violations
4. Suggestions for improvement

Be specific and reference line numbers when possible."""

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            if not message.content:
                return "Error: AI returned empty response"
            
            return message.content[0].text
        
        except anthropic.APIError as e:
            return f"API Error: {str(e)}"
        except Exception as e:
            return f"Error calling AI API: {str(e)}"