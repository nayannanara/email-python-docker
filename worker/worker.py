import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    r = redis.Redis(host='queue', port=6379, db=0)
    print('Aguardando mensagens ...')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        print('Mandadno a mensagem')
        sleep(randint(15,45))
        print('mensagem enviada')
