import argparse
import os
import json
import sys

def parse_args(argv):
    parser = argparse.ArgumentParser("Test")
    parser.add_argument("--port", "-p", type=int, default=8080, help="Specify the port recordpeeker runs on")
    parser.add_argument("--verbosity", "-v", default=0, type=int, choices=[0,1,2,3])
    return parser.parse_args(argv[1:])

def launch():
    script = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mitmdump_input.py')

    # This is just here so that --help returns the arguments
    args = parse_args(sys.argv)
    arglist = " ".join(sys.argv[1:])
    sys.argv = [sys.argv[0], '-s "{0}" "{1}"'.format(script, arglist), '-q']
    from libmproxy.main import mitmdump
    mitmdump()

if __name__ == '__main__':
    launch()

