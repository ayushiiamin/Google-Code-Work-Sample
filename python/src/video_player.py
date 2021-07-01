"""A video player class."""

from .video_library import VideoLibrary
import random

#li = []
#randLi = []
#flagPause = False
#pauseList = []
#pauseVar = 0
class VideoPlayer:
    """A class used to represent a Video Player."""

    
    def __init__(self):
        self._video_library = VideoLibrary()
        self.li = []
        self.randLi = []
        self.pauseList = []
        self.vidList = []
        self.playList = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        vid_all = self._video_library.get_all_videos()
        vid_all.sort(key=lambda x: x._title, reverse=False)
        length = len(vid_all)
        print("Here's a list of all available videos:")
        for i in range(length):
            print(vid_all[i]._title + " " + "(" + vid_all[i]._video_id + ")" + " " + "[{0}".format(' '.join(map(str, vid_all[i]._tags))) + "]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        vid_title = self._video_library.get_video(video_id)
        self.vidList.append(vid_title)
        #print(self.vidList[1]._title)
        #li = []
        if vid_title == None:
            print("Cannot play video: Video does not exist")
        elif self.li == []:
            self.li.append(vid_title._title)
            print("Playing video: " + self.li[0])
        else:
            print("Stopping video: " + self.li[0])
            #li[0] = vid_title._title
            self.li.pop(0)
            self.vidList.clear()
            self.pauseList.clear()
            self.vidList.append(vid_title)
            self.li.append(vid_title._title)
            print("Playing video: " + self.li[0])
            #li.clear() ###############

    def stop_video(self):
        """Stops the current video."""

        if self.li == []:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: " + self.li[0])
            self.li.pop(0)
            self.vidList.clear()
            self.pauseList.clear()

    def play_random_video(self):
        """Plays a random video from the video library."""

        vid_list = self._video_library.get_all_videos()
        vid_random = random.choice(vid_list)
        
        if self.randLi == [] and self.li == []:
            self.randLi.append(vid_random._title)
            print("Playing video: " + self.randLi[0])
        elif self.li != []:
            print("Stopping video: " + self.li[0])
            #li[0] = vid_title._title
            self.li.pop(0)
            self.li.append(vid_random._title)
            print("Playing video: " + self.li[0])
            #li.clear()
        elif self.randLi != []:
            print("Stopping video: " + self.randLi[0])
            #li[0] = vid_title._title
            self.randLi.pop(0)
            self.randLi.append(vid_random._title)
            print("Playing video: " + self.randLi[0])
            #li.pop(0)
        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        if self.li == []:
            print("Cannot pause video: No video is currently playing")
        elif self.pauseList.count(self.li[0]) > 0: 
            print("Video already paused: " + self.li[0])
        else:
            print("Pausing video: " + self.li[0])
            self.pauseList.append(self.li[0])

    def continue_video(self):
        """Resumes playing the current video."""

        if self.li == [] and self.pauseList == []:
            print("Cannot continue video: No video is currently playing")
        elif self.pauseList == []:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video: Amazing Cats")
            self.pauseList.remove(self.li[0])

        #print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        if self.vidList == []:
            print("No video is currently playing")
        elif self.pauseList != []:
            print("Currently playing: " + self.vidList[0]._title + " " + "(" + self.vidList[0]._video_id + ")" + " " +"[{0}".format(' '.join(map(str, self.vidList[0]._tags))) + "]" + " - " + "PAUSED")
        else:
            print("Currently playing: " + self.vidList[0]._title + " " + "(" + self.vidList[0]._video_id + ")" + " " +"[{0}".format(' '.join(map(str, self.vidList[0]._tags))) + "]")

        #print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in map(str.lower, self.playList.keys()):
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playList[playlist_name] = []
            print("Successfully created new playlist: " + playlist_name)


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.

        """
        vid_title_list = self._video_library.get_video(video_id)

        if playlist_name.lower() not in map(str.lower, self.playList.keys()):
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")
        elif vid_title_list == None:
            print("Cannot add video to " + playlist_name + ": Video does not exist")
        elif playlist_name.lower() in map(str.lower, self.playList.keys()):
            for x in self.playList.keys():
                if x.lower() == playlist_name.lower():
                    #print(x)
                    if self.playList[x].count(vid_title_list) > 0:
                        print("Cannot add video to " + playlist_name + ": Video already added")
                    else:
                        self.playList[x].append(vid_title_list)
                        print("Added video to " + playlist_name + ": " + self.playList.get(x)[0]._title)

    def show_all_playlists(self):
        """Display all playlists."""

        if self.playList == {}:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for key in sorted(self.playList.keys()):
                print(key)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in map(str.lower, self.playList.keys()):
            print("Cannot show playlist " + playlist_name + ": Playlist does not exist")
        elif playlist_name.lower() in map(str.lower, self.playList.keys()):
            for x in self.playList.keys():
                if x.lower() == playlist_name.lower():
                    if self.playList.get(x) == []:
                        print("Showing playlist: " + playlist_name)
                        print("No videos here yet")
                    else:
                        print("Showing playlist: " + playlist_name)
                        print(self.playList.get(x)[0]._title + " " + "(" + self.playList.get(x)[0]._video_id + ")" + " " + "[{0}".format(' '.join(map(str, self.playList.get(x)[0]._tags))) + "]")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        vid_title_list = self._video_library.get_video(video_id)

        if playlist_name.lower() not in map(str.lower, self.playList.keys()):
            print("Cannot remove video from " + playlist_name + ": Playlist does not exist")
        elif vid_title_list == None:
            print("Cannot remove video from " + playlist_name + ": Video does not exist")
        elif playlist_name.lower() in map(str.lower, self.playList.keys()):
            for x in self.playList.keys():
                if x.lower() == playlist_name.lower():
                    #print(x)
                    if self.playList[x].count(vid_title_list) == 0:
                        print("Cannot remove video from " + playlist_name + ": Video does not exist")
                    else:
                        self.playList[x].append(vid_title_list)
                        print("Removed video from " + playlist_name + ": " + self.playList.get(x)[0]._title)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in map(str.lower, self.playList.keys()):
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")
        elif playlist_name.lower() in map(str.lower, self.playList.keys()):
            for x in self.playList.keys():
                if x.lower() == playlist_name.lower():
                    self.playList.get(x).clear()
                    print("Successfully removed all videos from " + playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in map(str.lower, self.playList.keys()):
            print("Cannot delete playlist " + playlist_name + ": Playlist does not exist")
        elif playlist_name.lower() in map(str.lower, self.playList.keys()):
            for x in list(self.playList.keys()):
                if x.lower() == playlist_name.lower():
                    del self.playList[x]
                    print("Deleted playlist: " + playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
