// copy.js
document.addEventListener('DOMContentLoaded', function() {
    const resultElement = document.getElementById('result');
    const copyButton = document.getElementById('copyButton');
  
    copyButton.addEventListener('click', () => {
      const textToCopy = resultElement.innerText;
  
      const tempTextArea = document.createElement('textarea');
      tempTextArea.value = textToCopy;
      document.body.appendChild(tempTextArea);
  
      tempTextArea.select();
      document.execCommand('copy');
      document.body.removeChild(tempTextArea);
  
      alert('文字已複製：' + textToCopy);
    });
  });