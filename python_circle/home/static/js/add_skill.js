$(document).ready(function() {
    var i = 1;
    $("#add_row").click(function() {
      $('#addr' + i).html("<td>" + (i + 1) + "</td><td><input  name=' skill[]' type='text' placeholder=' skill' class='form-control'/></td>");
      $('#tab_logic').append('<tr id="addr' + (i + 1) + '"></tr>');
      i++;
    });
    $("#delete_row").click(function() {
      if (i > 1) {
        $("#addr" + (i - 1)).html('');
        i--;
      }
    });
  });