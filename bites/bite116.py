import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    large_files = []
    # one way

    # files_dirname = os.scandir(dirname)
    # for file in files_dirname:
    #     if file.is_file():
    #         size = file.stat().st_size
    #         if size >= size_in_kb * ONE_KB:
    #             large_files.append(file.name)
    # return large_files

    # another way
    with os.scandir(dirname) as files_dirname:
        for file in files_dirname:
            if file.is_file() and file.stat().st_size >= size_in_kb * ONE_KB:
                large_files.append(file.name)
        return large_files

# tests
# import os
from tempfile import TemporaryDirectory

# import pytest

# from files import ONE_KB, get_files

TMP = '/tmp'


def _create_files(dirname):
    for i in range(1, 4):
        for j in range(1, 11):
            file_size = i * j * ONE_KB
            filename = f'{file_size}.txt'
            path = os.path.join(dirname, filename)
            _create_file(path, file_size)


def _create_file(path, size):
    with open(path, 'wb') as f:
        f.write(os.urandom(size))


@pytest.mark.parametrize("size", [
    1, 3, 6, 9, 12, 20, 25,
])
def test_get_files(size):
    with TemporaryDirectory(dir=TMP) as dirname:
        test_size_in_kb = size * ONE_KB
        _create_files(dirname)

        files = list(get_files(dirname, test_size_in_kb))
        filenames = [os.path.splitext(os.path.basename(f))[0] for f in files]

        assert all(int(fn) >= test_size_in_kb for fn in filenames)
                
    
    