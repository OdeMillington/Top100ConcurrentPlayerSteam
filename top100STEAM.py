import requests
import json

gameList = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v0002/')
concurrentPlayers = requests.get('https://api.steampowered.com/ISteamChartsService/GetGamesByConcurrentPlayers/v1/')

topGamesList = []

for game in gameList.json()['applist']['apps']:
    for topGame in concurrentPlayers.json()['response']['ranks']:
        if game['appid'] == topGame['appid']:
            topGamesList.append((topGame['rank'],game['name'], topGame['concurrent_in_game']))



for i in range(len(topGamesList)):
    topGamesList = sorted(topGamesList)

for index in range(len(topGamesList)):
    print(f"#{topGamesList[index][0]}: {topGamesList[index][1]} \nCurrent Players: {topGamesList[index][2]} \n\n")