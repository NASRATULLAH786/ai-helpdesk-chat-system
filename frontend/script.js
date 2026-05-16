async function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value;

    if (!message) return;

    const chatBox = document.getElementById("chatBox");

    chatBox.innerHTML += `
        <div class="message user">
            <strong>You:</strong> ${message}
        </div>
    `;

    const response = await fetch(
        "http://127.0.0.1:8081/chat",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        }
    );

    const data = await response.json();

    chatBox.innerHTML += `
        <div class="message bot">
            <strong>AI Support:</strong> ${data.reply}
        </div>
    `;

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}


async function loadHistory() {
    const response = await fetch("http://127.0.0.1:8081/history");
    const data = await response.json();

    const chatBox = document.getElementById("chatBox");
    chatBox.innerHTML = "";

    data.forEach(chat => {
        chatBox.innerHTML += `
            <div class="message user">
                <strong>You:</strong> ${chat.user_message}
            </div>

            <div class="message bot">
                <strong>AI Support:</strong> ${chat.bot_reply}
            </div>
        `;
    });

    chatBox.scrollTop = chatBox.scrollHeight;
}


window.onload = loadHistory;