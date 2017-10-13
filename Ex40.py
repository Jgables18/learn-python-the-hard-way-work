class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def Sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy Birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                         "With pockets full of shells"])

happy_bday.Sing_me_a_song()

bulls_on_parade.Sing_me_a_song()
