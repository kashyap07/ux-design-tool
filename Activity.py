import redis
import pickle
from time import time

conn_pool = redis.ConnectionPool(host='localhost', db=1)
redis_cache = redis.StrictRedis(connection_pool=conn_pool)

class Activity(object):
    """Instances of Activity contain a single act captured"""
    
    VERSION = "v0"
    EXPIRATION_TIME = 60 * 20 # seconds
    # versioning db objects is crutial
    # it helps in distinguishing modified objects
    # and prevents breakdown

    # interim, computing id should change
    id = int(time())
    
    def __init__(self):
        self.id = Activity.id
        Activity.id += 1

    # inserts the user activity into the object
    def insert_activity(self, activity):
        self.activity = activity

    # pickle object and save to db
    def save(self):
        cache_key = Activity.get_cache_key(self.id)
        redis_cache.setex(cache_key, Activity.EXPIRATION_TIME, pickle.dumps(self))

    # compute key used to access object
    @staticmethod
    def get_cache_key(id):
        if not id:
            raise Exception("Requires Activity ID")
        return "activity_%s_%d" % (Activity.VERSION, id)

    # gets all keys ever present in db
    @staticmethod
    def get_all_keys(): 
        return redis_cache.keys('activity_' + Activity.VERSION + '_*')

    # gets a single activity from db
    @staticmethod
    def get(id):
        return Activity.get_from_key(Activity.get_cache_key(id))

    # gets all activities from db
    @staticmethod
    def get_all():
        keys = Activity.get_all_keys()
        return map(lambda x: Activity.get_from_key(x), keys)

    # performs actual operation of retrieving from db 
    @staticmethod
    def get_from_key(key):
        activity_pickled = redis_cache.get(key)
        activity = None
        if(activity_pickled):
            activity = pickle.loads(activity_pickled)
        return activity

    # example analysis
    # to use call, Activity.num_clicks(Activity.get_all())
    @staticmethod
    def num_clicks(activity_list):
        nclicks = 0
        for activity in activity_list:
            if "type" in activity.activity and activity.activity["type"] == "click":
                nclicks += 1

        return nclicks
