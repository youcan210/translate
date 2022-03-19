
// 要素取得

document.addEventListener("DOMContentLoaded", function() {
  let element = document.getElementById("trans-select");
  let text = document.getElementById("origin-form");
  let textArea = document.getElementById("text-area");
  
  element.addEventListener("change", async function () {
    // let btn = document.getElementById("btn");
    let lang = this.value;
    let set_lang = await eel.view_set_lang(lang)();
    // pythonへ値を渡します
    text.addEventListener("change",function() {
      
      eel.send_text_to_python(text.value,set_lang)

    },false);

  },false);

  eel.expose(send_text_to_javascript)
  function send_text_to_javascript(trans_text) {
    if(trans_text) {
      console.log(trans_text);
      textArea.innerHTML += trans_text + "\n";
    }
  }

},false)
