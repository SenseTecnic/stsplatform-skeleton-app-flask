jQuery(function($) {
    $('form[data-async]').on('submit', function(event) {

        var $form = $(this);
        var $target = $($form.attr('data-target'));
        var button_method = $form.find('button[clicked=true]').attr('data-method');
        $.ajax({
            method: button_method !== undefined ? button_method : $form.attr('method'),
            url: $form.attr('action'),
            data: $form.serialize(),

            success: function(data, status) {
                $target.html(data);
            }
        });
        event.preventDefault();

        if ($form.attr('data-modal') === "true") {
          $('#credentialsModal').modal('hide'); //In the case of the modal, close it.
        }

    });

    $("form button[type=submit]").click(function() {
        $("button[type=submit]", $(this).parents("form")).removeAttr("clicked");
        $(this).attr("clicked", "true");
    });

});
