const PLATFORM = detectPlatform();

function detectPlatform() {
  const host = location.hostname;
  if (host.includes("instagram.com")) return "instagram";
  if (host.includes("reddit.com")) return "reddit";
  if (host.includes("facebook.com")) return "facebook";
  if (host.includes("twitter.com") || host.includes("x.com")) return "twitter";
  return null;
}

// ── Platform-specific post selectors ──────────────────────────────────────────
const SELECTORS = {
  instagram: {
    post: "article",
    text: ["h1", "._a9zs", "._aacl", "span[class*='x193iq5w']"],
    images: ["img[class*='x5yr21d']", "img[srcset]"]
  },
  reddit: {
    post: "shreddit-post, [data-testid='post-container'], .Post",
    text: ["[data-testid='post-content']", "h1", ".RichTextJSON-root", "[slot='text-body']"],
    images: ["img[src*='redd.it']", "img[src*='reddit']", "img[src*='preview']"]
  },
  facebook: {
    post: "[data-pagelet*='FeedUnit'], [role='article']",
    text: ["[data-ad-comet-preview='message']", "[data-testid='post_message']", "div[dir='auto']"],
    images: ["img[referrerpolicy='origin-when-cross-origin']", "img[class*='x1ey2m1c']"]
  },
  twitter: {
    post: "article[data-testid='tweet']",
    text: ["[data-testid='tweetText']"],
    images: ["img[src*='pbs.twimg.com/media']"]
  }
};

// ── Extract text from a post element ──────────────────────────────────────────
function extractText(postEl) {
  const sel = SELECTORS[PLATFORM];
  if (!sel) return "";
  for (const s of sel.text) {
    const el = postEl.querySelector(s);
    if (el && el.innerText.trim().length > 5) return el.innerText.trim();
  }
  return postEl.innerText.slice(0, 600).trim();
}

// ── Extract image URLs from a post element ────────────────────────────────────
function extractImages(postEl) {
  const sel = SELECTORS[PLATFORM];
  if (!sel) return [];
  const urls = new Set();
  for (const s of sel.images) {
    postEl.querySelectorAll(s).forEach(img => {
      const src = img.src || img.dataset.src;
      if (src && src.startsWith("http") && !src.includes("profile") && !src.includes("avatar")) {
        urls.add(src);
      }
    });
  }
  return [...urls].slice(0, 5);
}

// ── Inject Analyze button into a post ─────────────────────────────────────────
function injectButton(postEl) {
  if (postEl.querySelector(".suart-btn")) return;

  const btn = document.createElement("button");
  btn.className = "suart-btn";
  btn.innerHTML = `<span class="suart-logo">S</span> Analyze`;
  btn.title = "Analyze with SUART";

  btn.addEventListener("click", (e) => {
    e.stopPropagation();
    e.preventDefault();
    analyzePost(postEl, btn);
  });

  // Append to post — try to find action bar, else append to post itself
  const actionBar = postEl.querySelector(
    "section, [role='group'], ._ae2s, [data-testid='reply'], .action-buttons"
  );
  (actionBar || postEl).appendChild(btn);
}

// ── Run analysis ───────────────────────────────────────────────────────────────
async function analyzePost(postEl, btn) {
  const text = extractText(postEl);
  const image_urls = extractImages(postEl);

  if (!text && image_urls.length === 0) {
    showSidebar({ error: "Could not extract content from this post." });
    return;
  }

  btn.disabled = true;
  btn.innerHTML = `<span class="suart-spinner"></span> Analyzing...`;

  chrome.runtime.sendMessage(
    {
      type: "ANALYZE_CONTENT",
      payload: {
        text: text || "No text content",
        image_urls,
        platform: PLATFORM,
        post_url: location.href
      }
    },
    (response) => {
      btn.disabled = false;
      btn.innerHTML = `<span class="suart-logo">S</span> Analyze`;

      if (response?.success) {
        showSidebar(response.data);
      } else {
        showSidebar({ error: response?.error || "Analysis failed. Is the backend running?" });
      }
    }
  );
}

// ── Sidebar ────────────────────────────────────────────────────────────────────
function showSidebar(data) {
  let sidebar = document.getElementById("suart-sidebar");
  if (!sidebar) {
    sidebar = document.createElement("div");
    sidebar.id = "suart-sidebar";
    document.body.appendChild(sidebar);
  }

  if (data.error) {
    sidebar.innerHTML = `
      <div class="suart-sidebar-header">
        <span class="suart-title">SUART Analysis</span>
        <button class="suart-close" onclick="document.getElementById('suart-sidebar').classList.remove('open')">✕</button>
      </div>
      <div class="suart-error">${data.error}</div>`;
    sidebar.classList.add("open");
    return;
  }

  const risk = data.combined_risk || data.risk_assessment;
  const score = risk?.score ?? 0;
  const level = risk?.level ?? "UNKNOWN";
  const ca = data.content_analysis || {};
  const sentiment = ca.sentiment?.label ?? "N/A";
  const toxic = ca.toxicity?.is_toxic ? `Yes (${(ca.toxicity.confidence * 100).toFixed(0)}%)` : "No";
  const hate = ca.hate_speech?.is_hate_speech ? `Yes (${(ca.hate_speech.confidence * 100).toFixed(0)}%)` : "No";
  const intent = ca.intent?.intent ?? "unknown";
  const categories = ca.content_categories?.detected_categories ?? [];
  const factors = data.risk_assessment?.factors ?? [];
  const reasons = data.risk_assessment?.reasons ?? [];
  const images = data.image_analysis ?? [];

  const color = score >= 70 ? "#ef4444" : score >= 50 ? "#f97316" : score >= 30 ? "#eab308" : score >= 15 ? "#3b82f6" : "#22c55e";

  sidebar.innerHTML = `
    <div class="suart-sidebar-header">
      <span class="suart-title">SUART Analysis</span>
      <button class="suart-close" onclick="document.getElementById('suart-sidebar').classList.remove('open')">✕</button>
    </div>

    <div class="suart-score-ring" style="--ring-color:${color}">
      <svg viewBox="0 0 80 80">
        <circle cx="40" cy="40" r="34" fill="none" stroke="#2a2a2a" stroke-width="8"/>
        <circle cx="40" cy="40" r="34" fill="none" stroke="${color}" stroke-width="8"
          stroke-dasharray="${2 * Math.PI * 34}" stroke-dashoffset="${2 * Math.PI * 34 * (1 - score / 100)}"
          stroke-linecap="round" transform="rotate(-90 40 40)"/>
      </svg>
      <div class="suart-score-text">
        <span class="suart-score-num">${score}</span>
        <span class="suart-score-label" style="color:${color}">${level}</span>
      </div>
    </div>

    <div class="suart-platform-badge">${(data.platform || PLATFORM).toUpperCase()}</div>

    <div class="suart-section">
      <div class="suart-row"><span>Sentiment</span><span>${sentiment}</span></div>
      <div class="suart-row"><span>Toxic</span><span style="color:${ca.toxicity?.is_toxic ? '#ef4444' : '#22c55e'}">${toxic}</span></div>
      <div class="suart-row"><span>Hate Speech</span><span style="color:${ca.hate_speech?.is_hate_speech ? '#ef4444' : '#22c55e'}">${hate}</span></div>
      <div class="suart-row"><span>Intent</span><span>${intent}</span></div>
    </div>

    ${categories.length ? `
    <div class="suart-section">
      <div class="suart-label">Categories</div>
      <div class="suart-tags">${categories.map(c => `<span class="suart-tag">${c.replace(/_/g, " ")}</span>`).join("")}</div>
    </div>` : ""}

    ${factors.length ? `
    <div class="suart-section">
      <div class="suart-label">Risk Factors</div>
      <div class="suart-tags">${factors.map(f => `<span class="suart-tag danger">${f.replace(/_/g, " ")}</span>`).join("")}</div>
    </div>` : ""}

    ${reasons.length ? `
    <div class="suart-section">
      <div class="suart-label">Notes</div>
      ${reasons.map(r => `<div class="suart-note">• ${r}</div>`).join("")}
    </div>` : ""}

    ${images.length ? `
    <div class="suart-section">
      <div class="suart-label">Images Analyzed (${images.length})</div>
      ${images.map(img => `
        <div class="suart-img-row">
          <span>${img.nsfw?.is_nsfw ? "🔞 NSFW" : img.violence?.is_violent ? "⚠️ Violent" : "✅ Safe"}</span>
          <span>Risk: ${img.image_risk_score ?? 0}/100</span>
        </div>`).join("")}
    </div>` : ""}

    <div class="suart-footer">Powered by SUART AI</div>`;

  sidebar.classList.add("open");
}

// ── Observe DOM for new posts (infinite scroll) ────────────────────────────────
function observePosts() {
  const sel = SELECTORS[PLATFORM]?.post;
  if (!sel) return;

  const inject = () => {
    document.querySelectorAll(sel).forEach(post => {
      if (!post.querySelector(".suart-btn")) injectButton(post);
    });
  };

  inject();
  new MutationObserver(inject).observe(document.body, { childList: true, subtree: true });
}

if (PLATFORM) observePosts();
