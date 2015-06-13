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
__author__ = 'kemiz'

from cloudify.decorators import workflow
from cloudify.workflows import ctx
from cloudify.workflows import parameters as p


@workflow
def execute_state(**kwargs):
    instance = None
    for node in ctx.nodes:
        if kwargs['node_id'] == node.id:
            for i in node.instances:
                instance = i
                break
            break

    ctx.logger.info("executing instance {}".format(instance))

    instance.execute_operation("salt.commands.execute_state",
                               kwargs={'node_id': p.node_id, 'salt_state': p.salt_state)

