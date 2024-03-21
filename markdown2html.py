#!/usr/bin/python3
"""an argument with first argument a markdown and the second
    argument is the output file name
"""


import sys
import os.path
import markdown2

if __name__ == "__main__":
    """run the code"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
        
    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)
        
    with open(sys.argv[1]) as read:
        with open(sys.argv[2], 'w') as html:
            for line in read:
                length = len(line)
                heading = line.lstrip('#')
                heading_no = length - len(heading)
                
                if 1 <= heading_no <= 6:
                    line = '<h{}>'.format(
                        heading_no) + heading.strip() + '</h{}>\n'.format(
                        heading_no)
                        
                if length > 1:
                    html.write(line)
            
    
    exit(0)