#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

"""Cache that uses Redis to store cached values."""

import logging
import pickle

import redis


class BaseMessage:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


class RedisCache:
    """Cache that uses Redis to store cached values."""

    def __init__(self):
        self.initialize_redis()

    def initialize_redis(self) -> None:
        """Initialize the Redis client and logging.

        This method sets up the Redis client with custom configuration parameters.
        """
        # initialize Redis client
        self.redis_client = redis.StrictRedis(
            host="localhost",
            port=6379,
            decode_responses=False,  # we store serialized messages as bytes, not strings
        )
        # Set custom configuration parameters

    def get(self, user_id: str, conversation_id: str):
        """Get the value associated with the given key.

        Args:
            user_id: User identification.
            conversation_id: Conversation ID unique for given user.

        Returns:
            The value associated with the key, or None if not found.
        """
        key = user_id + ":" + conversation_id

        value = self.redis_client.get(key)
        if value is None:
            return None
        return pickle.loads(value, errors="strict")  # noqa S301

    def insert_or_append(self, user_id: str, conversation_id: str, value) -> None:
        """Set the value associated with the given key.

        Args:
            user_id: User identification.
            conversation_id: Conversation ID unique for given user.
            value: The value to set.

        Raises:
            OutOfMemoryError: If item is evicted when Redis allocated
                memory is higher than maxmemory.
        """
        key = user_id + ":" + conversation_id

        while True:
            with self.redis_client.pipeline(transaction=True) as pipeline:
                try:
                    logging.debug("Transaction started")
                    pipeline.watch(key)
                    old_value = self.get(user_id, conversation_id)
                    pipeline.multi()
                    if old_value:
                        old_value.extend(value)
                        pipeline.set(
                            key,
                            pickle.dumps(old_value, protocol=pickle.HIGHEST_PROTOCOL),
                        )
                    else:
                        pipeline.set(
                            key, pickle.dumps(value, protocol=pickle.HIGHEST_PROTOCOL)
                        )
                    pipeline.execute()
                    pipeline.unwatch()
                    logging.debug("Transaction finished")
                    break
                except redis.WatchError as err:
                    logging.info("Watch error", err)
