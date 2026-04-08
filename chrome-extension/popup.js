chrome.storage.sync.get("apiBase", ({ apiBase }) => {
  document.getElementById("apiUrl").value = apiBase || "http://localhost:8001";
});

document.getElementById("save").addEventListener("click", () => {
  const apiBase = document.getElementById("apiUrl").value.trim().replace(/\/$/, "");
  chrome.runtime.sendMessage({ type: "SET_API_BASE", apiBase });
  chrome.storage.sync.set({ apiBase });
  const s = document.getElementById("status");
  s.style.display = "block";
  setTimeout(() => s.style.display = "none", 2000);
});
