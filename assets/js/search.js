/* Fuse.js 기반 연관 검색 — title/daily_title/keywords 가중 검색 + 점수 정렬.
   home / archive / book 모든 페이지에서 동일하게 사용.

   사용법:
     <script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js" defer></script>
     <script src="/ai-tech-digest/assets/js/search.js" defer></script>
     <script>
       window.initFuseSearch({
         searchJsonUrl: '/ai-tech-digest/search.json',
         inputId: 'search-input',
         resultsId: 'search-results',
       });
     </script>
*/
(function () {
  function escapeHtml(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }

  function renderResults(resultsEl, matches) {
    if (!matches.length) {
      resultsEl.innerHTML = '<li style="padding:0.55rem 0.85rem;color:var(--ink-muted,#666);font-size:0.85rem;">결과 없음</li>';
      return;
    }
    resultsEl.innerHTML = matches.map(function (m) {
      var p = m.item;
      var title = p.title || p.daily_title || '(제목 없음)';
      return '<li><a href="' + escapeHtml(p.url) + '">' +
        '<span class="sr-date">' + escapeHtml(p.date || '') + '</span>' +
        '<span>' + escapeHtml(title) + '</span>' +
        '</a></li>';
    }).join('');
  }

  function initFuseSearch(opts) {
    var input = document.getElementById(opts.inputId);
    var results = document.getElementById(opts.resultsId);
    if (!input || !results) return;

    var fuse = null;
    var pendingQuery = null;

    function runSearch() {
      var q = (input.value || '').trim();
      if (!q) { results.innerHTML = ''; return; }
      if (!fuse) { pendingQuery = q; return; }
      var matches = fuse.search(q, { limit: 12 });
      renderResults(results, matches);
    }

    input.addEventListener('input', runSearch);

    fetch(opts.searchJsonUrl)
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (posts) {
        if (typeof Fuse === 'undefined') {
          console.error('Fuse.js 미로드 — CDN 차단되었거나 스크립트 순서 확인 필요');
          return;
        }
        fuse = new Fuse(posts, {
          keys: [
            { name: 'title',        weight: 0.55 },  // 한국어 헤드라인 — 검색 주 신호
            { name: 'daily_title',  weight: 0.20 },  // 원문 영어 제목 (arxiv/github)
            { name: 'keywords',     weight: 0.25 },  // ai_keywords / sub_tags
          ],
          threshold: 0.4,         // 0.0=exact, 1.0=anything; 0.4 = 적당히 관대
          distance: 100,
          ignoreLocation: true,   // 단어 위치 무관 (어디 등장하든 동일 가중)
          includeScore: true,
          minMatchCharLength: 1,  // 한국어 1글자도 의미 있음 ('llm', '책')
          findAllMatches: true,
          shouldSort: true,
        });
        if (pendingQuery !== null) runSearch();
      })
      .catch(function (e) {
        console.error('search.json 로드 실패', e);
      });
  }

  window.initFuseSearch = initFuseSearch;
})();
