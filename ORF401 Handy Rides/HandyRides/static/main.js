function getCookie(c_name) {
  var i,x,y,ARRcookies=document.cookie.split(";");
  for (i=0;i<ARRcookies.length;i++){
    x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
    y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
    x=x.replace(/^\s+|\s+$/g,"");
    if (x==c_name) {
      return unescape(y);
    }
  }
}
function setCookie(c_name,value,exdays) {
  var exdate=new Date();
  exdate.setDate(exdate.getDate() + exdays);
  var c_value=escape(value) + ((exdays==null) ? "" : ";expires="+exdate.toUTCString());
  document.cookie=c_name + "=" + c_value;
}

function checkForm(form){
  var search_City = form.children[1].value;
  var search_State = form.children[1].value;

    //part below is making it not load if nothing is put into either of the search fields
    //if((search_City =="") && (search_State=="")){
  return false;
    }
      //part below is attempting to create the pop up for elon musk
      //if (search_City =="Elon Musk") {
        //alert("He's not here");
