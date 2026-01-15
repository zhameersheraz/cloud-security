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

if __name__ == "__main__":
    analyzer = CodeAnalyzer()
    
    test_file = input("Enter Python file path: ")
    try:
        info = analyzer.get_file_info(test_file)
        print("\nFile Analysis:")
        print(f"Path: {info['filepath']}")
        print(f"Lines: {info['lines']}")
        print(f"Characters: {info['characters']}")
        print(f"Empty lines: {info['empty_lines']}")
    except Exception as e:
        print(f"Error: {e}")