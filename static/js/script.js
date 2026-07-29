document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
    const chatMessages = document.getElementById("chat-messages");
    const typingIndicator = document.getElementById("typing-indicator");
    const themeToggle = document.getElementById("theme-toggle");
    const clearBtn = document.getElementById("clear-btn");
    const suggestionChips = document.querySelectorAll(".suggestion-chip");

    // Load history on startup
    loadHistory();

    // Theme Toggle
    const updateThemeButton = () => {
        const html = document.documentElement;
        const currentTheme = html.getAttribute("data-theme") || "dark";
        const icon = themeToggle.querySelector("i");
        icon.className = currentTheme === "dark"
            ? "fa-solid fa-moon"
            : "fa-solid fa-sun";
        themeToggle.title = currentTheme === "dark" ? "Switch to light theme" : "Switch to dark theme";
    };

    updateThemeButton();

    themeToggle.addEventListener("click", () => {
        const html = document.documentElement;
        const currentTheme = html.getAttribute("data-theme");
        const newTheme = currentTheme === "dark" ? "light" : "dark";
        html.setAttribute("data-theme", newTheme);
        updateThemeButton();
    });

    // Suggestion Chips Click -> Auto Send Message
    suggestionChips.forEach(chip => {
        chip.addEventListener("click", () => {
            const message = chip.textContent.trim();
            userInput.value = message;
            userInput.focus();
            sendUserMessage(message, { preserveInput: true });
        });
    });

    // Form Submit
    chatForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const message = userInput.value.trim();
        if (!message) return;
        sendUserMessage(message);
    });

    // Send Message Function
    async function sendUserMessage(message, options = {}) {
        const { preserveInput = false } = options;

        if (!preserveInput) {
            userInput.value = "";
        }

        appendMessage(message, "user");
        scrollToBottom();

        typingIndicator.style.display = "flex";
        scrollToBottom();

        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: message })
            });
            const data = await response.json();

            typingIndicator.style.display = "none";
            appendMessage(data.answer, "bot");
            scrollToBottom();
        } catch (error) {
            typingIndicator.style.display = "none";
            appendMessage("Sorry, something went wrong with the server connection.", "bot");
            scrollToBottom();
        }
    }

    // Clear History
    clearBtn.addEventListener("click", async () => {
        try {
            await fetch("/clear", { method: "POST" });
            chatMessages.innerHTML = `
                <div class="message bot-message">
                    <div class="message-avatar"><i class="fa-solid fa-robot"></i></div>
                    <div class="message-content">
                        <h3>Welcome 👋</h3>
                        <p>Chat history cleared. How can I help you today?</p>
                        <span class="message-time">Just now</span>
                    </div>
                </div>
            `;
        } catch (error) {
            console.error("Failed to clear history", error);
        }
    });

    // Append Message
    function appendMessage(text, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", `${sender}-message`);

        const avatarDiv = document.createElement("div");
        avatarDiv.classList.add("message-avatar");
        avatarDiv.innerHTML = sender === "bot" ? '<i class="fa-solid fa-robot"></i>' : '<i class="fa-solid fa-user"></i>';

        const contentDiv = document.createElement("div");
        contentDiv.classList.add("message-content");

        const p = document.createElement("p");
        p.textContent = text;

        const timeSpan = document.createElement("span");
        timeSpan.classList.add("message-time");
        timeSpan.textContent = getCurrentTime();

        contentDiv.appendChild(p);
        contentDiv.appendChild(timeSpan);

        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);

        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }

    // Load History
    async function loadHistory() {
        try {
            const response = await fetch("/history");
            const history = await response.json();
            
            if (Array.isArray(history) && history.length > 0) {
                // Keep welcome message or clear, here we preserve order
                history.forEach(item => {
                    if (item.question) appendMessage(item.question, "user");
                    if (item.answer) appendMessage(item.answer, "bot");
                });
                scrollToBottom();
            }
        } catch (error) {
            console.error("Failed to load history", error);
        }
    }

    function getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});