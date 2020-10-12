#!/usr/bin/env python3

from datetime import datetime
from pytz import timezone

def main():
    now = datetime.now(tz=timezone('America/Denver'))
    file_name = now.strftime('%m-%d-%Y-%H-%M')
    title = now.strftime('**%a %H:%M** [*%d-%m-%Y*]')
    post = open(f'{file_name}.md', 'w')
    post.write(f'### {title}\n')
    post.write(f'__Description__\n\n\n---')


if __name__ == '__main__':
    main()
