document.getElementById("generate-button").addEventListener("click", function () {
    const mailBody = document.getElementById("message-box").value.trim();
  
    if (!mailBody) {
      alert("Lütfen bir mail içeriği girin.");
      return;
    }
  
    // Backend'e gönder
    fetch("http://localhost:8000/generate-reply", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ mail_body: mailBody }),
    })
      .then((res) => res.json())
      .then((data) => {
        // Gelen yanıtı mail formatında göstermek
        console.log("Backend'den gelen cevap: ", data);
        const formattedReply = formatReply(data.reply);
        document.getElementById("output").innerHTML = formattedReply;
      })
      .catch((err) => {
        console.error("AI'dan yanıt alınamadı:", err);
      });
  });
  
  // Backend'den gelen yanıtı mail formatına uygun hale getirmek
  function formatReply(reply) {
    return `
      <div>
        <p><strong>Dear User,</strong></p>
        <p>${reply}</p>
        <p>Best regards,<br>Your Assistant</p>
      </div>
    `;
  }
  