# Docker 环境下的 Kafka 使用

## 环境构建

- 下载zookeeper

```bash
$ docker pull wurstmeister/zookeeper
```

- 下载kafka

```bash
$ docker pull wurstmeister/kafka:2.11-0.11.0.3
```

## 启动

- 启动zookeeper

```bash
$ docker run -d --name zookeeper -p 2181:2181 -v /etc/localtime:/etc/localtime wurstmeister/zookeeper
```

- 启动kafka

```bash
$ docker run  -dit --name kafka -p 9092:9092 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=169.254.207.36:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://169.254.207.36:9092 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 wurstmeister/kafka:2.11-0.11.0.3
```

## 测试

- 创建topic

```bash
$ docker exec -it kafka /bin/sh
# cd /opt/kafka/
# bin/kafka-topics.sh --zookeeper 169.254.207.36:2181 --create --topic test --partitions 2 --replication-factor 1
```

- 查看全部topic

接着上面的步骤

```bash
# bin/kafka-topics.sh --zookeeper 169.254.207.36:2181 --list
```

- 查看刚刚创建的topic

```bash
# bin/kafka-topics.sh --zookeeper 169.254.207.36:2181 --describe --topic test
```

- 发布消息

继续接着上面的步骤，把当前所在的容器当作生产者

```bash
# bin/kafka-console-producer.sh --topic=test --broker-list 169.254.207.36:9092
>hello
>world
>成功
>
```

- 接收消息

另外启动一个容器，作为消费者

```bash
$ docker exec -it kafka /bin/sh
# cd /opt/kafka/
# bin/kafka-console-consumer.sh --bootstrap-server 169.254.207.36:9092 --from-beginning --topic test
hello
world
成功

```

如果消费者接收成功，则 Kafka 环境搭建完成。

## Kafka界面管理

- 相关镜像下载

```bash
$ docker pull sheepkiller/kafka-manager
```

- 相关镜像启动

```bash
$ docker run -itd --name=kafka-manager -p 9000:9000 -e ZK_HOSTS="169.254.207.36:2181" sheepkiller/kafka-manager
```

- 访问

浏览器中输入 `<IP>:9000`

