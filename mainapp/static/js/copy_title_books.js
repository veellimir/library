function copyTitle(bookId) {
    const titleElement = document.getElementById('book-title-' + bookId),
          tempInput = document.createElement('input'),
          notificationElement = document.getElementById('copy-notification-' + bookId);

    tempInput.value = titleElement.textContent.trim();
    document.body.appendChild(tempInput);

    tempInput.select();
    tempInput.setSelectionRange(0, 99999);
    document.execCommand('copy');

    document.body.removeChild(tempInput);

    notificationElement.style.display = 'inline';

    setTimeout(function() {
        notificationElement.style.display = 'none';
    }, 1000);
}