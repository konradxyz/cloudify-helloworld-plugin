from cloudify import ctx
from cloudify.decorators import operation

import logging
import uuid

@operation
def operation_log(**kwargs):
  msg = ctx.instance.runtime_properties.get('msg', 'no msg')
  new_msg = uuid.uuid4()
  ctx.instance.runtime_properties['msg'] = new_msg
  logger = logging.getLogger(__name__)
  logger.warn('old msg: {}'.format(msg))
  logger.warn('new msg: {}'.format(new_msg))
  logger.warn(str(kwargs))
