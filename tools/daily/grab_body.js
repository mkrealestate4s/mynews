// node grab_body.js <abs post html> <abs out txt>  — 복사 버튼 텍스트를 받아 발행본(작업용 꼬리 제외)을 쓴다
const { chromium } = require('playwright-core');
const fs = require('fs');
(async () => {
  const [src, out] = [process.argv[2], process.argv[3]];
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const p = await b.newPage();
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  await p.addInitScript(() => {
    window.__copied = [];
    const w = t => { window.__copied.push(t); return Promise.resolve(); };
    Object.defineProperty(navigator, 'clipboard', { value: { writeText: w }, configurable: true });
    document.execCommand = () => true;
  });
  await p.goto('file://' + src, { waitUntil: 'load' });
  await p.click('#copyBody');
  await p.waitForTimeout(300);
  let txt = await p.evaluate(() => window.__copied[window.__copied.length - 1] || '');
  if (!txt) { console.log('복사 텍스트 없음'); process.exit(1); }
  const cut = txt.indexOf('──── 아래는 작업용 안내');
  const pub = (cut >= 0 ? txt.slice(0, cut) : txt).trim() + '\n';
  fs.writeFileSync(out, pub);
  const slots = [...pub.matchAll(/\[이미지(\d+)/g)].map(m => +m[1]);
  console.log(`복사 ${txt.length} 자 → 발행본 ${pub.length} 자 · 슬롯 ${slots.join(',')} · 1~6 ${JSON.stringify(slots) === '[1,2,3,4,5,6]'} · 줄표 ${(pub.match(/—/g) || []).length} · 깃페이지 ${pub.includes('github.io')} · 참고자료 ${pub.includes('참고 자료')} · 태그줄 ${/^#\S/m.test(pub)} · JS에러 ${errs.length}`);
  await b.close();
})();
