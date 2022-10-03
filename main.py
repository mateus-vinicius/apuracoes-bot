import tweepy
import schedule
import time
from scripts.get_votes import get_votes

api = tweepy.Client(
    consumer_key='',
    consumer_secret='',
    access_token='',
    access_token_secret=''
)



def func():
    try:
        resultado = get_votes()
        apuracoes = []
        for n in range(4):
            apuracoes.append('{nome}: {votos}%'.format(nome=resultado['cand'][n]['nm'],votos=resultado['cand'][n]['pvap']))
        try:
            tweet = api.create_tweet(text='{pst}%\n\n{text}\n #eleicoes2022 #eleicoes'.format(pst=resultado['pst'],text='\n'.join(apuracoes)))
            print(tweet)
        except:
            print('Erro ao postar tweet')
    except:
        print('Slow down')

schedule.every(5).minutes.do(func)

while True:
	schedule.run_pending()
	time.sleep(1)
