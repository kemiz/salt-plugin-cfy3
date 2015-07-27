########
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and

# * limitations under the License.
import commands
from cloudify.decorators import operation
import subprocess
import urllib
import os


def get_ip_from_interface_name(interface_name):
    intf_ip = commands.getoutput("ip address show dev " + interface_name).split()
    intf_ip = intf_ip[intf_ip.index('inet') + 1].split('/')[0]
    return intf_ip

@operation
def execute_state(ctx, **kwargs):
    state_name = kwargs["node_id"]["state_name"]
    ctx.logger.info("executing state " + state_name + " on node " + kwargs["node_id"])
    command = "salt-call"
    exitcode = subprocess.call([command, state_name])
