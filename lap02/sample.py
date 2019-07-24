from youtube_dl import YoutubeDL
# # Sample 1: Download a single youtube video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE')
# # Sample 2: Download multiple youtube videos
# dl = YoutubeDL()
# # Put list of song urls in download function to download them, one by one
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])


# Sample 3: Download audio
# options = {'format': 'bestaudio/audio'}
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])
# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])