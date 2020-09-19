
# (1, 3); (3, 6); (8, 14); (10, 21); (4, 25)

import collections

Interval = collections.namedtuple('Interval', ('start', 'end'))

def merge_intervals(A):
    # sort the intervals.
    # new_interval and iterate over the list.

    A.sort(key=lambda a: (a[0], a[1]))
    A = [Interval(a[0], a[1]) for a in A]
    new_interval = Interval(A[0].start, A[0].end)

    res = []

    for interval in A:
        if interval.start <= new_interval.end:
            new_interval = Interval( min(new_interval.start, interval.start),
                                     max(new_interval.end, interval.end) )
        else:
            res.append(new_interval)
            new_interval = interval

    res.append(new_interval)
    res = [(a.start, a.end) for a in res]
    return res

if __name__ == "__main__":
    A = [(1,3), (3,6), (8,14), (10,21)]
    print (merge_intervals(A))
