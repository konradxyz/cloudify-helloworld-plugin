from cloudify import ctx
from cloudify.decorators import operation

import logging
import uuid

def log_more(logger):
  i = 0
  while i < 1000:
    logger.warn("hello_log " * 1000)
    i = i + 1

@operation
def operation_log(**kwargs):
  msg = ctx.instance.runtime_properties.get('msg', 'no msg')
  new_msg = str(uuid.uuid4())
  ctx.instance.runtime_properties['msg'] = new_msg
  logger = logging.getLogger(__name__)
  logger.warn('old msg: {}'.format(msg))
  logger.warn('new msg: {}'.format(new_msg))
  log_more(logger)
  logger.warn(str(kwargs))
