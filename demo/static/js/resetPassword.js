$(function() {
    resetPasswordHandler();
});

function resetPasswordHandler() {
    if (getUrlParameter("vtype") === 'reset') {
        $('#btn-minimal-resetpassword').on('click', function() {
            if ($("#minimal-resetpassword-password").val() !== $("#minimal-resetpassword-confirmpassword").val()) {
                $("#minimal-resetpassword-message").text("Passwords do not match!");
                $("#minimal-resetpassword-message").attr("class", "error-message");
                return;
            }

            $.ajax({
                type: "PUT",
                url: "/password/reset",
                dataType: "json",
                data: $.param({
                    password: $("#minimal-resetpassword-password").val(),
                    token: getUrlParameter("vtoken")
                }),
                success: function(res) {
                    $("#minimal-resetpassword-message").text("Password reset successful.");
                    $("#minimal-resetpassword-message").attr("class", "success-message");
                },
                error: function(xhr, status, error) {
                    $("#minimal-resetpassword-message").text(xhr.responseText);
                    $("#minimal-resetpassword-message").attr("class", "error-message");
                }
            });
        });
    }
}

function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
}