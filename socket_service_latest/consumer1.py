# from os import wait
from kafka import KafkaConsumer
import json
# import asyncio

local_boostrap_server_address = 'localhost:9093'

a = 0
try:
    consumer = KafkaConsumer(
                    "topic0001",
                    bootstrap_servers=local_boostrap_server_address,
                    auto_offset_reset='latest',
                    enable_auto_commit = True,
                    request_timeout_ms = 10000,
                    consumer_timeout_ms=2000,
                    group_id="consumer-group-a")

    a=1

except:
    a = 0

class GetText():

    
    def get_text_corpus():
        global a, consumer
        if (a==1):
            print("starting the consumer1")
            for msg in consumer:
                print(msg)
                data_received = json.loads(msg.value)
                break
            consumer.commit()
            # consumer.stop()


        else:
            try:
                consumer = KafkaConsumer(
                                "topic0001",
                                bootstrap_servers=local_boostrap_server_address,
                                auto_offset_reset='latest',
                                enable_auto_commit = True,
                                request_timeout_ms = 11000,
                                consumer_timeout_ms=10000,
                                group_id="consumer-group-a")

                a=1

                print("starting the consumer2")
                for msg in consumer:
                    data_received = json.loads(msg.value)
                    break
                consumer.commit()
                # consumer.stop()

            except:
                data_received = "Refresh the page to get a Text"

        return data_received


    def get_data():
        data_received = "nothing here"
        consumer = KafkaConsumer(
                                "topic0001",
                                bootstrap_servers=local_boostrap_server_address,
                                auto_offset_reset='latest',
                                enable_auto_commit = True,
                                consumer_timeout_ms=2000,
                                group_id="consumer-group-a")

        print("starting the consumer")
        for msg in consumer:
            data_received = json.loads(msg.value)
            print('data_received')
            print(data_received)
            break

        return data_received


if __name__ == "__main__":
    # consumer = GetText.get_text_corpus()
    consumer = KafkaConsumer(
        "topic0001",
        bootstrap_servers=local_boostrap_server_address,
        auto_offset_reset='latest',
        enable_auto_commit = True,
        request_timeout_ms = 11000,
        consumer_timeout_ms=2000,
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        data_received = json.loads(msg.value)
        print('data_received')
        print(data_received)