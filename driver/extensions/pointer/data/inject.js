var s = document.createElement('script');
s.src = chrome.runtime.getURL('script.data');
s.onload = function() {
    this.remove();
};
(document.head || document.documentElement).appendChild(s);



