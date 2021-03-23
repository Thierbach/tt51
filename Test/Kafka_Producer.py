# -*- coding: utf-8 -*-
from confluent_kafka import Producer
import uuid
 
json = open('JSON-Object','r') 
msgkey = uuid.uuid4().hex

p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce('KeepInbound', key=msgkey, value=json.read())
p.flush(30)

json.close()