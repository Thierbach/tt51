window.onload = function() {
  var conversationalForm = window.cf.ConversationalForm.startTheConversation({
    formEl: document.getElementById("form"),
    context: document.getElementById("cf-context"),    
    showProgressBar: true, 
    dictionaryData: {
        "input-placeholder": "Gib bitte hier Deine Antwort ein ...",
        "user-reponse-missing": "Fehlende Eingabe ...",
        "user-reponse": "Keine Auswahl getroffen ...",
        "input-placeholder": "Geben Sie hier Ihre Antwort ein ...",
        "input-placeholder-error": "Ihre Eingabe ist nicht korrekt ...",
        "input-no-filter": "Keine Ergebnisse für {input-value}",
        "general": "Allgemeiner Typ1|Allgemeiner Typ2",
        "input-placeholder-required": "Eingabe erforderlich ...",
        "user-response-and": "Beantworte bitte die Frage ..."
    },
    dictionaryRobot: {
    	"checkbox": "Wählen Sie so viele, wie Sie möchten."
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
