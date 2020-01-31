import copy



num_painters = 3

board_sizes = [12, 13, 5, 1, 5, 6, 10, 12, 30, 4, 2]


def max_segment(num_segments, board_sizes, work_for_first_painter):
    board_sizes_copy_1 = copy.copy(board_sizes)
    board_sizes_copy_2 = copy.copy(board_sizes)

    if num_segments == 1:
        return sum(board_sizes)

    if len(board_sizes) == 0:
        return work_for_first_painter

    first_elem = board_sizes_copy_1.pop(0)
    board_sizes_copy_2.pop(0)

    return min(
        max(work_for_first_painter + first_elem, max_segment(num_segments - 1, board_sizes_copy_1, 0)),
        max_segment(num_segments, board_sizes_copy_2, work_for_first_painter + first_elem)
    )



print max_segment(num_painters, board_sizes, 0)
