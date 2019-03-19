import argparse
import sys

from stevedore import extension


def main():
    plugins = extension.ExtensionManager(
        namespace='fellow.plugins',
        invoke_on_load=True,
        invoke_args=(),
    )
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        choices=plugins.names(),
        help='the command to run',
    )
    args = parser.parse_args()
    items = dict(plugins.items())
    items.get(args.command).obj.run()


if __name__ == '__main__':
    sys.exit(main())
