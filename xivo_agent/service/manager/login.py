# -*- coding: utf-8 -*-

# Copyright (C) 2013-2015 Avencall
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

from xivo_agent.exception import AgentAlreadyLoggedError, ExtensionAlreadyInUseError
from xivo_dao.helpers import db_utils

logger = logging.getLogger(__name__)


class LoginManager(object):

    def __init__(self, login_action, agent_status_dao):
        self._login_action = login_action
        self._agent_status_dao = agent_status_dao

    def login_agent(self, agent, extension, context, state_interface):
        self._check_agent_is_not_logged(agent)
        self._check_extension_is_not_in_use(extension, context)
        self._login_action.login_agent(agent, extension, context, state_interface)

    def _check_agent_is_not_logged(self, agent):
        with db_utils.session_scope():
            agent_status = self._agent_status_dao.get_status(agent.id)
        if agent_status is not None:
            raise AgentAlreadyLoggedError()

    def _check_extension_is_not_in_use(self, extension, context):
        with db_utils.session_scope():
            if self._agent_status_dao.is_extension_in_use(extension, context):
                raise ExtensionAlreadyInUseError()
