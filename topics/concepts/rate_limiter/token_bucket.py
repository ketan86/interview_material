"""
Token bucket algorithm to rate limit APIs requests.
"""
# pylint:skip-file
import time

class TokenBucket:
    def __init__(self, tokens, fill_rate):
        """
        Constructs `class:TokenBucket` instance.

        :param int tokens:
            A number of tokens.
        :param float fill_rate:
            A fill rate in tokens/second.
        """
        self.capacity = tokens
        self.tokens = tokens
        self.fill_rate = fill_rate
        self.prev_fill_time = int(time.time())

    def consume(self, tokens):
        # refill the tokens based on the time difference and fill rate.
        self._refill()
        # if requested tokens are less than equal to current tokens.
        # consume them by reducing them from current tokens.
        if tokens <= self.tokens:
            self.tokens -= tokens
            return True
        return False

    def _refill(self):
        # if current tokens is less than the capacity. refill required
        if self.tokens < self.capacity:
            now = int(time.time())
            delta = self.fill_rate * (now - self.prev_fill_time)
            # current tokens will min of capacity or current tokens + addition
            self.tokens = min(self.capacity, self.tokens + delta)
            # set prev fill time to current time.
            self.prev_fill_time = now