import abc

import six


@six.add_metaclass(abc.ABCMeta)
class PluginBase(object):
    """Base class for plugin used in fellow.
    """

    def __init__(self, max_width=60):
        self.max_width = max_width

    @abc.abstractmethod
    def run(self):
        """Run the plugin
        """
