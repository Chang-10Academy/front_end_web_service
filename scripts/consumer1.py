from kafka import KafkaConsumer
import json

local_boostrap_server_address = 'localhost:9092'

a = 0
try:
    consumer = KafkaConsumer(
                    "topic0001",
                    bootstrap_servers=local_boostrap_server_address,
                    auto_offset_reset='latest',
                    group_id="consumer-group-a")

    a=1

except:
    a = 0

class GetText():

    
    def get_text_corpus():
        global a, consumer
        if (a==1):
            print("starting the consumer")
            for msg in consumer:
                data_received = json.loads(msg.value)
                break


        else:
            try:
                consumer = KafkaConsumer(
                                "topic0001",
                                bootstrap_servers=local_boostrap_server_address,
                                auto_offset_reset='latest',
                                group_id="consumer-group-a")

                a=1

                print("starting the consumer")
                for msg in consumer:
                    data_received = json.loads(msg.value)
                    break

            except:
                data_received = "Refresh the page to get a Text"

        return data_received


if __name__ == "__main__":
    consumer = GetText.get_text_corpus()
    print(consumer)