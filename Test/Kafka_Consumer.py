# -*- coding: utf-8 -*-
from confluent_kafka import Consumer, KafkaError
import sys
import json
from main import worker

settings = {
    'bootstrap.servers': '192.168.178.26:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}


def parser(msg):
    y = json.loads(msg)

    print (y['Version'])
    print (y['Eigentuemer'])
    print (y['AuftragsId'])
    print (y['Zeitstempel'])
    print (y['DokumentName'])
    print (y['DokumentId'])
    global DokumentId
    DokumentId = (y['DokumentId'])


    print (y)
    
c = Consumer(settings)

c.subscribe(['KeepInbound'])

try:
    while True:
        msg = c.poll(0.1)

        
        if msg is None:
            continue
        elif not msg.error():
            print('Received message: {0}'.format(msg.value()))
            print(format(msg.value()))
            parser(msg.value())
            worker('Testfiles/' + DokumentId)
            

        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {0}'.format(msg.error().str()))

except KeyboardInterrupt:
    pass

finally:
    c.close()
    
    