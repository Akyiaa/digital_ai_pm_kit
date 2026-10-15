from pathlib import Path
import csv,collections
p=Path(__file__).parent/'data/incidents.csv'
with p.open(newline='') as f: rows=list(csv.DictReader(f))
by=collections.Counter(r['service'] for r in rows)
mttr=sum(int(r['minutes_to_resolve']) for r in rows)/len(rows)
print('Synthetic incidents by service:',dict(by))
print('Mean time to resolution (minutes):',round(mttr,1))
print('Reopened tickets:',sum(int(r['reopened']) for r in rows))
