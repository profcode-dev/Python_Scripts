import pytube
import pyfiglet 
import time 
from termcolor import colored, cprint

class Main:
    def __init__(self):
        art = pyfiglet.figlet_format("Python Tube", font='slant')
        cprint(art, 'magenta')
        
        print("welcome to my 'python tube': ")
        print("Enter number from my choices to Enter Script..")
        print("Press [1] for Video_information")
        print("Press [2] for Playlist_information")
        print("Press [3] for Vidoe_download")   
        print("Press [4] for Playlist_download") 
        print("write 'exit' to close the script ")
        print("write 'back' to go startmenu")  

        self.choices()
    
    def choices(self):
        while True: 
            try: 
                choice = int(input("Enter your choice : "))
                
                
                if choice == 1 :
                    self.video_info()
                elif choice == 2:
                    self.playlist_info()
                elif choice == 3: 
                    print('I am working on it')
                elif choice == 4:
                    print('I am working on it')
                else:
                    print('you are wrong')
            
            except ValueError :
                print("Please, Enter A valid number.")
            except KeyboardInterrupt:
                break 
            
            
    def playlist_info(self):
        try:    
            def convert_time(time):
                seconds = time
                seconds = seconds % (24 * 3600)
                hour = seconds // 3600
                seconds %= 3600
                minutes = seconds // 60
                seconds %= 60

                print("Playlist_time:","%d:%02d:%02d" % (hour, minutes, seconds))
                
            def playlist_time():
                lst  = []
                print(colored("Account time for playlist..", 'blue'))
                time.sleep(0.5)
                print(colored("Be patient script is loading....", 'blue'))
                for i in playli.video_urls:
                    time_playlist = pytube.YouTube(i)
                    url_time = time_playlist.length
                    lst.append(url_time)
                    
                result = sum(lst) 
                convert_time(result)
                
            print("welcome to playlist_information")
            Entry = input(colored("Enter playlist_url: ", 'red'))

            playli = pytube.Playlist(Entry)
            
            
            print("------------ Playlist_Information -------------")
            # playlist title 
            print(f"title: {playli.title}")

            # return playlist video count 
            print(f"Video_counts: {playli.length} videos")
            print(f"Views: {playli.views:,} ")
            print(f"Last_updated: {playli.last_updated}")
            playlist_time()

            print(f"Playlist_url: {playli.playlist_url}")
            print(f"Playlist_id: {playli.playlist_id}")

            # the owner of the playlist 
            print(f"channel_name: {playli.owner}")
            print(f"channel_id: {playli.owner_id}")
            print(f"channel_url: {playli.owner_url}")


            print("--------------------Playlist_vidoes-----------------------------")
            # for n in range(1,playli.length):
            #     N = print(n)
            
            n = 1
            while n < playli.length:
                
                for i in playli.video_urls:
                    youT = pytube.YouTube(i)
                    print(f"{n}-{colored(youT.title, 'yellow')}")
                    # print(f"{youT.title}")
                    print(f"  video_url: {i} ")
                    n +=1
                
        except KeyboardInterrupt:
            exit

    def video_info(self):
        def convert_time(time):
            seconds = time
            
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60

            print("video_time:","%d:%02d:%02d" % (hour, minutes, seconds))

        # welcome message 
        print("welcome to get video_info")
        Entry = input('Enter url: ')

        # get info about videos 
        youT = pytube.YouTube(Entry)

        print("--------------- Video Information ------------")
        print(f"title: {youT.title}")
        print(f"channel_name: {youT.author}"),
        print(f"video_ID: {youT.channel_id}")# Get the video poster's channel id.
        # print(f"Description: {youT.description}")# Get the video description 
        # print(f"{youT.keywords}")
        print(f"Channel_URL: {youT.channel_url}")
        convert_time(youT.length)
        print(f"Publish_date: {youT.publish_date}")
        print(f"Thumbnail_url: {youT.thumbnail_url}")
        print(f"Views: {youT.views:,} ")

    def playlist_downlaod(self):
        pass
    
    def video_download(self):
        pass
    

tk = Main()
# tk.playlist_info()
# # tk.video_info()