from tg.util import Bunch
import os

class SignalsConfig(Bunch):
    """
        Configuration dictionary that uses the familiar TG 
        app_cfg.py/base_config style configuration
    """
    def __init__(self):
        self.broker = Bunch()
        self.authentication = Bunch()

        # Set some defaults
        self.broker.protocol = None
        self.broker.host = "localhost"
        self.broker.port = None

        self.authentication.username = ""
        self.authentication.password = ""


def load_package_config():
    """
        Figures out what the current package is (the active WSGI app usually)
        and loads the config in from appname/config/app_cfg.py
    """
    from tg.util import get_package_name
    package_name = get_package_name()

    if not package_name:
        return None

    package = __import__(package_name+".config.app_cfg", {}, {}, ['signals_config'])

    if hasattr(package, 'signals_config'):
        return package.signals_config
