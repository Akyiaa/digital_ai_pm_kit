from pathlib import Path
import csv
p=Path(__file__).parent/'data/feedback.csv'
with p.open(newline='') as f: rows=list(csv.DictReader(f))
def classify(t):
 t=t.lower()
 if any(x in t for x in ['payment','checkout','refund']):return 'payment'
 if any(x in t for x in ['crash','freez','error']):return 'bug'
 if any(x in t for x in ['add','wishlists','filters']):return 'feature'
 return 'positive'
correct=sum(classify(r['text'])==r['expected'] for r in rows)
print(f'Offline rules-based baseline: {correct}/{len(rows)} correct = {correct/len(rows):.1%}')
print('NOT an LLM; evaluate a local or optional paid LLM separately on the same cases.')
