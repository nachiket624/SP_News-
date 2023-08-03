$('#modal').on('hidden.bs.modal', function (e) {
    $(this)
      .find("input,textarea,select")
         .val('')
         .end()
      .find("input[type=checkbox], input[type=radio]")
         .prop("checked", "")
         .end();
  })

function validateFormCategoriesorm() {
    var x = document.forms["Categoriesform"]["inputcategories"].value;
    if (x == "") {
      alert("Categorie Must Fill");
      return false;
    }
  }
  

  function validateFormSection() {
    var x = document.forms["Sectionform"]["inputsection"].value;
    if (x == "") {
      alert("Categorie Must Fill");
      return false;
    }
  }