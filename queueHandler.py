import threading
from database.gettingProfiles import Profile
from execute import Execution
import time


class Handler:
    server = 'instance-1'
    threadList = []

    def loadProfile(self):
        profile = Profile(self.server).getting()
        return profile

    def makeThread(self, profile):
        thread = threading.Thread(target=Execution(profile).case)
        self.threadList.append(thread)

    def handler(self):
        profile = self.loadProfile()
        if profile is not False:
            self.makeThread(profile)
        else:
            time.sleep(20)

        while threading.active_count() >= 2:
            time.sleep(20)


a = Handler().handler()
time.sleep(5)
del a