// Function to dynamically find tags and link them to explore page
function formatTags() {
    // Find all elements with the class of body and then we can loop through 
    // all of those elements and get the text
    var elements = document.getElementsByClassName('body');
    for (let i = 0; i < elements.length; i++) {
      let bodyText = elements[i].children[0].innerText;
      // Split the text by each word and loop through those words 
      // to find any word that begins with a #
      let words = bodyText.split(' ');
      for (let j = 0; j < words.length; j++) {
        if (words[j][0] === '#') {
            let replacedText = bodyText.replace(/\s\#(.*?)(\s|$)/g, ` <a href="/templates/app/index?query=${words[j].substring(1)}">${words[j]}</a>`);
            elements[i].innerHTML = replacedText;
        }
      }
    }
  }
  formatTags();