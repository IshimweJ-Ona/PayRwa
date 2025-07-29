document.getElementById("registerForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const currency = document.getElementById("currency").value;

  try {
    const res = await fetch("/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password, currency })
    });
    const result = await res.json();
    document.getElementById("regResponse").innerText = result.success ? "Registration successful!" : (result.error || "Registration failed.");
    if (result.success) window.location.href = "/";
  } catch (err) {
    document.getElementById("regResponse").innerText = "Network error during registration.";
    console.error(err);
  }
});