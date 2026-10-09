"""Package only runtime skill files, never course data or local credentials."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import hashlib
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'dist';out.mkdir(exist_ok=True)
archive=out/'omni-learning-assistant-skill-v0.2.0.zip'
with ZipFile(archive,'w',ZIP_DEFLATED) as z:
 for p in sorted((ROOT/'skills/omni-learning-assistant').rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.name!='.DS_Store':
   z.write(p,Path('omni-learning-assistant')/p.relative_to(ROOT/'skills/omni-learning-assistant'))
(out/'SHA256SUMS').write_text(hashlib.sha256(archive.read_bytes()).hexdigest()+'  '+archive.name+'\n')
print(archive.name,archive.stat().st_size)
