import tweepy
import schedule
import time
from scripts.get_votes import get_votes

api = tweepy.Client(
    consumer_key='G8b1UAvQudHXsFVIxBPBbM3Uf',
    consumer_secret='qa4Jgeo5GEjh9CGwkFLGJEs4FLOqW0sJEX0tEdH7PtBu3ckS6L',
    access_token='1576660988392267776-bu9vbtiBpeFTHIh5t9KgtIjdVQfcdN',
    access_token_secret='KRjXrjHlJISWf82BlUu5GHQhLnA464Z6YMQQXGfyA4Pjw'
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
