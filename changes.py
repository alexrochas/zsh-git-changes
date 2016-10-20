import re
import subprocess
import os

import sys


def verbose():
    if '-v' in sys.argv:
        return True
    return False


def fetch_reflog(cmd):
    if verbose():
        print('Reflog in %s' % cmd)
    output = subprocess.check_output('git -C {}/ reflog | cat'.format(cmd), shell=True)
    if verbose():
        print('Received reflog %s' % output)
    return output.decode('utf-8')


def parse_reflog(reflog):
    if verbose():
        print('Parsing %s' % reflog)
    groups = re.compile('\s*(.*)\sHEAD@{(\d)}:\s(.*):\s.*').findall(reflog)
    if groups:
        return groups
    return None


def build_hash_range(reflog_groups):
    hashes = [h[0] for h in reflog_groups]
    return "{}..{}".format(hashes[1], hashes[0])


def call_diff(hash_range):
    subprocess.call(['git', 'difftool', hash_range])


if __name__ == '__main__':
    print 'Looking for changes between the last two commits.'
    cmd = os.getcwd()
    reflog = fetch_reflog(cmd)
    hashes = parse_reflog(reflog)
    hash_range = build_hash_range(hashes)
    call_diff(hash_range)
