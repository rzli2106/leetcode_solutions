with open("mixmilk.in", "r") as file_in:
    lines = file_in.read().splitlines()



c = [0] * 3
m = [0] * 3

for i in range(3):
    c[i], m[i] = map(int, lines[i].split())

for i in range(100):
    from_bucket = i % 3
    to_bucket = (i+1) % 3

    if (c[to_bucket] - m[to_bucket]) > m[from_bucket]:
        m[to_bucket] += m[from_bucket]
        m[from_bucket] = 0
    else:
        m[from_bucket] -= (c[to_bucket] - m[to_bucket])
        m[to_bucket] += (c[to_bucket] - m[to_bucket])


with open("mixmilk.out", "w") as file_out:
    for amount in m:
        file_out.write(str(amount) + "\n")