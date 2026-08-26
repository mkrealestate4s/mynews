// 카드 HTML 디렉터리를 정확한 뷰포트로 캡처한다 (크롭 보정 불필요)
//   node shot_cards.js <src-dir> <out-dir> <width> <height>
// 예) node shot_cards.js insta-reels pngr 1080 1920
//     node shot_cards.js insta-car   pngc 1080 1350
// 세로 프레임용 자동 확대(make_cards.fit_script) 배율을 함께 찍어 준다 —
// over v/h 가 0 이 아니면 잘린 것이므로 배율 상한을 낮춰야 한다.
const { chromium } = require('playwright-core');
const fs = require('fs'), path = require('path');
(async () => {
  const [src, out, W, H] = [process.argv[2], process.argv[3], +process.argv[4], +process.argv[5]];
  const only = process.argv[6] || '';   // 선택: 파일명 접두어만 캡처 (하루치만 다시 뽑을 때)
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  for (const f of fs.readdirSync(src).filter(x => x.endsWith('.html') && x.startsWith(only)).sort()) {
    await p.goto('file://' + path.resolve(src, f), { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(400);
    const fit = await p.evaluate(() => {
      const m = document.querySelector('.mid');
      return m ? { z: m.dataset.fit, v: m.scrollHeight - m.clientHeight, h: m.scrollWidth - m.clientWidth } : null;
    });
    const png = f.replace(/\.html$/, '.png');
    await p.screenshot({ path: path.join(out, png) });
    console.log(png.padEnd(24), fit ? `zoom=${fit.z} over v${fit.v} h${fit.h}` : '(no .mid)');
  }
  if (errs.length) console.log('JS errors:', errs);
  await b.close();
})();
