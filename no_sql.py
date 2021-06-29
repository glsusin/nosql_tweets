import re
from pymongo import MongoClient

from tweets_txt_to_csv import cifras_transposicao

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

def busca_id_tweet(client):
    id_tweet = input('Digite o ID do Tweet que deseja buscar: ')
    # Criptografa ID do Tweet para buscar pelo id criptografado no banco
    id_criptografado = cifras_transposicao(str(id_tweet))
    ID_TWEET={'tweet_id': str(id_criptografado)}
    result = client['tweets']['tweets'].find(filter=ID_TWEET)
    for resultado in result:
        print('ID do Tweet ' + str(id_tweet))
        print('ID do Tweet criptografado ' + str(id_criptografado))
        print('Texto ' + resultado['text'])
        print('Usuário ' + resultado['user'])
        print('Data ' + resultado['date'])
        print('Localização ' + resultado['location'])
        print('Hashtags ' + resultado['hashtags'])

def busca_por_hashtag(client):
    hashtag = input('Digite a Hashtag do Tweet que deseja buscar: ')
    
    HASHTAG={'hashtags': {
                '$regex': re.compile(r'"'+hashtag+'(?i)"')
            }
    }
    result = client['tweets']['tweets'].find(filter=HASHTAG)
    for resultado in result:
        print('ID do Tweet ' + str(resultado['tweet_id']))
        print('Texto ' + resultado['text'])
        print('Usuário ' + resultado['user'])
        print('Data ' + resultado['date'])
        print('Localização ' + resultado['location'])
        print('Hashtags ' + resultado['hashtags'])

def busca_por_local_de_postagem(client):
    local = input('Digite o local de postagem do Tweet que deseja buscar: ')
    
    LOCAL={'location': {
                '$regex': re.compile(r'"'+local+'(?i)"')
            }
    }
    result = client['tweets']['tweets'].find(filter=LOCAL)
    for resultado in result:
        print('ID do Tweet ' + str(resultado['tweet_id']))
        print('Texto ' + resultado['text'])
        print('Usuário ' + resultado['user'])
        print('Data ' + resultado['date'])
        print('Localização ' + resultado['location'])
        print('Hashtags ' + resultado['hashtags'])

client = MongoClient('mongodb+srv://gustavo:FXIf72KKwponKglB@cluster0.2lhst.mongodb.net/admin?authSource=admin&replicaSet=atlas-4zc7o4-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')

# Busca quantas hashtags possuem a palavra PFIZER
PFIZER={'hashtags': {
            '$regex': re.compile(r"PFIZER(?i)")
        }
    }
result = client['tweets']['tweets'].find(filter=PFIZER).count()
print(result)

# Busca quantas hashtags possuem a palavra CORONAVAC
CORONAVAC={'hashtags': {
            '$regex': re.compile(r"CORONAVAC(?i)")
        }
    }
result = client['tweets']['tweets'].find(filter=CORONAVAC).count()
print(result)

# Busca quantas hashtags possuem a palavra ASTRAZENECA
ASTRAZENECA={'hashtags': {
            '$regex': re.compile(r"ASTRAZENECA(?i)")
        }
    }
result = client['tweets']['tweets'].find(filter=ASTRAZENECA).count()
print(result)

print("Digite o que você deseja fazer:")
print("0 - Sair")
print("1 - Pesquisar por id do tweet")
print("2 - Pesquisa por hashtag")
print("3 - Pesquisa por local de postagem")

opcao = input()

while opcao != '0':
    if opcao == '1':
        busca_id_tweet(client)
    elif opcao == '2':
        busca_por_hashtag(client)
    elif opcao == '3':
        busca_por_local_de_postagem(client)

    print("Digite o que você deseja fazer:")
    print("0 - Sair")
    print("1 - Pesquisar por id do tweet")
    print("2 - Pesquisa por hashtag")
    print("3 - Pesquisa por local de postagem")

    opcao = input()
