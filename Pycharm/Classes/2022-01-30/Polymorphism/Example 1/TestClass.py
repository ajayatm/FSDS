from MainClass import *

x = Main(1, 2)
print(x.add())

y = Main('Ajay', 'Mani')
print(y.add())

i = Insta()
f = Facebook()


def sharestories(app):
    app.share_stories()


class Social_Media:
    def share_stories(self):
        print("Share stories")


class Facebook(Social_Media):
    def share_stories(self):
        print("Facebook story")


class Insta(Social_Media):
    def share_stories(self):
        print("Insta story")


sharestories(i)
sharestories(f)
i.share_stories()
f.share_stories()

l = Facebook()
m = Insta()

l.share_stories()
m.share_stories()
