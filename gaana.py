# # webscraping for gaana.com

# import requests
# import webbrowser
# from bs4 import BeautifulSoup
# response = requests.get("https://gaana.com/playlist/gaana-dj-telugu-top-50-1").text
# soup = BeautifulSoup(response,"html.parser")
# main_div = soup.find("div",class_="s_c")
# ul_div = main_div.find_all("div",class_="playlist_thumb_det")
# numbering_count = 0
# list_of_links = []
# for i in ul_div:
# 	numbering_count+=1
# 	song_link = i.find("a")["href"]
# 	song_name = i.find("a").text
# 	print(str(numbering_count)+"."+song_name)
# 	list_of_links.append(song_link)

# song =int(input("which song do you wnat to listen:-"))
# url = list_of_links[song-1]
# webbrowser.open_new(url)



