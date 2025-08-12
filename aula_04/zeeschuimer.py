import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_json('../bases/israel.ndjson', lines=True)
print(dados.head())

dados2 = pd.json_normalize(dados['data'])
print(dados2.head())

for posicao, item in enumerate(dados2.columns):
    print(posicao, item)

colunas_desejadas = ['id', 'desc', 'challenges', 'createTime', 'video.duration', 'video.cover', 'author.id',
                    'author.nickname', 'author.uniqueId','author.verified', 'music.title', 'authorStats.followingCount',
                    'authorStats.followerCount', 'authorStats.heartCount', 'authorStats.videoCount',
                    'authorStats.diggCount', 'authorStats.heart', 'statsV2.collectCount', 'statsV2.commentCount',
                    'statsV2.diggCount', 'statsV2.playCount', 'statsV2.shareCount']

dados3 = dados2[colunas_desejadas]
print(dados3)

print(dados3.info())

for coluna in colunas_desejadas:
    print(f'{coluna}: {dados3[coluna][30]}')

dados3['createdAt'] = dados3['createTime'].apply(lambda x: pd.Timestamp(x, unit='s'))

def preenche_url(item):
    return f"https://www.tiktok.com/@{item['author.uniqueId']}/video/{item['id']}"

dados3['url'] = dados3.apply(preenche_url, axis=1)

dados3['statsV2.diggCount'] = dados3['statsV2.diggCount'].astype(float)
dados3['statsV2.playCount'] = dados3['statsV2.playCount'].astype(float)
dados3['statsV2.shareCount'] = dados3['statsV2.shareCount'].astype(float)
dados3['statsV2.commentCount'] = dados3['statsV2.commentCount'].astype(float)
dados3['statsV2.collectCount'] = dados3['statsV2.collectCount'].astype(float)

indice_mais_like = dados3['statsV2.diggCount'].idxmax()

print(f"O vídeo com mais likes é: {dados3['url'][indice_mais_like]}, com {dados3['statsV2.diggCount'][indice_mais_like]} likes")

print(f'A média de comentários é {dados3["statsV2.commentCount"].mean()}')

print(f'A mediana de compartilhamentos (shares) é {dados3["statsV2.shareCount"].median()}')

print(f'O total de posts é {dados3.shape[0]}')