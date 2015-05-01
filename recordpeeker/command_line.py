import os
import json
from subprocess import call

import click

@click.command()
@click.option('--port', '-p', default=8080, help='Specify the port recordpeeker runs on')
def launch(port):
    script = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mitmdump_input.py')

    args = dict(port=port)

    command = ['mitmdump', '-s {0} "{1}"'.format(script, args), '-q']
    call(command)

if __name__ == '__main__':
    launch()

