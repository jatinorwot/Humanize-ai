const chatMessages = document.getElementById('chatMessages');
        const userInput = document.getElementById('userInput');
        const sendButton = document.getElementById('sendButton');
        const fileInput = document.getElementById('fileInput');
        const typingIndicator = document.getElementById('typingIndicator');
        const onlineStatus = document.querySelector('.online-status');
        const selectedImagePreview = document.getElementById('selectedImagePreview');
        const previewImage = document.getElementById('previewImage');
        let imageData = null;

        function addMessage(content, isUser, isHTML = false) {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message');
            messageDiv.classList.add(isUser ? 'user-message' : 'bot-message');
            
            const contentDiv = document.createElement('div');
            contentDiv.classList.add('message-content');
            if (isHTML) {
                contentDiv.innerHTML = content;
            } else {
                contentDiv.textContent = content;
            }
            messageDiv.appendChild(contentDiv);
            
            const footerDiv = document.createElement('div');
            footerDiv.classList.add('message-footer');
            
            const timeSpan = document.createElement('span');
            timeSpan.classList.add('message-time');
            timeSpan.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            footerDiv.appendChild(timeSpan);

            if (isUser) {
                const statusSpan = document.createElement('span');
                statusSpan.classList.add('message-status');
                statusSpan.textContent = '✓';
                footerDiv.appendChild(statusSpan);

                setTimeout(() => {
                    statusSpan.classList.add('read');
                    statusSpan.textContent = '✓✓';
                }, 2000);
            }
            
            messageDiv.appendChild(footerDiv);
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function showTypingIndicator() {
            typingIndicator.style.display = 'block';
        }

        function hideTypingIndicator() {
            typingIndicator.style.display = 'none';
        }

        function sendMessage() {
    const message = userInput.value.trim();
    const errorMessage = document.getElementById('errorMessage');

    if ((message && imageData) || (message && !imageData)) {
        errorMessage.style.display = 'none'; // Hide error message if validation passes
        let messageContent = '';
        if (imageData) {
            messageContent += `<img src="${imageData}" style="max-width: 100%; border-radius: 10px;">`;
        }
        if (message) {
            messageContent += `<p>${message}</p>`;
        }
        addMessage(messageContent, true, true);
        userInput.value = '';
        showTypingIndicator();

        const payload = {
            user_input: message,
            image: imageData
        };

        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        })
        .then(response => response.json())
        .then(data => {
            setTimeout(() => {
                hideTypingIndicator();
                addMessage(data.response, false);
            }, 1000);
        })
        .catch(error => {
            console.error('Error:', error);
            setTimeout(() => {
                hideTypingIndicator();
                addMessage('Sorry, there was an error processing your message.', false);
            }, 1000);
        });

        // Reset imageData and hide preview after sending
        imageData = null;
        selectedImagePreview.style.display = 'none';
    } else if (!message && imageData) {
        errorMessage.style.display = 'block'; // Show error message if only image is sent
    }
}

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

fileInput.addEventListener('change', function() {
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            imageData = event.target.result;
            previewImage.src = imageData;
            selectedImagePreview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});

// Show online status after 2 seconds
setTimeout(() => {
    onlineStatus.style.opacity = '1';
}, 2000);

// Initial message
setTimeout(() => {
    addMessage("Hey, mera naam Simran hai🎀🎀, Apka naam kya hai?😜", false);
}, 1000);