import time
import threading
from execute import Execution
from database.gettingProfiles import Profile
from generator.profile import ProfileGenerator


class Handler:
    server = 'instance-1'
    threadList = []

    def loadProfile(self):
        profile = Profile(self.server).getting()
        return profile

    def makeThread(self, profile):
        print(profile['name'])
        thread = threading.Thread(target=Execution(profile).case)
        self.threadList.append(thread)

    def newConfig(self):
        profile = ProfileGenerator()
        profile.make(self.server)
        del profile

    def handler(self):
        profile = self.loadProfile()
        if profile is not False:
            self.makeThread(profile)
        else:
            time.sleep(20)

        while threading.active_count() >= 2:
            time.sleep(20)
        else:
            self.newConfig()


a = Handler().handler()
time.sleep(5000)
del a
