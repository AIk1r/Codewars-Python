# DESCRIPTION:
# Task
# "Given an array of queues, how many times must you perform dequeueing operations, for each number to end up in its associated queue?"
# queues                          perfect

# [[0, 1], [2], [1, 1]]     ->    [[0], [1, 1, 1], [2]]
# Input
  # queues
  # an array of zero, one or more queues
  # each queue is an array containing zero, one or more non-negative integers
  # each number is within the range: 0 ≤ n < number of queues
  # the head of a queue is the right-most item
  # the tail of a queue is the left-most item
  # dequeueing an element from a queue is taking the head
  # enqueueing an element to a queue is prepending it to the tail
# Output
  # return a non-negative integer representing the number of dequeueing operations to get each number to end up in its associated queue
  # the associated queue for a number n is the queue at 0-based index n of the input array of queues
  # empty is a valid terminal state for any queue
  # empty is a valid terminal state for the array of queues
# Algorithm
# Your code should yield the same outcome as the algorithm described below, but should be more efficient than this naive approach,
# and you can use any algorithm you want to get the job done.

# start at queue 0
# keep performing the following actions until all queues have entered a terminal state
# if the current queue has reached a terminal state, move to next queue
# moving from the last queue to the next, takes you back to the first queue
# otherwise dequeue a number of the current queue and enqueue it to the associated queue of that number; that queue becomes the new current queue
# keep track of each time you dequeue a number and return the total amount of dequeueing operations

def dequeue_count(que):
    count = 0
    for i in range(len(que)):
        for j in range(len(que[i])):
            if que[i][j] != i:
                count += len(que[i]) - j
                break
    return count
