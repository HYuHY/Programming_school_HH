"""
Solution for the task 'Infinity Sequence'
Full task description in:
The_Task_2nd_level_selection_infinity_sequence.mhtml

Created on 10 oct. 2017.
@author: HYuHY
"""

# sequence - int

def find_sequence(sequence):
    def compare_frame(frame, next_frame, len_frame, pos):
        # сравниваем наличные элементы frame с тем, 
        # что должно быть если следующий фрейм увеличил количество разрядов
        if str(next_frame - 1)[-(len_frame - pos):] == "".join(frame[pos:]):
            match = True
        else:
            match = False
        return match, [n for n in str(next_frame - 1) if n.isdigit()]

    def check_resize_next_frame(frame, len_frame, pos, seq):
        if pos > 0:
            if len(seq[len_frame - pos:]) >= len_frame + 1:
                next_frame = [seq[len_frame - pos + num] for num in range(0, len_frame + 1)]
            else:
                next_frame = []
                next_frame[0:] = seq[len_frame - pos:]
                next_frame = next_frame + ['0'] * (len_frame - len(next_frame))
            next_frame = int(''.join(next_frame))
            match, frame = compare_frame(frame, next_frame, len_frame, pos)
        else:
            next_frame = int(''.join(frame)) + 1
            match, frame = compare_frame(frame, next_frame, len_frame, pos)
        return match, frame

    def check_guess_seq(frame, seq, len_seq):
        guess_seq = ""
        cur_frame = ''.join(frame)
        while len(guess_seq) < len_seq:
            guess_seq = "".join(guess_seq) + "".join(cur_frame)
            cur_frame = str(int(cur_frame) + 1)
            if seq in guess_seq:
                return True
        return False

    frame = [None, ]
    seq = str(sequence)
    len_seq = len(seq)
    while len(frame) <= len_seq:  # постепенно увеличиваем размер фрейма
        len_frame = len(frame)
        for pos in range(0, len_frame):  # смещаем первое число из последовательности по фрейму вправо
            frame[pos:] = seq[0:(len_frame - pos)]
            if frame[-1] == '9':
                match, frame = check_resize_next_frame(frame, len_frame, pos, seq)
                if match:
                    finded = check_guess_seq(frame, seq, len_seq)
                    if finded:
                        return int("".join(frame))
            if len_seq > 1:
                frame[0:pos] = seq[len_frame - pos: len_frame]
                finded = check_guess_seq(frame, seq, len_seq)
                if finded:
                    return int("".join(frame))
            else:
                finded = check_guess_seq(frame, seq, len_seq)
                if finded:
                    return int("".join(frame))
            frame = [None] * len_frame
        frame = [None] * (len_frame + 1)


def main(sequence):
    answer = find_sequence(sequence)
    print("первое вхождение заданной последовательности начинается с числа:\n", answer)
    return answer


if __name__ == "__main__":
    sequence = 837457843346455
    answer = main(sequence)
