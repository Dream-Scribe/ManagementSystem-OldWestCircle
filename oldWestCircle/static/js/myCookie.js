function createCookie(cName,cValue){
    var tmp = "";
    document.cookie = tmp + cName + "=" + cValue + ";path=/";
}

function getCookie(cName){
    var name = cName + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name)==0) { return c.substring(name.length,c.length); }
    }
    return "";
}

function deleteCookie(cName){
    var date = new Date();
    date.setTime(date.getTime() - 1);
    document.cookie = cName + "=; expires=" + date.toGMTString() + ";path=/";
}