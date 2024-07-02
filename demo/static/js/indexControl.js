$(function() {
    login_traditional();
    login_mfa();
    login_passwordless();
    login_social();
    register();
    forgotpassword();
});

function login_traditional() {
    $("#btn-minimal-login").click(function() {
        if ($('#minimal-login-email').val().trim() == '' || $('#minimal-login-password').val().trim() == '') {
            $("#minimal-login-message").text("All fields are required.");
            $("#minimal-login-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "GET",
            url: "/login",
            dataType: "json",
            data: $.param({
                email: $("#minimal-login-email").val(),
                password: $("#minimal-login-password").val()
            }),
            success: function(res) {
                getProfile(res.access_token, res.Profile.Uid);
            },
            error: function(xhr, status, error) {
                $("#minimal-login-message").text(xhr.responseText);
                $("#minimal-login-message").attr("class", "error-message");
            }
        });
    });
}

function login_mfa() {
    $("#btn-minimal-mfalogin-next").click(function() {
        if ($('#minimal-mfalogin-email').val().trim() == '' || $('#minimal-mfalogin-password').val().trim() == '') {
            $("#minimal-mfalogin-message").text("All fields are required.");
            $("#minimal-mfalogin-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "POST",
            url: "/mfa",
            dataType: "json",
            data: $.param({
                email: $("#minimal-mfalogin-email").val(),
                password: $("#minimal-mfalogin-password").val()
            }),
            success: function(res) {
                $("#minimal-mfalogin-message").text("");
                if (res.SecondFactorAuthentication) {
                    if (res.SecondFactorAuthentication.IsGoogleAuthenticatorVerified === false) {
                        $("#minimal-mfalogin-qrcode").append('<img src="' + res.SecondFactorAuthentication.QRCode + '">');
                    }
                    $("#minimal-mfalogin-next")
                        .html('<table><tbody><tr>' +
                            '<td>Authenticator Code: </td><td><input type="text" id="minimal-mfalogin-googlecode"></td>' +
                            '</tr></tbody></table>' +
                            '<button id="btn-minimal-mfalogin-login">Login</button>');
                    $("#btn-minimal-mfalogin-login").on('click', function() {
                        validateGoogleCode(res.SecondFactorAuthentication.SecondFactorAuthenticationToken);
                    });
                } else {
                    getProfile(res.access_token, res.Profile.Uid);
                }
            },
            error: function(xhr) {
                $("#minimal-mfalogin-message").text(xhr.responseText);
                $("#minimal-mfalogin-message").attr("class", "error-message");
            }
        });
    });
}

function validateGoogleCode(gtoken) {
    if ($('#minimal-mfalogin-googlecode').val().trim() == '') {
            $("#minimal-mfalogin-message").text("All fields are required.");
            $("#minimal-mfalogin-message").attr("class", "error-message");
            return;
        }
    $.ajax({
        type: "PUT",
        url: "/mfa/verify",
        dataType: "json",
        data: $.param({
            code: $("#minimal-mfalogin-googlecode").val(),
            token: gtoken
        }),
        success: function(res) {
            getProfile(res.access_token, res.Profile.Uid);
        },
        error: function(xhr) {
            $("#minimal-mfalogin-message").text(xhr.responseText);
            $("#minimal-mfalogin-message").attr("class", "error-message");
        }
    });
}

function login_passwordless() {
    $("#btn-minimal-pwless").click(function() {
        if ($('#minimal-pwless-email').val().trim() == '') {
            $("#minimal-pwless-message").text("All fields are required.");
            $("#minimal-pwless-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "GET",
            url: "/passwordless",
            dataType: "json",
            data: $.param({
                email: $("#minimal-pwless-email").val()
            }),
            success: function(res) {
                $("#minimal-pwless-message").text("Check your email for the login link.");
                $("#minimal-pwless-message").attr("class", "success-message");
            },
            error: function(xhr, status, error) {
                $("#minimal-pwless-message").text(xhr.responseText);
                $("#minimal-pwless-message").attr("class", "error-message");
            }
        });
    });
}

function login_social() { // uses js-library
    let social_script = $(
        '<script type="text/html" id="loginradiuscustom_tmpl">' +
        '<a class="lr-provider-label" href="javascript:void(0)" onclick="return LRObject.util.openWindow(\'<#= Endpoint #>\');" title="<#= Name #>" alt="Sign in with <#=Name#>">' +
        '<span class="lr-ls-icon lr-ls-icon-<#= Name #>"></span>' +
        '</a>&nbsp;&nbsp;&nbsp;' +
        '</script>'
    );

    $("#sociallogin").append(social_script);

    let custom_interface_option = {};
    let sl_options = {};

    sl_options.onSuccess = function(res) {
        getProfile(res.access_token, res.Profile.Uid);
    };
    sl_options.onError = function(err) {
        //console.log("Sociallogin err::", err);
    };

    custom_interface_option.templateName = 'loginradiuscustom_tmpl';
    sl_options.container = "sociallogin-container";

    LRObject.util.ready(function() {
        LRObject.customInterface(".interfacecontainerdiv", custom_interface_option);
        LRObject.init('socialLogin', sl_options);
    });
}

function register() {
    $("#btn-minimal-signup").click(function() {
        if ($("#minimal-signup-password").val() == '' || $("#minimal-signup-email").val() == '' || $("#minimal-signup-confirmpassword").val() == '' ) {
            $("#minimal-signup-message").text("All fields are required.");
            $("#minimal-signup-message").attr("class", "error-message");
            return;
        }

        $.ajax({
            type: "POST",
            url: "/register",
            dataType: "json",
            data: $.param({
                email: $("#minimal-signup-email").val(),
                password: $("#minimal-signup-password").val()
            }),
            success: function(res) {
                $("#minimal-signup-message").text("Check your email to verify your account.");
                $("#minimal-signup-message").attr("class", "success-message");
            },
            error: function(xhr, status, error) {
                $("#minimal-signup-message").text(xhr.responseText);
                $("#minimal-signup-message").attr("class", "error-message");
            }
        });
    });
}

function forgotpassword() {
    $("#btn-minimal-forgotpassword").click(function() {
        if ($("#minimal-forgotpassword-email").val() == '') {
            $("#minimal-forgotpassword-message").text("All fields are required.");
            $("#minimal-forgotpassword-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "POST",
            url: "/password/forgot",
            dataType: "json",
            data: $.param({
                email: $("#minimal-forgotpassword-email").val()
            }),
            success: function(res) {
                $("#minimal-forgotpassword-message").text("Check your email to start the password reset process.");
                $("#minimal-forgotpassword-message").attr("class", "success-message");
            },
            error: function(xhr, status, error) {
                $("#minimal-forgotpassword-message").text(xhr.responseText);
                $("#minimal-forgotpassword-message").attr("class", "error-message");
            }
        });
    });
}

function getProfile(access_token, profile_uid) {
    localStorage.setItem('LRTokenKey', access_token);
    localStorage.setItem('lr-user-uid', profile_uid);
    window.location.href = "/profile";
}