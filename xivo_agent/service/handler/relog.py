# -*- coding: utf-8 -*-

# Copyright (C) 2013-2014 Avencall
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

import logging
from xivo import debug
from xivo_bus.resources.agent import command as commands

logger = logging.getLogger(__name__)


class RelogHandler(object):

    def __init__(self, relog_manager):
        self._relog_manager = relog_manager

    def register_commands(self, agent_server):
        agent_server.add_command(commands.RelogAllCommand, self.handle_relog_all)

    @debug.trace_duration
    def handle_relog_all(self, command):
        logger.info('Executing relog all command')
        self._relog_manager.relog_all_agents()