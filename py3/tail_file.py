import os
import sys

def tail_file(file_path, lines=10, force=False):
    if not os.path.isfile(file_path):
        print('file dose not exist.')
    f = open(file_path, 'rb')
    chunk_size = 50
    content_cache = []
    # line_count = 0
    # move position
    f.seek(-chunk_size, 2)
    data = f.read(chunk_size)
    _lines = data.splitlines(True)
    content_cache = _lines
    while len(content_cache) < lines:
        if content_cache and _lines:
            last_line = content_cache[-1]
            if last_line[-1] in ('\n', '\r'):
                content_cache.extend(_lines)
            else:
                last_line += _lines[0]
                content_cache[-1] = last_line
                if len(_lines) > 1:
                    content_cache.extend(_lines[1:])
            f.seek(-chunk_size, 1)
            data = f.read(chunk_size)
            _lines = data.splitlines(True)
        else:
            break
    print(content_cache[-lines-1:])
    f.close()


if __name__ == '__main__':
    args = sys.argv
    print(args)
    if len(args) < 2:
        print('require file path.')
    else:
        tail_file(args[1])
