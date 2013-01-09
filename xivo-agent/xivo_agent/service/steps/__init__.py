# -*- coding: UTF-8 -*-

# Copyright (C) 2012-2013  Avencall
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

from .check_agent_membership import CheckAgentIsMemberOfQueueStep, CheckAgentIsNotMemberOfQueueStep
from .check_agent_status import CheckAgentIsLoggedStep, CheckAgentIsNotLoggedStep
from .check_extension import CheckExtensionIsNotInUseStep
from .get_agent import GetAgentStep
from .get_agent_status import GetAgentStatusStep
from .get_agent_statuses import GetAgentStatusesStep
from .get_interface import GetInterfaceStep, GetStateInterfaceForExtensionStep
from .get_queue import GetQueueStep
from .manage_events import SendAgentAddedToQueueEventStep, SendAgentRemovedFromQueueEventStep,\
    SendAgentLoginEventStep, SendAgentLogoffEventStep
from .manage_queue_member import InsertAgentIntoQueuememberStep, DeleteAgentFromQueuememberStep
from .manage_queues import AddAgentToQueueStep, AddAgentToQueuesStep,\
    RemoveAgentFromQueueStep, RemoveAgentFromQueuesStep
from .update_agent_status import UpdateAgentStatusStep
from .update_queue_log import UpdateQueueLogStep
from .get_logged_in_agents import GetLoggedInAgentsStep
from .logoff_all_agents import LogoffAllAgentsStep
