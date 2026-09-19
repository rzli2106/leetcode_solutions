with open("shell.in", "r") as file:
    lines = file.read().splitlines()

n = int(lines[0])

swaps = []
for line in lines[1:]:
    if line.strip():
        a, b, g = map(int, line.split())
        swaps.append((a,b,g))

ans = [0] * 3

for starting_shell in [1, 2, 3]:
    pebble_location = starting_shell
    score = 0

    for a, b, g in swaps:
        if pebble_location == a:
            pebble_location = b
        elif pebble_location == b:
            pebble_location = a

        if pebble_location == g:
            score += 1
    ans[starting_shell - 1] = score
    



with open("shell.out", "w") as file_out:
    file_out.write(str(max(ans)) + "\n")