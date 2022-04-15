#!/usr/bin/bash

#Download and unzip Kafka to one of the nodes
echo "Download and unzip Kafka to one of the nodes"
wget https://downloads.apache.org/kafka/2.8.1/kafka_2.13-2.8.1.tgz
tar -xzf kafka_2.13-2.8.1.tgz
cd kafka_2.13-2.8.1
#Start zookeeper
echo "Starting Zookeeper"
bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
#Start Kafka
echo "Starting Kafka"
bin/kafka-server-start.sh -daemon config/server.properties
#Create a Kafka topic named "test"
echo "Creating a Kafka topic named test"
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
echo "Now you are set to go!"
