
function checkandsub(){
    var form = document.forms["formy"];
    var error = document.getElementById('errors');
    if(! /^[0-9]{2,10}$/.test(form["stid"].value)){
        error.innerHTML="Student ID is only numbers";
        return false;
    }if(! /^[a-zA-Z- ]{1,30}$/.test(form["fname"].value)){
        error.innerHTML="First name must be valid";
        return false;
    }if(! /^[a-zA-Z- ]{1,30}$/.test(form["lname"].value)){
        error.innerHTML="Last name must be valid";
        return false;
    }if(! /^[a-zA-Z0-9-]{6,20}$/.test(form["cname"].value)){
        error.innerHTML="The computer name is only alphanumeric with dashes";
        return false;
    }
    return true;
}