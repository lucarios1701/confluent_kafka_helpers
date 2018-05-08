from setuptools import find_packages, setup

setup(name="confluent_kafka_helpers",
      version="0.6.1",
      description="Helpers for Confluent's Kafka Python client",
      url="https://github.com/fyndiq/confluent_kafka_helpers",
      author="Fyndiq AB",
      author_email="support@fyndiq.com",
      license="MIT",
      packages=find_packages(),
      install_requires=[
          'structlog>=17.2.0',
          'confluent-kafka==0.11.4',
          'fastavro==0.18.0'
      ],
      zip_safe=False)
