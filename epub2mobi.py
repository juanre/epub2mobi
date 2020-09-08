#!/usr/bin/env python

import os
from functools import reduce


def epub2mobi(fromdir, todir, ignore_if=None):
    """Look for .epub files in fromdir, convert them to .mobi and store 
    them in the flat directory todir unless their path includes any string
    present in the list ignore_if. 

    Requires ebook-convert, coming from calibre (http://calibre-ebook.com). 
    Go to Preferences, select Miscellaneous in Advanced, and click the 
    "Install command line tools" button.
    """
    if not os.path.exists(todir):
        os.makedirs(todir)
    for root, dirs, files in os.walk(fromdir):
        ignore = False
        if ignore_if is not None:
            ignore = reduce(lambda a, b: a or b,
                            [ig in root for ig in ignore_if])
        if not ignore:
            for fl in files:
                nm, ext = os.path.splitext(fl)
                if ext == '.epub':
                    mobi = os.path.join(todir, nm + '.mobi')
                    if not os.path.exists(mobi):
                        os.system('ebook-convert ' +
                                  os.path.join(root, fl) + ' ' + mobi)


if __name__ == '__main__':
    import sys
    fromdir, todir = '.', 'kindle'
    if len(sys.argv) > 1:
        fromdir = sys.argv[1]
    if len(sys.argv) == 3:
        todir = sys.argv[2]
    epub2mobi(fromdir, todir, ignore_if=['ninios'])
