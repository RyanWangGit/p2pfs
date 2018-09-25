from p2pfs.core.peer import PeerServer
from p2pfs.core.server import CentralServer
import argparse
import logging
import coloredlogs

coloredlogs.install(level='INFO', fmt='%(levelname)s:%(module)s[0x%(thread)x]: %(message)s')


def main():
    arg_parser = argparse.ArgumentParser(description=__doc__)
    arg_parser.add_argument('option', metavar='OPTION', type=str, nargs=1)
    arg_parser.add_argument('host', metavar='HOST', type=str, nargs='?', default='127.0.0.1')
    arg_parser.add_argument('host_port', metavar='HOST_PORT', type=int, nargs='?', default=8888)
    arg_parser.add_argument('server', metavar='SERVER', type=str, nargs='?', default='127.0.0.1')
    arg_parser.add_argument('server_port', metavar='SERVER_PORT', type=int, nargs='?', default=8888)
    results = arg_parser.parse_args()

    if results.option[0] == 'server':
        server = CentralServer(results.host, results.host_port)
        server.listen()
    elif results.option[0] == 'peer':
        peer = PeerServer(results.host, results.host_port, results.server, results.server_port)
        peer.listen()
    else:
        logging.error('Option must either be \'server\' or \'peer\'')


if __name__ == '__main__':
    main()
