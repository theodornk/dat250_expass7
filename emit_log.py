import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

result = channel.queue_declare(queue='', exclusive=True)

print(" [x] Sent %r" % message)
connection.close()