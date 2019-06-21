from server import ServerLinker
from argparse import ArgumentParser
from error import RaiseError


def main():
    parser = ArgumentParser(
        description="Simple Cloud-Storage File Transfer Program")
    parser.add_argument('--from', '-f', metavar='FROM')
    parser.add_argument('--to', '-t', metavar='TO')
    args, direction = parser.parse_known_args()

    # Validate direction:
    if len(direction) != 1:
        RaiseError('Too many arguments.')
    elif direction[0] not in ['dl', 'ul', 'd', 'u', 'download', 'upload']:
        RaiseError('Invalid argument <{}>'.format(direction[0]))

    # Confirm parameters:
    direction = 'download' if direction[0][0].lower() == 'd' else 'upload'
    remote_path = vars(args)['from']
    local_path = vars(args)['to']

    if direction == 'upload':
        remote_path, local_path = (local_path, remote_path)

    # Intiialize ServerLinker and run:
    linker = ServerLinker(direction=direction,
                          remote_path=remote_path,
                          local_path=local_path)
    linker.run()


if __name__ == "__main__":
    main()
