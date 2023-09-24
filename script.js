document.addEventListener('DOMContentLoaded', function() {

document.getElementById('translateButton').addEventListener('click', function() {
    speechToText();
});

function speechToText() {
    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';

    recognition.onresult = function(event) {
        const spokenText = event.results[0][0].transcript;
        translateText(spokenText);
    }

    recognition.start();
}

function translateText(text) {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/translate');
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function() {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            const translatedText = response.translatedText;
            displayTranslationResult(translatedText);
        }
    }

    xhr.send(JSON.stringify({ spokenText: text }));
}

function displayTranslationResult(text) {
    const outputDiv = document.getElementById('output');
    outputDiv.textContent = `Translated Text: ${text}`;
}

xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        var translatedText = response.translatedText;
        // Do something with the translated text
    }
};
});
