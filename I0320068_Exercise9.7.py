7.
# mengonversi string ke dalam array.array
B = array.array('b')
B.fromstring("Python")
B
for karakter in B:
    print("%c " % karakter, end='')