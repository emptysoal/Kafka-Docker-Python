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
