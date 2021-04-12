#!/usr/bin/env python3

import time
import threading
from collectionObject import Collection
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
        thread = threading.Thread(target=Collection(profile).case)
        thread.start()
        self.threadList.append(thread)

    def newConfig(self):
        profile = ProfileGenerator()
        profile.make(self.server)
        del profile

    def handler(self):
        while True:
            profile = self.loadProfile()
            if profile is not False:
                self.makeThread(profile)
            else:
                self.newConfig()

            while threading.active_count() >= 2:
                time.sleep(20)

            for thread in self.threadList:
                thread.join()



if __name__ == '__main__':
    handler = Handler()
    handler.handler()
