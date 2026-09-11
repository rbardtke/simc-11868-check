import json, subprocess, sys
simc, label = sys.argv[1], sys.argv[2]
rows = []
for seed in range(1, 17):
    subprocess.run([simc, 'repro.simc', f'seed={seed}', 'json2=out.json', 'report_details=0'], capture_output=True)
    g = json.load(open('out.json'))['sim']['players'][0]['gear']
    rows.append((seed, g['shoulders']['ilevel'], g['finger1']['ilevel']))
wrong = [r for r in rows if r[1] != 256 or r[2] != 262]
print(f'{label}: ' + ' '.join(f'{s}:{a}/{b}' for s, a, b in rows))
print(f'{label}: {len(wrong)} of 16 seeds wrong (expected shoulders 256, finger1 262)')
