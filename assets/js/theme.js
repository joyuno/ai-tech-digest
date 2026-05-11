/* 테마 토글 — joyuno.github.io 와 동일 origin / 동일 key 사용해 자동 sync.
   localStorage['theme']: 'light' | 'dark'  (기본 'light')

   <html data-theme="..."> 속성으로 CSS 변수 스왑.
   페인트 전 inline <script> 가 먼저 attr 을 세팅하면 깜빡임 없음 — 각 레이아웃 head 상단 inline 참고. */
(function () {
  const KEY = 'theme';

  function current() {
    // 이 사이트(ai-tech-digest) 의 기본값은 dark. joyuno.github.io 와 같은 origin 이라
    // localStorage['theme'] 가 있으면 자동 sync (사용자가 한쪽에서 light 로 바꾸면 양쪽 다 light).
    return document.documentElement.getAttribute('data-theme') || 'dark';
  }

  function apply(t) {
    document.documentElement.setAttribute('data-theme', t);
    try { localStorage.setItem(KEY, t); } catch (_) {}
    updateButtons(t);
  }

  function updateButtons(t) {
    const isDark = t === 'dark';
    document.querySelectorAll('[data-theme-toggle]').forEach(function (btn) {
      btn.setAttribute('aria-label', isDark ? '라이트 모드로 전환' : '다크 모드로 전환');
      const icon = btn.querySelector('.theme-icon');
      if (icon) icon.textContent = isDark ? '☀' : '☾';
    });
  }

  function init() {
    document.querySelectorAll('[data-theme-toggle]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        apply(current() === 'dark' ? 'light' : 'dark');
      });
    });
    updateButtons(current());
  }

  // 다른 탭 / 같은 origin 의 다른 페이지에서 테마 바꾸면 즉시 반영
  window.addEventListener('storage', function (e) {
    if (e.key === KEY && e.newValue && e.newValue !== current()) {
      document.documentElement.setAttribute('data-theme', e.newValue);
      updateButtons(e.newValue);
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
