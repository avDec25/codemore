from datetime import datetime
from kafka import KafkaConsumer, TopicPartition

topic  = "dc1.Pretr-PUSH_UPDATE_EVENT_TO_SELLER" 
broker = "pac-azairbuskafka21:9092,pac-azairbuskafka22:9092,pac-azairbuskafka23:9092,pac-azairbuskafka24:9092,pac-azairbuskafka25:9092"

# lets check messages of the first day in New Year
date_in  = datetime(2022,8,21)
date_out = datetime(2022,8,30)

consumer = KafkaConsumer(topic, bootstrap_servers=broker, enable_auto_commit=True)
consumer.poll()  # we need to read message or call dumb poll before seeking the right position

tp      = TopicPartition(topic, 0) # partition n. 0
# in simple case without any special kafka configuration there is only one partition for each topic channel
# and it's number is 0

# in fact you asked about how to use 2 methods: offsets_for_times() and seek()
rec_in  = consumer.offsets_for_times({tp:date_in.timestamp() * 1000})
rec_out = consumer.offsets_for_times({tp:date_out.timestamp() * 1000})

consumer.seek(tp, rec_in[tp].offset) # lets go to the first message in New Year!

c = 0
for msg in consumer:
  if msg.offset >= rec_out[tp].offset:
    break

  c += 1
  # message also has .timestamp field

print("{c} messages between {_in} and {_out}".format(c=c, _in=str(date_in), _out=str(date_out)))