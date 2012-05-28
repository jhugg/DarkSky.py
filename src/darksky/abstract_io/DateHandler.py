import datetime as datetime_mod

class DateHandler(object):

    def __init__(
        self,
        utcfromtimestamp = None,
        utcnow = None,
        timedelta = None
    ):
        self.__utcfromtimestamp = datetime_mod.datetime.utcfromtimestamp
        self.__utcnow = datetime_mod.datetime.utcnow()
        self.__timedelta = date

    def toDatetime(
        self,
        unixtime
    ):
        return self.__utcfromtimestamp(unixtime)

    def currentTime():
        return self.__utcnow()

    def getTimeDelta(*args, **kwargs):
        return self.__timedelta(*args, **kwargs)