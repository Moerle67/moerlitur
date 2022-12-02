window.myConfirm = function(text, OK, cancel){ 
    var dialog = document.querySelector("#confirm"), textElement = document.querySelector("#confirm [data-text]");
    if (dialog && textElement) { 
        textElement.innerText = (text && text.length ? text : ""); 
        dialog.setCallback("cancel", cancel); 
        dialog.setCallback("ok", OK); 
        dialog.show(); } }