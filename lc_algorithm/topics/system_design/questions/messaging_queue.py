"""

We have to design a message queue supporting publisher-subscriber model.
It should support following operations:

1. It should support multiple topics where messages can be published.
2. Publisher should be able to publish a message to a particular topic.
3. Subscribers should be able to subscribe to a topic.
4. Whenever a message is published to a topic, all the subscribers, who are
   subscribed to that topic, should receive the message.
5. Subscribers should be able to run in parallel


createTopic(topicName) -> topicId
subscribe(topicId, subscriber) -> boolean
publish(topicId, message) -> boolean
resetOffset(topidId, subscriber, offset) -> boolean




publisher        MessagingService        subscriber-1       subscriber-2
    |  create -> t1,t2   |                     |   t1 <-- subscribe  |
    |------------------->|<--------------------|---------------------|
    |                    |<--------------------|                     |
    |                    | t2,t1 <-- subscribe |                     |
    |                    |                     |                     |
    |  msg -> (t1, hi)   |                     |                     |
    |------------------->|         hi          |                     |
    |                    |-------------------->|      hi             |
    |                    |---------------------|-------------------->|
    |                    |         hi          |                     |
    |  msg -> (t2, hello)|                     |                     |
    |------------------->|         hello       |                     |
    |                    |-------------------->|                     |


Threads: 
    1. Thread/Subscriber to manage sending of the message to subscriber
    2. Thread/Published_Message to accept message from publisher and
       to send to all subscribed users.
    3. Thread/OffsetReset to push messages from the offset till current to
       subscribed user of that offset change. 

Classes:
    1. Message
    2. ISubscriber
    3. SleepingSubscriber
    4. TopicSubscriber
    5. Topic - Needs Lock to allow writting messages in order
    6. TopicHandler
    7. SubscriberWorker - Condition(wait, notify) with Lock to consume till 
            current offset and wait until new message is published.
    8. MessagingService

"""
import time
import abc
import threading
import concurrent.futures

class Message:
    """
    Represents message.
    """
    def __init__(self, data:str) -> None:
        self.data = data

class ISubscriber(abc.ABC):
    """
    Abstract subscriber class
    """
    @abc.abstractmethod
    def consume(self, message: Message, offset: int) -> None:
        """
        Consume published messages with concrete implementation.
        """
        raise NotImplementedError()

class SleepingSubscriber(ISubscriber):
    """
    Concrete implementation of the subscriber class.
    """

    def __init__(self, name: str, sleep_time: float) -> None:
        self.name = name
        self.sleep_time = sleep_time

    def consume(self, message: Message, offset: int) -> None:
        """
        Consume message with delay.
        """
        # print(f'Subscriber name={self.name}, started consuming msg={message.data} at {offset=}')
        time.sleep(self.sleep_time)
        print(f'Subscriber name={self.name}, consumed msg={message.data} at {offset=}')


class TopicSubscriber:
    """Represents a subscriber of a given topic"""
    def __init__(self, subscriber: ISubscriber) -> None:
        self.subscriber = subscriber
        self.offset = 0

    def reset_offset(self) -> None:
        """Reset the offset"""
        self.offset = 0

    def increment_offset(self, prev_offset: int) -> None:
        """Increment offset if prev offset value matches the current offset"""
        if prev_offset == self.offset:
            self.offset += 1

class Topic:
    """Topic to store messages in order of their publish time"""
    def __init__(self, name:str) -> None:
        self.name = name
        self.messages = []
        self.subscribers = []
        self.lock = threading.Lock()

    def add_message(self, message: str) -> None:
        """Add message to the topic"""
        # Acquire lock before updating the message queue.
        with self.lock:
            self.messages.append(Message(message))

    def add_subscriber(self, subscriber: TopicSubscriber) -> None:
        self.subscribers.append(subscriber)


class TopicHandler:
    """Handler responsible for pushing messages to subscribers"""
    def __init__(self, topic: Topic, workers: int=10) -> None:
        self.topic = topic
        # create thread pool to for concurrent message handling
        self.thread_pool = concurrent.futures.ThreadPoolExecutor(workers)
        self.t_subscribers = {}

    def shutdown(self) -> None:
        # terminate running thread
        for t_sub in self.t_subscribers.keys():
            self.t_subscribers[t_sub].terminate()

        # shutdown thread pool executor
        self.thread_pool.shutdown(wait=True)

    def publish(self) -> None:
        # publish message to all subscriber of this topic
        for t_sub in self.topic.subscribers:
            self.start_subscriber_worker(t_sub)

    def start_subscriber_worker(self, t_sub:TopicSubscriber) -> None:
        print(t_sub)
        # submit notify job to subscriber worker if topic subscriber was
        # consuming messages before.
        if t_sub not in self.t_subscribers:
            self.t_subscribers[t_sub] = SubscriberWorker(self.topic, t_sub)
            self.thread_pool.submit(
                self.t_subscribers[t_sub].notify)
        else:
            # just poke the subscriber to indicate that new message has
            # be pushed.
            self.t_subscribers[t_sub].poke()

class SubscriberWorker:
    """Worker that is responsible of pushing messages to subscriber"""
    def __init__(self, topic: Topic, topic_sub: TopicSubscriber):
        self.topic = topic
        self.topic_sub = topic_sub
        self.condition = threading.Condition()
        self.exit = False
    
    def terminate(self) -> None:
        self.exit = True
        with self.condition:
            self.condition.notify()

    def notify(self) -> None:
        while True:
            with self.condition:
                curr_offset = self.topic_sub.offset
                while curr_offset >= len(self.topic.messages):
                    if self.exit:
                        return
                    self.condition.wait()
                    # read current offset when poked to read the up-to date
                    # offset value
                    curr_offset = self.topic_sub.offset
                message = self.topic.messages[curr_offset]
                self.topic_sub.subscriber.consume(message, curr_offset)
                self.topic_sub.increment_offset(curr_offset)

    def poke(self) -> None:
        """Wakes up the worker to notify subscriber for new message"""
        with self.condition:
            self.condition.notify()



class MessagingService:
    """Messaging queue service implementation"""
    def __init__(self) -> None:
        # stores all topic handlers
        self.topic_handlers = {}
        self.threads = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # join all threads
        for t in self.threads:
            t.join()
        # shutdown threadpool executor running per handler
        for t_h in self.topic_handlers.keys():
            self.topic_handlers[t_h].shutdown()

    def create_topic(self, name: str) -> None:
        """
        Create a new topic and add it to handler.
        """
        topic = Topic(name)
        self.topic_handlers[name] = TopicHandler(topic)
        return topic

    def subscribe(self, sub_name: str, topic: Topic) -> None:
        """
        Subscribe to a topic.
        """
        topic.add_subscriber(TopicSubscriber(sub_name))

    def publish(self, topic: Topic, msg: str) -> None:
        """
        Publish message to a topic"""
        topic.add_message(msg)
        # spawn a new thread to notify handler about the new message.
        t = threading.Thread(target=self.topic_handlers[topic.name].publish)
        t.start()

    def reset_offset(self, topic: Topic, subscriber: ISubscriber, offset: int) -> bool:
        for t_sub in topic.subscribers:
            if t_sub.subscriber == subscriber:
                t_sub.offset = offset
                t = threading.Thread(
                    target=self.topic_handlers[
                        topic.name].start_subscriber_worker, args=(t_sub,))
                t.start()
                return True
        return False


with MessagingService() as ms:
    subscriber = SleepingSubscriber('sub1', 0.1)
    subscriber2 = SleepingSubscriber('sub2', 0.1)
    # subscriber3 = SleepingSubscriber('sub3', 0.1)
    # subscriber4 = SleepingSubscriber('sub4', 0.1)
    # subscriber5 = SleepingSubscriber('sub5', 0.1)
    # subscriber6 = SleepingSubscriber('sub6', 0.1)
    # subscriber7 = SleepingSubscriber('sub7', 0.1)
    topic = ms.create_topic('product')
    ms.subscribe(subscriber, topic)
    # ms.subscribe(subscriber2, topic)
    # ms.subscribe(subscriber3, topic)
    # ms.subscribe(subscriber4, topic)
    # ms.subscribe(subscriber5, topic)
    # ms.subscribe(subscriber6, topic)
    # ms.subscribe(subscriber7, topic)
    i = 0
    while i < 10:
        ms.publish(topic, 'Car')
        # ms.publish(topic, 'Truck')
        # ms.publish(topic, 'Bus')
        # ms.publish(topic, 'Cycle')
        # ms.publish(topic, 'Tri-Cycle')
        # ms.publish(topic, 'Van')
        # ms.publish(topic, 'Mini')
        print('-----------')
        i += 1
    time.sleep(5)
    ms.reset_offset(topic, subscriber, 5)

