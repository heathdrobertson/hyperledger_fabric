#!/usr/bin/env python3

from datetime import datetime
from pytz import timezone
from pathlib import Path


def main():
    now = datetime.now(tz=timezone('America/Denver'))
    file_name = now.strftime('%m-%d-%Y-%H-%M')
    path_to_new_post = Path(f'notes/{file_name}.md')
    title = now.strftime('**%a %H:%M** [*%d-%m-%Y*]')
    post = open(path_to_new_post, 'w')
    post.write(f'### {title}\n')
    post.write(f'__Description__\n')
    post.write(f'[README](../README.md)\n\n\n\n')
    post.write(f'---\n')
    post.write(f'[README](../README.md)\n')


if __name__ == '__main__':
    main()
