#1
import array, tempfile
a = array.array('b', [10, 20, 30])
a.append(40)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(20):", a.count(20))
a.extend([50, 60])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:1])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([5, 15])
print("index(10):", a.index(10))
a.insert(1, 25)
print("pop:", a.pop(0))
a.remove(20)
a.reverse()
print("Final 'b':", a)


#2
import array, tempfile
a = array.array('B', [0, 100, 200])
a.append(255)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(100):", a.count(100))
a.extend([10, 20])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:1])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([50, 60])
print("index(100):", a.index(100))
a.insert(0, 5)
print("pop:", a.pop())
a.remove(100)
a.reverse()
print("Final 'B':", a)


#3
import array, tempfile
a = array.array('u', 'abc')
a.append('d')
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count('b'):", a.count('b'))
a.extend(['e', 'f'])
try:
    print("tounicode:", a.tounicode())
    a.fromunicode("gh")
except AttributeError:
    pass
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:2])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist(['x', 'y'])
print("index('b'):", a.index('b'))
a.insert(1, 'z')
print("pop:", a.pop(0))
a.remove('b')
a.reverse()
print("Final 'u':", a)


#4
import array, tempfile
a = array.array('h', [-1000, 0, 1000])
a.append(2000)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(0):", a.count(0))
a.extend([3000, 4000])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:2])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([500, 600])
print("index(0):", a.index(0))
a.insert(1, 150)
print("pop:", a.pop())
a.remove(0)
a.reverse()
print("Final 'h':", a)


#5
import array, tempfile
a = array.array('H', [1000, 2000, 3000])
a.append(65000)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(2000):", a.count(2000))
a.extend([4000, 5000])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:2])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([100, 200])
print("index(2000):", a.index(2000))
a.insert(0, 500)
print("pop:", a.pop())
a.remove(2000)
a.reverse()
print("Final 'H':", a)


#6
import array, tempfile
a = array.array('i', [-100000, 0, 100000])
a.append(200000)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(0):", a.count(0))
a.extend([300000, 400000])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:4])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([50, 60])
print("index(0):", a.index(0))
a.insert(2, 5000)
print("pop:", a.pop())
a.remove(0)
a.reverse()
print("Final 'i':", a)


#7
import array, tempfile
a = array.array('I', [100000, 200000, 300000])
a.append(400000)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(200000):", a.count(200000))
a.extend([500000, 600000])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:4])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([10, 20])
print("index(200000):", a.index(200000))
a.insert(1, 150000)
print("pop:", a.pop())
a.remove(200000)
a.reverse()
print("Final 'I':", a)


#8
import array, tempfile
a = array.array('l', [-500000, 0, 500000])
a.append(1000000)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(0):", a.count(0))
a.extend([2000000, 3000000])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:4])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([100, 200])
print("index(0):", a.index(0))
a.insert(0, -1000)
print("pop:", a.pop())
a.remove(0)
a.reverse()
print("Final 'l':", a)


#9
import array, tempfile
a = array.array('L', [1000000, 2000000, 3000000])
a.append(4000000)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(2000000):", a.count(2000000))
a.extend([5000000, 6000000])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:4])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([10, 20])
print("index(2000000):", a.index(2000000))
a.insert(1, 1500000)
print("pop:", a.pop())
a.remove(2000000)
a.reverse()
print("Final 'L':", a)


#10
import array, tempfile
a = array.array('q', [-9000000000, 0, 9000000000])
a.append(10000000000)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(0):", a.count(0))
a.extend([20000000000, 30000000000])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:8])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([500, 600])
print("index(0):", a.index(0))
a.insert(1, 12345)
print("pop:", a.pop())
a.remove(0)
a.reverse()
print("Final 'q':", a)


#11
import array, tempfile
a = array.array('Q', [10000000000, 20000000000, 30000000000])
a.append(40000000000)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(20000000000):", a.count(20000000000))
a.extend([50000000000, 60000000000])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:8])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([10, 20])
print("index(20000000000):", a.index(20000000000))
a.insert(0, 9999)
print("pop:", a.pop())
a.remove(20000000000)
a.reverse()
print("Final 'Q':", a)


#12
import array, tempfile
a = array.array('f', [1.5, 2.5, 3.5])
a.append(4.5)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(2.5):", a.count(2.5))
a.extend([5.5, 6.5])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:4])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([0.5, 0.75])
print("index(2.5):", a.index(2.5))
a.insert(1, 1.75)
print("pop:", a.pop())
a.remove(2.5)
a.reverse()
print("Final 'f':", a)


#13
import array, tempfile
a = array.array('d', [3.14159, 2.71828, 1.41421])
a.append(1.61803)
print("buffer_info:", a.buffer_info())
a.byteswap()
a.byteswap()
print("count(2.71828):", a.count(2.71828))
a.extend([0.57721, 1.20205])
raw_bytes = a.tobytes()
a.frombytes(raw_bytes[:8])
with tempfile.TemporaryFile() as f:
    a.tofile(f)
    f.seek(0)
    a.fromfile(f, 2)
py_list = a.tolist()
a.fromlist([9.81, 1.0])
print("index(2.71828):", a.index(2.71828))
a.insert(2, 0.0)
print("pop:", a.pop())
a.remove(2.71828)
a.reverse()
print("Final 'd':", a)

