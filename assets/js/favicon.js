/* OIIA 고양이 파비콘 — sprite sheet 165 프레임 cycling.
   Chrome/Safari 는 GIF/SVG 애니메이션 favicon 을 native 지원 안 함 → canvas 로 매 프레임 redraw.

   동작 정책 (로딩 상태와 무관):
   - 1 cycle 회전 (~5.5s @ 30fps × 165 frames)
   - 5s 정지 (정적 favicon 표시)
   - 무한 반복

   레이아웃이 inline 으로 주입:
     <script>
       window.OIIA_CAT_URL    = '{{ "/assets/favicon/oiia-cat.png"    | relative_url }}';
       window.OIIA_SPRITE_URL = '{{ "/assets/favicon/oiia-sprite.png" | relative_url }}';
     </script>
*/
(function () {
  const FRAME_COUNT   = 165;
  const COLS          = 15;
  const FRAME_SIZE    = 64;
  const ANIMATION_FPS = 30;
  const FRAME_MS      = 1000 / ANIMATION_FPS;
  const PAUSE_MS      = 5000;

  const STATIC_URL = window.OIIA_CAT_URL    || '/assets/favicon/oiia-cat.png';
  const SPRITE_URL = window.OIIA_SPRITE_URL || '/assets/favicon/oiia-sprite.png';

  function getOrCreateLink() {
    let link = document.querySelector("link[rel~='icon']");
    if (!link) {
      link = document.createElement('link');
      link.rel = 'icon';
      document.head.appendChild(link);
    }
    return link;
  }

  const link = getOrCreateLink();
  if (!link.href) link.href = STATIC_URL;

  const canvas = document.createElement('canvas');
  canvas.width = canvas.height = FRAME_SIZE;
  const ctx = canvas.getContext('2d');

  let sprite = null;
  const spritePromise = new Promise(function (resolve) {
    const img = new Image();
    img.onload = function () { resolve(img); };
    img.onerror = function () { resolve(null); };
    img.src = SPRITE_URL;
  });
  spritePromise.then(function (s) { sprite = s; });

  function drawFrame(idx) {
    if (!sprite) return;
    const col = idx % COLS;
    const row = Math.floor(idx / COLS);
    ctx.clearRect(0, 0, FRAME_SIZE, FRAME_SIZE);
    ctx.drawImage(
      sprite,
      col * FRAME_SIZE, row * FRAME_SIZE, FRAME_SIZE, FRAME_SIZE,
      0, 0, FRAME_SIZE, FRAME_SIZE
    );
    link.href = canvas.toDataURL('image/png');
  }

  // 상태 머신: 'animating' (회전 중) ↔ 'paused' (정지 대기)
  let state = 'paused';
  let frameIdx = 0;
  let lastFrameTime = 0;
  let pauseUntil = 0;

  function loop(now) {
    if (state === 'paused') {
      if (now >= pauseUntil) {
        state = 'animating';
        frameIdx = 0;
        lastFrameTime = now;
      }
      requestAnimationFrame(loop);
      return;
    }
    // animating
    if (now - lastFrameTime >= FRAME_MS) {
      drawFrame(frameIdx);
      frameIdx++;
      lastFrameTime = now;
      if (frameIdx >= FRAME_COUNT) {
        // 한 사이클 끝 → 정적 favicon 으로 복귀 후 5s 대기
        link.href = STATIC_URL;
        state = 'paused';
        pauseUntil = now + PAUSE_MS;
      }
    }
    requestAnimationFrame(loop);
  }

  // 스프라이트 도착하면 루프 시작 — 첫 사이클은 즉시 시작
  spritePromise.then(function (s) {
    if (!s) return;  // 로드 실패 시 정적 favicon 만 유지
    state = 'animating';
    frameIdx = 0;
    lastFrameTime = 0;
    requestAnimationFrame(loop);
  });
})();
