class AbstractBroker(object):
    ''' Base broker definition for connecting to a message-broker '''

    def __init__(self, host, port, *args, **kwargs):
        self.host = host
        self.port = port

    def connect(self):
        pass

    def subscribe(self, *args, **kwargs):
        pass

    def cleanup(self, *args, **kwargs):
        pass


    def setup(self, cls, **kwargs):
        pass

