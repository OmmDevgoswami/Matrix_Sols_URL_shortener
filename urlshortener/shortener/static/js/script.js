function copyToClipboard() {
    let copyText = document.getElementById("shortUrl");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
    alert("Copied: " + copyText.value);
}