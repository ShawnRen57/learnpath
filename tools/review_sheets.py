"""Create page contact sheets for human/model visual review, not an auto-review."""
from pathlib import Path
from PIL import Image,ImageDraw
import sys
key=sys.argv[1]
root=Path(__file__).resolve().parents[1]
out=root/'docs/review';out.mkdir(exist_ok=True)
for r in (root/'examples').iterdir():
 pages=list(sorted((r/'previews').glob(key+'-*.png')))
 if not pages:continue
 canvas=Image.new('RGB',(len(pages)*600,885),'#dde6e8')
 for n,p in enumerate(pages):
  im=Image.open(p);im.thumbnail((590,850));canvas.paste(im,(n*600+5,30));ImageDraw.Draw(canvas).text((n*600+10,8),f'{r.name} / {p.stem}',fill='black')
 canvas.save(out/(r.name+'-'+key+'.jpg'),quality=92)
