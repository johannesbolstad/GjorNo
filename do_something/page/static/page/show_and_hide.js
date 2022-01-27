
function show_hide(element_id)
{
    if (document.getElementById(element_id).style.display === 'none'){
        document.getElementById(element_id).style.display = 'inline';
        document.getElementById(element_id).parentElement.children[2].innerHTML = "&nbsp; Lukk &nbsp;";
        document.getElementById(element_id).parentElement.children[2].style.backgroundColor = '#dc3545'
    }
    else{
        document.getElementById(element_id).style.display = 'none';
        document.getElementById(element_id).parentElement.children[2].style.backgroundColor = '#20B2AA'
        document.getElementById(element_id).parentElement.children[2].innerHTML = "Se mer";
    
    }
   
}
function reply_click(clicked_id)
  { 
    
      return clicked_id;
  }