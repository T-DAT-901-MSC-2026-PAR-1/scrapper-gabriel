import os
import logging
from confluent_kafka import Producer

logger = logging.getLogger(__name__)

base = os.environ.get("BASE")
quote = os.environ.get("QUOTE")
client_id = f"scrapper-raw-trades-{base}-{quote}".lower()

CONFIG = {
    "bootstrap.servers": os.environ.get("BOOTSTRAP_SERVERS"),
    "client.id": client_id,
    "security.protocol": "PLAINTEXT",
}


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class RawTradesProducer(Producer, metaclass=SingletonMeta):
    def __init__(self, config: dict):
        # Avoid instanciation if the instance already exists
        if not hasattr(self, "_initialized"):
            super().__init__(config)
            self._initialized = True
            logger.debug(f"RawTradesProducer created with config: {config}")


producer = RawTradesProducer(CONFIG)
