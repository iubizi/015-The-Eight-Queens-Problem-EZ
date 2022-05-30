import time

start = time.time()

seq = [ [a, b, c, d, e, f, g, h]
        for a in range(1, 9)
        for b in range(1, 9)
        for c in range(1, 9)
        for d in range(1, 9)
        for e in range(1, 9)
        for f in range(1, 9)
        for g in range(1, 9)
        for h in range(1, 9)
        # Only one queen per row & per column
        if all( [a!=b, a!=c, a!=d, a!=e, a!=f, a!=g, a!=h,
                 b!=c, b!=d, b!=e, b!=f, b!=g, b!=h,
                 c!=d, c!=e, c!=f, c!=g, c!=h,
                 d!=e, d!=f, d!=g, d!=h,
                 e!=f, e!=g, e!=h,
                 f!=g, f!=h,
                 g!=h] ) ]

end = time.time()

print('number of results =', len(seq))
print('time used =', round(end-start, 2), 's')

# number of results = 40320
# Include all symmetrical results

# time used = 8.3 s
# better CPU, faster speed (single process)
