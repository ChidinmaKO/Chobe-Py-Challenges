def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    averages = []
    for i in range(1, len(sequence)+1):
        seq_sum = 0
        for num in sequence[:i]:
            seq_sum += num
            result = seq_sum / i
        averages.append(round(result, 2))
        
    return averages




# tests
import pytest

from running_mean import running_mean


@pytest.mark.parametrize("input_argument, expected_return", [
    ([1, 2, 3], [1, 1.5, 2]),
    ([2, 6, 10, 8, 11, 10],
     [2.0, 4.0, 6.0, 6.5, 7.4, 7.83]),
    ([3, 4, 6, 2, 1, 9, 0, 7, 5, 8],
     [3.0, 3.5, 4.33, 3.75, 3.2, 4.17, 3.57, 4.0, 4.11, 4.5]),
    ([], []),
])
def test_running_mean(input_argument, expected_return):
    ret = list(running_mean(input_argument))
    assert ret == expected_return