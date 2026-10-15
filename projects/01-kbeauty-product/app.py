from pathlib import Path
import csv
p=Path(__file__).parent/'data/events.csv'
with p.open(newline='') as f: rows=list(csv.DictReader(f))
counts={event:len({r['user_id'] for r in rows if r['event']==event}) for event in ['view','save','cart','purchase']}
print('Synthetic K-beauty funnel:',counts)
print('Purchase / view:',round(counts['purchase']/counts['view']*100,1),'%')
print('Illustration only: not real product performance.')
