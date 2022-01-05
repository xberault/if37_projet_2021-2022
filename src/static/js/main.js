
(function ($) {
    "use strict";



    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);



$('#speak').click(function(){
    var text = $('#txt_traduit').val();
    var msg = new SpeechSynthesisUtterance();
    msg.rate = 1;
    msg.pitch = 1;
    msg.text = text;
    msg.lang = "french"

    msg.onend = function(e) {
        console.log('Finished in ' + event.elapsedTime + ' seconds.');
    };

    speechSynthesis.speak(msg);
    }


);

// speech recognition


window.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("btn_spr");
    const result = document.getElementById("txt_genre");
    const parent = result.parentNode;
    let listening = false;
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    if (typeof SpeechRecognition !== "undefined") {
      const recognition = new SpeechRecognition();
      recognition.lang ="fr-FR"

      let btnInitialColor = button.style.background;

      const stop = () => {
        parent.classList.remove("speaking");
        recognition.stop();
        button.style.background = btnInitialColor;
      };

      const start = () => {
        parent.classList.add("speaking");
        recognition.start();
        button.style.background = "red"
      };

      const onResult = event => {
        result.innerHTML = "";
        for (const res of event.results) {
          const text = document.createTextNode(res[0].transcript);
          const p = document.createElement("p");
          if (res.isFinal) {
            p.classList.add("final");
          }
          p.appendChild(text);
          result.value = p.innerText;
        }
      };
      recognition.continuous = true;
      recognition.interimResults = true;
      recognition.addEventListener("result", onResult);
      button.addEventListener("click", event => {

        if(listening || confirm("Cela va supprimer le texte déjà entré, êtes-vous sûr ?")){
          listening ? stop() : start();
          listening = !listening;
        }
 
      });
    } else {
      button.remove();
      const message = document.getElementById("message");
      message.removeAttribute("hidden");
      message.setAttribute("aria-hidden", "false");
    }
  });



  // copy to clipboard button utils

  function copy() {
    var copyText =  $('#txt_traduit').val();
    
    if (navigator.clipboard) {
      navigator.clipboard.writeText(copyText).then(() => {
        console.log('Copied to clipboard successfully.');
      }, (err) => {
        console.log('Failed to copy the text to clipboard.', err);
      });
    } else if (window.clipboardData) {
      window.clipboardData.setData("Text", copyText);
    }


  }
  
  $('#copy_btn').click(copy)
  