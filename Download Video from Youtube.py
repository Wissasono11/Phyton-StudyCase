from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occured")
    print("Download is complete successfully") 

link = input("Enter the Youtube video URL: ")
Download(link)return go(f, seed, [])
