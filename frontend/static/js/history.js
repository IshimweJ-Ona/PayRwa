window.addEventListener("DOMContentLoaded", async () => {
  try {
    const res = await fetch("/history", { headers: { "Accept": "application/json" } });
    const data = await res.json();

    if (!Array.isArray(data.transactions) || data.transactions.length === 0) {
      document.getElementById("historyTable").innerHTML += '<tr><td colspan="4">No transactions found.</td></tr>';
      return;
    }

    const tbody = document.createElement("tbody");
    data.transactions.forEach(tx => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${tx.type || ""}</td>
        <td>${tx.amount}</td>
        <td>${tx.paid_to}</td>
        <td>${tx.date}</td>
      `;
      tbody.appendChild(row);
    });
    document.getElementById("historyTable").appendChild(tbody);
  } catch (err) {
    document.getElementById("historyTable").innerHTML += '<tr><td colspan="4">Failed to load history.</td></tr>';
    console.error("Error loading transaction history:", err);
  }
});