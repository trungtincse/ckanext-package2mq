import pika
#contain some config variables
RABBITMQ_ACCOUNT_NAME="rabbitmq"
RABBITMQ_ACCOUNT_PASSWORD="rabbitmq"
RABBITMQ_HOST="172.20.0.4"
RABBITMQ_PORT=5672
RABBITMQ_QUEUE="message_BC"
credentials=pika.PlainCredentials(RABBITMQ_ACCOUNT_NAME,RABBITMQ_ACCOUNT_PASSWORD)