// 모바일 390px 검증: 가로 오버플로·정사각 이미지·#insta 이미지 생성
const { chromium } = require('playwright-core');
(async () => {
  const url = 'http://localhost:8899/posts/' + process.argv[2] + '.html';
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 390, height: 844 } });
  const errs = [], bad = [];
  p.on('pageerror', e => errs.push(String(e)));
  p.on('response', r => { if (r.status() >= 400) bad.push(r.status() + ' ' + r.url()); });
  await p.goto(url, { waitUntil: 'networkidle' });
  const r = await p.evaluate(() => {
    const over = document.documentElement.scrollWidth - window.innerWidth;
    const nonSquare = [...document.querySelectorAll('img.card-art')].filter(i => i.naturalWidth && i.naturalWidth !== i.naturalHeight).map(i => i.src);
    const railOver = [...document.querySelectorAll('.rail')].filter(e => e.scrollWidth > e.clientWidth + 1).length;
    return { over, nonSquare, railOver, instaImgs: document.querySelectorAll('img.insta-art').length,
             cap: (document.getElementById('instacap') || {}).textContent?.length || 0 };
  });
  console.log(JSON.stringify(r));
  console.log('4xx/5xx:', bad.length ? bad : 'none', '| JS errors:', errs.length ? errs : 'none');
  await b.close();
})();
