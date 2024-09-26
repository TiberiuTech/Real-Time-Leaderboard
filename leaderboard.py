import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

LEADERBOARD_KEY = 'game_leaderboard'

def add_score(username, score):
    redis_client.zadd(LEADERBOARD_KEY, {username: score})

def get_top_players(n):
    return redis_client.zrevrange(LEADERBOARD_KEY, 0, n - 1, withscores=True)

def get_rank(username):
    rank = redis_client.zrevrank(LEADERBOARD_KEY, username)
    return rank + 1 if rank is not None else None
