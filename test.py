a = []
b = []

n = len(a)

a.sort()
b.sort()
c = a - b

for k in range(0, n):
    count = 0
    for i in range(len(c)):
        if (c[i] == -1):
            count += 1
    if (k == count):
        return 1;
    else:
        continue;



# b.sort();
#
# for i in range(0, n):
#     for k in range(0, n):
#         for j in range(0, k-1):
#             a[j] = a[j] + 1;
#     a.sort()
#     if(a == b):
#         return True;
#     else:
#         return False;

