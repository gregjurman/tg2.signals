from base import AbstractBroker
from pylons import request, response
from tg.decorators import Decoration
from pylons.controllers.util import abort
from tg.flash import flash


class signals(object):
    def __init__(self, **kwargs):
        pass
    
    def __call__(self, func):
        decoration = Decoration.get_decoration(func)
        decoration.register_hook('before_validate', self.before_validate)
        decoration.register_hook('before_call', self.before_call)
        return func
    
    def before_validate(self, remainder, params):
        if '_signals_subkey' not in params:
            flash('Not subscribed', status='warning')
            abort(401, 'Not subscribed')


    def before_call(self, remainder, params):
        raise Exception, params
