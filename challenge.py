from warmup1 import zeroremover
from warmup2 import sort_descending
from warmup3 import length_check
from warmup4 import front_elimination


def havel_hakimi(sequence):
    seq = sequence[:]
    while seq:
        seq = zeroremover(seq)
        if not seq:
            break
        seq = sort_descending(seq)
        number = seq[0]
        seq = seq[1:]
        if length_check(number, seq):
            return False
        seq = front_elimination(number, seq)

    return True
