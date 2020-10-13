#!/usr/bin/env python3

import glob

from datetime import datetime
from pytz import timezone
from pathlib import Path

def main():
    md_f = glob.glob('notes/*.md')
    md_files = sorted(md_f, reverse=True)

    readme = open('README.md', 'w')
    header = open('header.md', 'r')
    readme.write(f'{header.read()}')
    for i in md_files:
        f = Path(i)
        readme.write(f'- [{f.stem}]({f})\n')

if __name__ == '__main__':
    main()
