import argparse
import os
import json
from subprocess import call
import sys

def parse_args(argv):
    parser = argparse.ArgumentParser("Test")
    parser.add_argument("--port", "-p", type=int, default=8080, help="Specify the port recordpeeker runs on")
    parser.add_argument("--verbose", "-v", default=False, action="store_true")
    parser.add_argument("--single-process", "-s", default=False, action="store_true", help=argparse.SUPPRESS)
    return parser.parse_args(argv[1:])

def launch():
    script = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mitmdump_input.py')

    # This is just here so that --help returns the arguments
    args = parse_args(sys.argv)
    arglist = " ".join(sys.argv[1:])
    if args.single_process:
        sys.argv = [sys.argv[0], '-s "{0}" "{1}"'.format(script, arglist), '-q']
        from libmproxy.main import mitmdump
        mitmdump()
    else:
        command = [sys.executable, 'mitmdump_shim.py', '-s "{0}" "{1}"'.format(script, arglist), '-q']
        call(command)

if __name__ == '__main__':
    launch()

