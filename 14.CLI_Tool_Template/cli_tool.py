import argparse
import sys

# STRATEGY: Command Line Interfaces (CLI) & Arguments
# "Create a tool that I can run like: python tool.py --input file.txt --verbose"
# Concepts: argparse library, flags, help messages, input validation.
# This script is a template for ANY CLI tool.

def process_args():
    # 1. Setup the parser
    parser = argparse.ArgumentParser(description="A Simple CLI Text Processor")
    
    # 2. Add arguments
    # Positional argument (required)
    parser.add_argument("text", type=str, help="The string of text to process")
    
    # Optional flag (boolean)
    parser.add_argument("-u", "--upper", action="store_true", help="Convert text to UPPERCASE")
    
    # Optional flag (boolean)
    parser.add_argument("-r", "--reverse", action="store_true", help="Reverse the text")
    
    # Optional argument with value
    parser.add_argument("-n", "--repeat", type=int, default=1, help="Number of times to repeat the text")

    # 3. Parse arguments
    args = parser.parse_args()
    return args

def main():
    # If no args provided, print help (easier for demo purposes)
    if len(sys.argv) == 1:
        # Simulate running with --help
        sys.argv.append('--help')
    
    args = process_args()
    
    result = args.text
    
    if args.upper:
        result = result.upper()
        
    if args.reverse:
        result = result[::-1]
        
    print(f"\nOutput:\n{(result + ' ') * args.repeat}")

if __name__ == "__main__":
    # Try running in terminal: 
    # python cli_tool.py "hello world" -u -r -n 3
    main()
