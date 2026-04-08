const API_BASE = "http://localhost:8001";

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "ANALYZE_CONTENT") {
    fetch(`${API_BASE}/analyze/direct`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(message.payload)
    })
      .then(res => res.json())
      .then(data => sendResponse({ success: true, data }))
      .catch(err => sendResponse({ success: false, error: err.message }));

    return true; // keep channel open for async response
  }

  if (message.type === "GET_API_BASE") {
    chrome.storage.sync.get("apiBase", ({ apiBase }) => {
      sendResponse({ apiBase: apiBase || API_BASE });
    });
    return true;
  }

  if (message.type === "SET_API_BASE") {
    chrome.storage.sync.set({ apiBase: message.apiBase });
  }
});
