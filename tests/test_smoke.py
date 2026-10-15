import subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class SmokeTests(unittest.TestCase):
 def test_projects(self):
  for name in ['01-kbeauty-product','02-ai-feedback-tool','03-reliability-platform']:
   with self.subTest(name=name):
    p=subprocess.run([sys.executable,str(ROOT/'projects'/name/'app.py')],capture_output=True,text=True)
    self.assertEqual(p.returncode,0,p.stderr)
    self.assertTrue(p.stdout.strip())
if __name__=='__main__':unittest.main()
