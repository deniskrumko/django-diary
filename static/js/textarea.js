$(function() {

  autosize($('textarea'));

  $( "#note" ).focus();

  $('.box').click(function () {
    $( "#note" ).focus();
  });

  $("#note-date").click(function (event) {
    // show delete dialog for $(this).closest(".server")
    event.stopPropagation();
});

});
