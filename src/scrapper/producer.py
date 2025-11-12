import os
import logging
from confluent_kafka import Producer

logger = logging.getLogger(__name__)

CONFIG = {
    # === Mandatory parameters ===
    "bootstrap.servers": os.environ.get("BOOTSTRAP_SERVERS"),
    # === Identification ===
    "client.id": "scrapper-raw-trades-btc-usdt",
    # === Security (SCRAM-SHA-512 with TLS) ===
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "SCRAM-SHA-512",
    "sasl.username": os.environ.get("KAFKA_USERNAME"),
    "sasl.password": os.environ.get("KAFKA_PASSWORD"),
    # === TLS Configuration ===
    "ssl.ca.location": os.environ.get(
        "KAFKA_CA_CERT", "/etc/ssl/certs/ca-certificates.crt"
    ),
    "ssl.endpoint.identification.algorithm": "none",  # Set to 'none' for self-signed certs, use 'https' for production
    # === Performance ===
    # 'batch.size': 16384,              # Taille du batch en bytes
    # 'linger.ms': 10,                   # Temps d'attente pour remplir un batch
    # 'compression.type': 'snappy',      # Type de compression (none, gzip, snappy, lz4, zstd)
    # 'buffer.memory': 33554432,         # Mémoire totale disponible pour le buffering
    # === Reliability ===
    # 'acks': 'all',                     # 0, 1, ou 'all' pour la garantie de livraison
    # 'retries': 3,                      # Nombre de tentatives en cas d'erreur
    # 'max.in.flight.requests.per.connection': 5,
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
