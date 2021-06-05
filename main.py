import requests

title = []

if __name__ == '__main__':
    url = 'https://api.jikan.moe/v3/anime/1'
    #url = 'https://api.jikan.moe/v3/top/anime'
    
    response = requests.get(url)
    if response.status_code == 200:
        anime = response.json()
        print(anime)
        #print('Titulo del anime: ', anime['title'])
        #print('Numero total de episodios: ', anime['episodes'])
        #print('Sinopsis: ',anime['synopsis'])
#segunda prueba
        #for i in anime['top']:
        #    title.append(i['title'])
#
        #for e in title:
        #    print(e)
