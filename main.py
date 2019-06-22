from server import ServerLinker
from argparse import ArgumentParser
from core import RaiseError
from core import DIRECTION_DL_OPTS, DIRECTION_DL_KEY
from core import DIRECTION_UL_OPTS, DIRECTION_UL_KEY


def main():
    parser = ArgumentParser(
        description="Simple Cloud-Storage File Transfer Program")
    parser.add_argument('--from', '-f', metavar='FROM')
    parser.add_argument('--to', '-t', metavar='TO')
    args, direction = parser.parse_known_args()

    remote_path = vars(args)['from']
    local_path = vars(args)['to']

    # Validate direction:
    if len(direction) == 0:
        RaiseError('Too few arguments.')
    elif len(direction) != 1:
        RaiseError('Too many arguments.')

    direction = direction[0]
    if direction not in DIRECTION_DL_OPTS + DIRECTION_UL_OPTS:
        RaiseError('Invalid argument <{}>'.format(direction))
    if direction in DIRECTION_DL_OPTS:
        direction = DIRECTION_DL_KEY
    else:
        direction = DIRECTION_UL_KEY
        remote_path, local_path = (local_path, remote_path)

    # Intiialize ServerLinker and run:
    linker = ServerLinker(direction=direction,
                          remote_path=remote_path,
                          local_path=local_path)
    linker.run()


if __name__ == "__main__":
    main()
