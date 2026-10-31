import re, pathlib
here = pathlib.Path(__file__).parent
def path(n): return re.search(r' d="([^"]*)"', (here/'icons'/f'{n}.svg').read_text()).group(1)

# ======= عدّل هنا =======
HANDLE = "@Maqadeena"
HOURS  = "نستقبلكم يومياً من الساعة ٩ صباحاً حتى ١٢ منتصف الليل"
GREEN  = "#245731"
# ========================

html = f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<title>Magadhina Story</title>
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@500;700;800&display=swap" rel="stylesheet">
<style>
:root{{--g:{GREEN};--g2:#2F7F6F;--bg:#F6F6F4}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:var(--bg);font-family:'Tajawal',sans-serif;position:relative;overflow:hidden}}
.logo{{position:absolute;top:110px;right:70px;width:300px}}
.content{{position:absolute;top:470px;left:70px;right:70px;bottom:560px}}
.foot{{position:absolute;left:0;right:0;bottom:170px;text-align:center}}
.icons{{display:flex;justify-content:center;gap:44px;margin-bottom:40px}}
.ic{{width:112px;height:112px;border-radius:30px;background:var(--g);display:grid;place-items:center;box-shadow:0 10px 24px rgba(36,87,49,.25)}}
.ic svg{{width:60px;height:60px;fill:#fff}}
.handle{{display:inline-block;font-size:62px;font-weight:800;color:var(--g);direction:ltr;font-family:'Tajawal',sans-serif;letter-spacing:1px}}
.hours{{margin:34px auto 0;display:inline-block;font-size:34px;font-weight:700;color:#fff;background:var(--g2);padding:16px 40px;border-radius:999px}}
</style></head><body>
<img class="logo" src="logo.webp" alt="مقاضينا">
<div class="content"></div>
<div class="foot">
  <div class="icons">
    <div class="ic"><svg viewBox="0 0 24 24"><path d="{path('snapchat')}"/></svg></div>
    <div class="ic"><svg viewBox="0 0 24 24"><path d="{path('tiktok')}"/></svg></div>
    <div class="ic"><svg viewBox="0 0 24 24"><path d="{path('instagram')}"/></svg></div>
  </div>
  <div class="handle">{HANDLE}</div><br>
  <div class="hours">{HOURS}</div>
</div>
</body></html>"""
(here/'story.html').write_text(html, encoding='utf-8')
