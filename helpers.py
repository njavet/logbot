def correct_payload(words):
    s = stronglift_msg_correct(words)
    r = running_msg_correct(words)
    c = cycling_msg_correct(words)
    h = heavybag_msg_correct(words)
    if any([s, r, c, h]):
        return True
    else:
        return False


def stronglift_msg_correct(words):
    try:
        reps0 = words[0].split(',')
        weights0 = words[1].split(',')
        breaks0 = words[2].split(',')
    except IndexError:
        print('stronglift msg error: IndexError')
        return False

    try:
        reps1 = list(map(lambda e: int(e), reps0))
        weights1 = list(map(lambda e: int(e), weights0))
        breaks1 = list(map(lambda e: int(e), breaks0))
    except ValueError:
        print('stronglift msg error: ValueError')
        return False

    if len(reps1) != len(weights1) != 5:
        print('stronglift msg error: reps != weights')
        return False

    if len(breaks1) != 4:
        print('stronglift msg error: reps != breaks+1')
        return False

    if not all(list(map(lambda e: 0 < e < 8, reps1))):
        print('stronglift msg error: 0 < rep < 8')
        return False

    if not all(list(map(lambda e: 0 < e < 200, weights1))):
        print('stronglift msg error: 0 < weight < 200')
        return False

    if not all(list(map(lambda e: 0 < e < 300, breaks1))):
        print('stronglift msg error: 0 < break < 300')
        return False


def running_msg_correct(words):
    try:
        time0 = words[0]
        distance0 = words[1]
        rnd_ts0 = words[2]
    except IndexError:
        print('running msg error: IndexError')
        return False

    try:
        time1 = int(time0)
        distance1 = int(distance0)
        rnd_ts1 = list(map(lambda e: int(e), rnd_ts0))
    except ValueError:
        print('running msg error: ValueError')
        return False

    if not 0 < time1 < 3600:
        print('running msg error: 0 < time < 3600')
        return False

    if not 0 < distance1 < 20000:
        print('running msg error: 0 < distance < 20000')
        return False

    if not all(list(map(lambda e: 0 < e < 600, rnd_ts1))):
        print('running msg error: 0 < rnd_ts < 600')
        return False


def cycling_msg_correct(words):
    try:
        time0 = words[0]
        avgperf0 = words[1]
        calories0 = words[2]
    except IndexError:
        print('cycling msg error: IndexError')
        return False

    try:
        time1 = int(time0)
        avgperf1 = int(avgperf0)
        calories1 = int(calories0)
    except ValueError:
        print('cycling msg error: ValueError')
        return False

    if not 0 < time1 < 3600:
        print('cycling msg error: 0 < time < 3600')
        return False

    if not 0 < avgperf1 < 300:
        print('cycling msg error: 0 < avgperfm < 300')
        return False

    if not 0 < calories1 < 1000:
        print('cycling msg error: 0 < calories < 1000')
        return False


def heavybag_msg_correct(words):
    try:
        rounds0 = words[0]
        rnd_t0 = words[1]
        break_t0 = words[2]
    except IndexError:
        print('heavybag msg error: IndexError')
        return False

    try:
        rounds1 = int(rounds0)
        rnd_t1 = int(rnd_t0)
        break_t1 = int(break_t0)
    except ValueError:
        print('heavybag msg error: ValueError')
        return False

    if not 0 < rounds1 < 16:
        print('heavybag msg error: 0 < rounds < 16')
        return False

    if not 0 < rnd_t1 < 300:
        print('heavybag msg error: 0 < rnd_t1 < 300')
        return False

    if not 0 < break_t1 < 60:
        print('heavybag msg error: 0 < break < 60')
        return False







