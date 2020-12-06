# -*- coding:utf-8 -*-

"""
    Kafka 生产者
"""

import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='169.254.207.36:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

msg = {'key1': 'value1'}
producer.send('test', msg)
print("Send %s" % msg)

producer.close()
