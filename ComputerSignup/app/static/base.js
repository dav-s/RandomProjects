
function checkandsub(){
    var form = document.forms["formy"];
    var errorText = "";
    var hasError=false;
    if(! /^[0-9]{2,10}$/.test(form["stid"].value)){
        errorText+="<h3>Student ID is only numbers</h3>";
        hasError=true;
    }if(! /^[a-zA-Z- ]{1,30}$/.test(form["fname"].value)){
        errorText+="<h3>First name must be valid</h3>";
        hasError=true;
    }if(! /^[a-zA-Z- ]{1,30}$/.test(form["lname"].value)){
        errorText+="<h3>Last name must be valid</h3>";
        hasError=true;
    }if(! /^[a-zA-Z0-9-]{6,20}$/.test(form["cname"].value)){
        errorText+="<h3>The computer name is only alphanumeric with dashes</h3>";
        hasError=true;
    }if(! /^(Westerduin|Christopher|Kenney)$/.test(form["teacher"].value)){
        errorText+="<h3>Please choose an appropriate teacher</h3>";
        hasError=true;
    }if(! /^(Yes|No)$/.test(form["paid"].value)){
        errorText+="<h3>Please choose yes or no</h3>";
        hasError=true;
    }

    if (hasError){
        document.getElementById('errors').innerHTML=errorText;
        return false;
    }
    return true;
}