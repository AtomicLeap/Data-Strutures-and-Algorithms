# Leetcode 355. Design Twitter

# https://leetcode.com/problems/design-twitter/description/

# Tags -> Design, Hash Table, Linked List

from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.time = 0
        self.follow_map = defaultdict(set)   # follower -> set of followees
        self.tweets = defaultdict(list)      # user -> list of (time, tweetId)

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.time += 1
        self.tweets[user_id].append((self.time, tweet_id))

    def get_news_feed(self, user_id: int) -> list[int]:
        result = []
        max_heap = []

        users = set(self.follow_map[user_id])
        users.add(user_id)  # user always sees own tweets

        # Push each user's most recent tweet into heap
        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                time, tweet_id = self.tweets[user][idx]
                # use negative time because heapq is a min-heap
                heapq.heappush(max_heap, (-time, tweet_id, user, idx))

        # Extract up to 10 most recent tweets
        while max_heap and len(result) < 10:
            _, tweet_id, user, idx = heapq.heappop(max_heap)
            result.append(tweet_id)

            # Push the previous tweet from the same user
            if idx > 0:
                prev_time, prev_tweet_id = self.tweets[user][idx - 1]
                heapq.heappush(max_heap, (-prev_time, prev_tweet_id, user, idx - 1))

        return result

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id != followee_id:
            self.follow_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.follow_map[follower_id].discard(followee_id)


# Let f be the number of followed users plus the user themself.
# pushing initial latest tweets: O(f log f)
# extracting at most 10 tweets: O(10 log f)

# So overall:

# Time: O(f log f)
# Space: O(f)

twitter = Twitter()
twitter.post_tweet(1, 5)
print(twitter.get_news_feed(1))
twitter.follow(1, 2)
twitter.post_tweet(2, 6)
print(twitter.get_news_feed(1))
twitter.unfollow(1, 2)
print(twitter.get_news_feed(1))
