from cloudify.decorators import workflow
from cloudify.workflows import ctx

import logging

@workflow
def hello(**kwargs):
    log = logging.getLogger(__name__)
    log.warn('in hello')
       
    graph = ctx.graph_mode()

    for node in ctx.nodes:
        if 'cloudify.hello.instance' in node.type_hierarchy:
            for instance in node.instances:
                graph.add_task(instance.execute_operation('cloudify.interfaces.hello.hello'))

    return graph.execute()
