#!/usr/bin/bash

#Download and unzip Kafka to one of the nodes
echo "Downloading Kafka..."
wget https://downloads.apache.org/kafka/2.8.1/kafka_2.13-2.8.1.tgz
tar -xzf ./kafka_2.13-2.8.1.tgz
#Start zookeeper
echo "Starting Zookeeper..."
./kafka_2.13-2.8.1/bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
#Starting Kafka
echo "Starting Kafka..."
./kafka_2.13-2.8.1/bin/kafka-server-start.sh -daemon config/server.properties
#Create a Kafka topic named "test"
echo "Creating a Kafka topic named test"
./kafka_2.13-2.8.1/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic project
echo "Now you are set to go! The Topic project has been created"
./kafka_2.13-2.8.1/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
