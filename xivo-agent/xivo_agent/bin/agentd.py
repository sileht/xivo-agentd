# -*- coding: UTF-8 -*-

# Copyright (C) 2012  Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import argparse
import logging
import signal
from contextlib import contextmanager
from xivo_agent import ami
from xivo_agent import dao
from xivo_agent.ctl.server import AgentServer
from xivo_agent.queuelog import QueueLogManager
from xivo_agent.service import AgentService
from xivo_dao import queue_log_dao
from xivo_dao.alchemy import dbconnection

_DB_URI = 'postgresql://asterisk:proformatique@localhost/asterisk'


def main():
    _init_logging()

    parsed_args = _parse_args()

    if parsed_args.verbose:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

    _init_signal()
    _init_dao()
    with _new_ami_client() as ami_client:
        with _new_agent_server() as agent_server:
            queue_log_manager = QueueLogManager(queue_log_dao)

            agent_service = AgentService(ami_client, agent_server, queue_log_manager)
            agent_service.init()
            agent_service.run()


def _init_logging():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s (%(levelname)s): %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase verbosity')
    return parser.parse_args()


def _init_signal():
    signal.signal(signal.SIGTERM, _handle_sigterm)


def _init_dao():
    dao.init(_DB_URI)

    db_connection_pool = dbconnection.DBConnectionPool(dbconnection.DBConnection)
    dbconnection.register_db_connection_pool(db_connection_pool)
    dbconnection.add_connection_as(_DB_URI, 'asterisk')


def _handle_sigterm(signum, frame):
    raise SystemExit(0)


@contextmanager
def _new_ami_client():
    ami_client = ami.new_client('localhost', 'xivo_agent', 'die0Ahn8tae')
    try:
        yield ami_client
    finally:
        ami_client.close()


@contextmanager
def _new_agent_server():
    agent_server = AgentServer()
    try:
        agent_server.bind('localhost')
        yield agent_server
    finally:
        agent_server.close()


if __name__ == '__main__':
    main()
