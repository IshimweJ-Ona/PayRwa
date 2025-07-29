document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch("/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });
    const result = await res.json();
    document.getElementById("loginMessage").innerText = result.success ? "Login successful!" : (result.error || "Login failed.");
    if (result.success) window.location.href = "/";
  } catch (err) {
    document.getElementById("loginMessage").innerText = "Network error during login.";
    console.error(err);
  }
});