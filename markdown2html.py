#!/usr/bin/python3
"""an argument with first argument a markdown and the second
    argument is the output file name
"""


import sys
import os.path

if __name__ == "__main__":
    """run the code"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
        
    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {sys.argv[1]}")
        sys.exit(1)
    
    exit(0)