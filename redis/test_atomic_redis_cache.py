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

import multiprocessing
import time

PRODUCER_CYCLES = 100
PRODUCER_SLEEP_TIME = 0.1

USER_ID = "1234"
CONVERSATION_ID = "5678"


from redis_cache import BaseMessage, RedisCache


def producer_1(cycles, user_id, conversation_id, sleep_time):
    redis_cache = RedisCache()

    for i in range(cycles):
        message = [BaseMessage(f"message #{i}")]
        redis_cache.insert_or_append(user_id, conversation_id, message)
        time.sleep(sleep_time)


def producer_2(cycles, user_id, conversation_id, sleep_time):
    redis_cache = RedisCache()

    for i in range(cycles):
        message = [BaseMessage("second producer")]
        redis_cache.insert_or_append(user_id, conversation_id, message)
        time.sleep(sleep_time)


def test_atomic_insert_or_append():
    redis_cache = RedisCache()

    # make sure the conversation is cleared before testing
    redis_cache.redis_client.delete(USER_ID + ":" + CONVERSATION_ID)

    queue = multiprocessing.Queue()

    # construct both producers
    producer_1_process = multiprocessing.Process(
        target=producer_1,
        args=(PRODUCER_CYCLES, USER_ID, CONVERSATION_ID, PRODUCER_SLEEP_TIME),
    )
    producer_2_process = multiprocessing.Process(
        target=producer_2,
        args=(PRODUCER_CYCLES, USER_ID, CONVERSATION_ID, PRODUCER_SLEEP_TIME),
    )

    start_time = time.perf_counter()

    # start both producers
    producer_1_process.start()
    producer_2_process.start()

    # wait for producers
    print("Waiting for producers to finish")
    producer_1_process.join()
    producer_2_process.join()
    print("Finished")

    # compute duration
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Duration: {duration:4.3} seconds")

    # read messages from cache and perform elementary checks
    messages = redis_cache.get(USER_ID, CONVERSATION_ID)
    assert len(messages) == PRODUCER_CYCLES * 2

    # PRODUCER_CYCLES messages needs to be in cache in proper order
    index = 0
    for message in messages:
        if message.content == "second producer":
            continue
        expected = f"message #{index}"
        assert message.content == expected, f"Wrong message content {message.content}"
        index += 1


if __name__ == "__main__":
    print("Running test")
    test_atomic_insert_or_append()
