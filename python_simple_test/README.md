# 简单测试 - Python调用Kafka

## 环境

```bash
$ pip3 install kafka-python
```

## 代码

- 生产者 producer.py

```python
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

```

- 消费者 consumer.py

```python
# -*- coding:utf-8 -*-

"""
    Kafka 消费者
"""

from kafka import KafkaConsumer

consumer = KafkaConsumer("test", bootstrap_servers=["169.254.207.36:9092"])
print("Waiting for message. To exit press CTRL+C")

for msg in consumer:
    print("Received, msg info is:")
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)

```

