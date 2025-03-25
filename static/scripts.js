document.addEventListener("DOMContentLoaded", function () {
  const blockchainData = document.getElementById("blockchain-data");
  const viewBlockchainBtn = document.getElementById("view-blockchain");
  const mineBlockBtn = document.getElementById("mine-block");
  const submitTransactionBtn = document.getElementById("submit-transaction");

  async function fetchBlockchain() {
    try {
      blockchainData.innerHTML = "<p>Loading blockchain data...</p>";
      const response = await fetch("/get_chain");

      if (!response.ok) throw new Error("Failed to fetch blockchain data");

      const data = await response.json();
      blockchainData.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    } catch (error) {
      blockchainData.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    }
  }

  async function mineBlock() {
    try {
      mineBlockBtn.disabled = true;
      const response = await fetch("/mine_block");

      if (!response.ok) throw new Error("Error mining block");

      alert("Block Mined!");
      fetchBlockchain();
    } catch (error) {
      alert("Error: " + error.message);
    } finally {
      mineBlockBtn.disabled = false;
    }
  }

  async function submitTransaction() {
    try {
      const sender = document.getElementById("sender").value.trim();
      const receiver = document.getElementById("receiver").value.trim();
      const amount = document.getElementById("amount").value.trim();

      if (!sender || !receiver || !amount) {
        alert("Please fill all fields!");
        return;
      }

      submitTransactionBtn.disabled = true;
      const response = await fetch("/add_transaction", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sender, receiver, amount }),
      });

      if (!response.ok) throw new Error("Transaction failed!");

      alert("Transaction Added!");
      fetchBlockchain();
    } catch (error) {
      alert("Error: " + error.message);
    } finally {
      submitTransactionBtn.disabled = false;
    }
  }

  async function fetchRealBlockchainData() {
    try {
      blockchainData.innerHTML += "<p>Loading real blockchain data...</p>";
      const response = await fetch("https://api.blockcypher.com/v1/btc/main");

      if (!response.ok) throw new Error("Failed to fetch real blockchain data");

      const data = await response.json();
      blockchainData.innerHTML += `<h3>Real Blockchain Info:</h3>
                                   <pre>${JSON.stringify(data, null, 2)}</pre>`;
    } catch (error) {
      blockchainData.innerHTML += `<p style="color: red;">Error: ${error.message}</p>`;
    }
  }

  // Event Listeners
  viewBlockchainBtn.addEventListener("click", fetchBlockchain);
  mineBlockBtn.addEventListener("click", mineBlock);
  submitTransactionBtn.addEventListener("click", submitTransaction);

  // Fetch initial data
  fetchBlockchain();
  fetchRealBlockchainData();
});
