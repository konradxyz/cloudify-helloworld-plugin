from cloudify.decorators import workflow
from cloudify.workflows import ctx

import logging

@workflow
def hello(**kwargs):
    log = logging.getLogger(__name__)
    log.warn('in hello')
       
    graph = ctx.graph_mode()

    for node in ctx.nodes:
        for instance in node.instances:
            graph.add_task(instance.execute_operation('helloworld_plugin.tasks.operation_log'))

    return graph.execute()
