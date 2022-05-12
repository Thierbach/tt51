window.onload = function() {
  var conversationalForm = window.cf.ConversationalForm.startTheConversation({
    formEl: document.getElementById("form"),
    context: document.getElementById("cf-context"),    
    dictionaryData: {
        "input-placeholder": "Gib bitte hier Deine Antwort ein ...",
        "user-reponse-missing": "Fehlende Eingabe ..."
    },
    submitCallback: function() {
      var formData = conversationalForm.getFormData();
                    var formDataSerialized = conversationalForm.getFormData(true);
                    console.log("Formdata:", formData);
                    console.log("Formdata, serialized:", formDataSerialized);
                    const myTimeout = setTimeout(nextStep(formDataSerialized), 5000);

     conversationalForm.addRobotChatResponse("Danke, das war's schon!"); 
     
    }
  });
};

function nextStep(formDataSerialized) {
console.log(formDataSerialized);
//alert("Gute gemacht!" + "\n" + "Weiter geht's zum Dokumenten Upload...");
}
