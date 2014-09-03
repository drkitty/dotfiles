#!/usr/bin/env python2

from __future__ import unicode_literals
from os import chdir, path, symlink
from sys import stdout, stderr

from file_list import file_list


def main(dry_run):
    chdir('files')
    for name, directory in file_list.iteritems():
        directory = path.expanduser(directory)
        target = path.relpath(name, directory)
        link_name = path.abspath(path.join(directory, name))
        stdout.write('{} --> {}\n'.format(target, link_name))
        if not dry_run:
            try:
                symlink(target, link_name)
            except OSError as e:
                if e.errno != 17:  # File exists
                    raise
                stderr.write('WARNING: {} exists\n'.format(link_name))


if __name__ == '__main__':
    from sys import argv
    dry_run = len(argv) == 2 and argv[1] == '-n'
    main(dry_run)
