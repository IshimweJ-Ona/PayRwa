document.getElementById("paymentForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const payType = document.getElementById("payType").value;
  const target = document.getElementById("target").value;
  const amount = document.getElementById("amount").value;
  const currency = document.getElementById("currency").value;
  const userPhone = document.getElementById("userPhone").value;

  try {
    const res = await fetch("/pay", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ payType, target, amount, currency, userPhone })
    });
    const result = await res.json();
    document.getElementById("response").innerText = result.success ? "Payment successful!" : (result.error || "Payment failed.");
  } catch (err) {
    document.getElementById("response").innerText = "Network error during payment.";
    console.error(err);
  }
});