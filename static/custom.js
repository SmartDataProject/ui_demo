function dopost(){
  var days = $('#days input:radio:checked').val();
  var hours = $('#hours input:radio:checked').val();
  var game = $('#game').val();
  var budget = $('#budget').val()
  console.log(         {days,hours,game,budget},);
  $.ajax("/post",{
    data: JSON.stringify({days,hours,game,budget}),
    contentType: "application/json",
    type: "POST",
    success: function(data, status){
      console.log(data);
      $('#output').html(data);
    }});
}

function init(){
  console.log('read');
}
