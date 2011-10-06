from tg2.signals.configuration import load_package_config
import webob
from uuid import uuid4

class SignalsMiddleware(object):
    """ WSGI Middleware that provides a way to consume messages from messaging 
        queue protocols like STOMP or AMQP (qpid, RabbitMQ) with ease.
    """ 
    def __init__(self, app, **kwargs):
        '''
            Sets up the middleware.
        '''
        self.app = app
        self.config = load_package_config()
        self.registry = Registry()

        # Setup and connect to broker here
        self.brokerage = None
        _protocol = self.config.broker.protocol

        _brokerage_package = None
        try:
            _brokerage_package = __import__(
                "tg2.signals.brokers."+_protocol, {}, {}, 'broker')
        except:
            try:
                _brokerage_package = __import__(_protocol, {}, {}, 'broker')
            except:
                pass
        
        if _brokerage_package is not None and hasattr(_brokerage_package, 'broker'):
            self.brokerage = _brokerage_package.broker(self.config)

    def __call__(self, environ, start_response):
        """
            Process a request
        """
        """ Does nothing right now. """
        app = self.app
        req = webob.Request(environ)
        req.signals = dict(active = True)

        return app(environ, start_response)


class Registry(object):
    """
        Provides a mechanism for decorated controller actions to describe 
        what queues, topics, etc need to be available on the broker.

        Provides latest messages via request.signals['messages'] to properly
        subscribed remote-clients.
    """
    def __init__(self):
        self.registered_urls = {}

    def register(self, url, **kwargs):
        if url not in self.registered_urls:
            pass
