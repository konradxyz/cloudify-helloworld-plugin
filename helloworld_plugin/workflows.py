from cloudify.decorators import workflow
from cloudify.workflows import ctx

@workflow
def hello(**kwargs):
    graph = ctx.graph_mode()

    for node in ctx.nodes:
        for instance in node.instances:
            graph.add_task(instance.execute_operation('cloudify.interfaces.lifecycle.configure'))

    return graph.execute()
