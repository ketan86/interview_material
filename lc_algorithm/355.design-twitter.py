#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from collections import defaultdict
import heapq
import time


class Twitter:
    """There are two ways this can be solved,

    1. maintain min_heap for each user and maintain max 10 tweets
        - run time affected because of this but saves space.
    2. calculate top tweets during the `getNewsFeed` time
        - we will maintain all the tweets of the user (not space efficient)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = defaultdict(set)
        # max heap to maintain top 10 tweets per user by time
        self.tweets = defaultdict(list)
        self.max_tweets = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # only maintain 10 tweets for each user
        if self.tweets[userId] and len(self.tweets[userId]) == self.max_tweets:
            heapq.heapreplace(self.tweets[userId], (time.time(), tweetId))
        else:
            heapq.heappush(self.tweets[userId], (time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item 
        in the news feed must be posted by users who the user followed or by the 
        user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = []

        # add all tweets of the main user into the min_heap
        for timestamp, tweet_id in self.tweets[userId]:
            heapq.heappush(tweets, (timestamp, tweet_id))

        # go find all followers and update the tweets
        for followerId in self.followers[userId]:
            for timestamp, tweet_id in self.tweets[followerId]:
                if len(tweets) == self.max_tweets:
                    heapq.heapreplace(tweets, (timestamp, tweet_id))
                else:
                    heapq.heappush(tweets, (timestamp, tweet_id))

        # find top largest (latest by timestamp) tweets
        top_ten = heapq.nlargest(self.max_tweets, tweets)

        return [x[1] for x in top_ten]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be 
        a no-op.
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower un-follows a followee. If the operation is invalid, it should 
        be a no-op.
        """
        self.followers[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
