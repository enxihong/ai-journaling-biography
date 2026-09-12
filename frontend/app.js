let history = [];

async function sendChat() {
  const input = document.getElementById("chat-input");
  const text = input.value.trim();
  if (!text) return;
  input.value = "";

  history.push({ role: "user", content: text });
  renderChat();

  const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ history }),
  });
  const data = await res.json();
  history.push({ role: "assistant", content: data.reply });
  renderChat();
}

function renderChat() {
  const log = document.getElementById("chat-log");
  log.innerHTML = history
    .map(
      (m) =>
        `<div class="msg-${m.role}"><b>${m.role}:</b> ${m.content}</div>`
    )
    .join("");
  log.scrollTop = log.scrollHeight;
}

async function saveJournal() {
  if (history.length === 0) return alert("Talk a bit first.");
  const res = await fetch("/api/journal", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ history }),
  });
  const data = await res.json();
  alert(`Saved: "${data.title}"`);
  history = [];
  renderChat();
  loadJournal();
}

async function loadJournal() {
  const res = await fetch("/api/journal");
  const entries = await res.json();
  const list = document.getElementById("journal-list");
  list.innerHTML = entries
    .map(
      (e) =>
        `<div class="entry"><b>${e.title}</b> (${e.created_at})<p>${e.content}</p></div>`
    )
    .join("");
}

async function findPatterns() {
  const res = await fetch("/api/patterns", { method: "POST" });
  const data = await res.json();
  const out = document.getElementById("patterns-output");
  if (data.detail) {
    out.innerHTML = `<p>${data.detail}</p>`;
    return;
  }
  out.innerHTML =
    "<h3>Patterns</h3><ul>" +
    data.patterns.map((p) => `<li>${p.pattern}</li>`).join("") +
    "</ul>";
}

async function createPerson() {
  const name = document.getElementById("person-name").value.trim();
  const rel = document.getElementById("person-rel").value.trim();
  if (!name) return;
  await fetch("/api/persons", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, relationship: rel || null }),
  });
  document.getElementById("person-name").value = "";
  document.getElementById("person-rel").value = "";
  loadPersons();
}

async function loadPersons() {
  const res = await fetch("/api/persons");
  const persons = await res.json();
  const list = document.getElementById("persons-list");
  list.innerHTML = persons
    .map(
      (p) =>
        `<div class="person"><b>${p.name}</b> (${p.relationship || "unspecified"}) — ${p.memories.length} memories</div>`
    )
    .join("");
}

async function generateBiography() {
  const out = document.getElementById("biography-output");
  out.textContent = "Generating...";
  const res = await fetch("/api/biography", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({}),
  });
  const data = await res.json();
  out.textContent = data.chapter || data.detail || "No result";
}

loadJournal();
loadPersons();
