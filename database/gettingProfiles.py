from datetime import datetime, timedelta
from database.dataBaseHandler import DataBase


class Profile:
    def __init__(self, server):
        self.server = server
        self.db = DataBase()

    def sortingByDate(self):
        profiles = []
        listProfiles = self.db.catalogProfiles(self.server)
        counter = 0
        for profile in listProfiles:
            if profile['lastWalk'] != 'NULL':
                lastWalk = datetime.strptime(profile['lastWalk'],
                                             '%Y-%m-%d %H:%M:%S.%f')
                if lastWalk + timedelta(days=1) <= datetime.now():
                    profiles.append(profile)
                    counter += 1

            elif profile['lastWalk'] == 'NULL':
                profiles.append(profile)
                counter += 1

        if counter >= 0:
            return profiles
        else:
            return False

    def sortingByPrivate(self):
        profiles = self.sortingByDate()
        if profiles is not False:
            for profile in profiles:
                if profile['private'] != 1:
                    return profile
            else:
                return False
        else:
            return False

    def getting(self):
        profile = self.sortingByPrivate()
        if profile is not False:
            return profile
        else:
            return False


