#!/usr/local/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
Requirements:
If the number of arguments is less than 2: print in STDERR
Usage: ./markdown2html.py README.md README.html and exit 1
If the Markdown file doesnt exist: print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0
"""
import sys
from os.path import exists

def read_file(filename=''):
    ''' read file and keeps lines in an array'''
    cp_line = []
    with open(filename, encoding='utf8') as f:  # open(path_to_file, mode)
        for line in f:
            if line[0] == '#':
                md_to_html_headings(line, cp_line)
            return cp_line

def make_html(file='', cp_line=""):
    '''function that writes a string in a textfile filename'''
    with open(file,mode='r+', encoding='utf8') as f:
        for line in f:
            f.write(line)

def md_to_html_headings(md_line, cp_line):
    """convert Markdown headings to html"""
    level = md_line.count('#') #counts how many # are
    md_line = md_line.replace((('#' * level)+' '),('<h%s>' % level)) # str.replace(old, new, optional[maxim replaces])
    idx = md_line.find('\n')
    md_line = md_line[:idx] + '</h%s>' % level
    cp_line.append(md_line)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    md_file = sys.argv[1]
    html_file = sys.argv[2]
    if not exists(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]))
        exit(1)
    lines = read_file(md_file)
    make_html(html_file, lines)
