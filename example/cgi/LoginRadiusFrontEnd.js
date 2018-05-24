var LRObject = new LoginRadiusV2(commonOptions);
var homeDomain = window.location.origin + window.location.pathname;
jQuery(document).ready(function () {
    //handleResponse(true, "");
    jQuery("#fade, #lr-loading").click(function () {
        jQuery('#fade, #lr-loading').hide();
    });

    initializeLoginCiamForm();
    initializeRegisterCiamForm();
    initializeSocialRegisterCiamForm();
    initializeForgotPasswordCiamForms();
    callSocialInterface();
    show_birthdate_date_block();
    initializeResetPasswordCiamForm(commonOptions);
});
//if possible, use a much better toggle
$(document).ready(function () {
    $('.lr-link').click(function () {
        var dataForm = $(this).attr("data-form");
        $('.interfacecontainerdiv').css({'display': 'block'});
        $('.lr-heading').text('Login with');
        if (dataForm == 'lr-forgot-pw') {
            $('.interfacecontainerdiv').css({'display': 'none'});
            $('.lr-heading').text('Forgot Password');
        }
        $('.lr-traditional-frame').removeClass('lr-form-active');

        $("#" + dataForm).addClass('lr-form-active');
    });

    // this makes the first element with that class visible.. if you don't want this.. add that class manually
    $('.lr-traditional-frame:eq(0)').addClass('lr-form-active');
});

//tabs
jQuery(document).ready(function () {
    jQuery('.lr-menu-buttons .lr-buttons').click(function () {
        var dataTab = jQuery(this).attr("data-tab");

        jQuery('.lr-menu-buttons .lr-buttons').removeClass('lr-tab-active');
        jQuery('.lr-profile-frame .lr-frame').removeClass('lr-tab-active');

        jQuery(this).addClass('lr-tab-active');
        jQuery("#" + dataTab).addClass('lr-tab-active');
    });

    // this makes the first element with that class visible.. if you don't want this.. add that class manually
    jQuery('.lr-menu-buttons .lr-buttons:eq(0)').addClass('lr-tab-active');
    jQuery('.lr-profile-frame .lr-frame:eq(0)').addClass('lr-tab-active');
});

// Show Password

jQuery(document).ready(function () {
    jQuery('.lr-show-pw').click(function () {
        var dataTab = jQuery('.lr-tab-active').attr("data-tab");
        var placeholder = '';
        var showPass = function () {
            jQuery('.' + dataTab).find('input:password').each(function () {

                jQuery("<input type='text' class='showPass' />").attr({name: this.name, value: this.value}).insertBefore(this);
            }).remove();
        };
        var hidePass = function () {
            jQuery('.' + dataTab).find('input.showPass').each(function () {

                jQuery("<input type='Password' />").attr({name: this.name, value: this.value}).insertBefore(this);
            }).remove();
        };

        if (jQuery('.' + dataTab + ' input:password').is(':visible')) {
            showPass();
            jQuery('.lr-show-pw').addClass('lr-toggle');
            //   jQuery('.'+dataTab+' input:text').focus();
        } else {
            hidePass();
            jQuery('.lr-show-pw').removeClass('lr-toggle');
            //  $('.'+dataTab+' input:password').focus();
        }
    });
});

function show_birthdate_date_block() {
    var maxYear = new Date().getFullYear();
    var minYear = maxYear - 100;
    if (jQuery('body').on) {
        jQuery('body').on('focus', '.loginradius-birthdate', function () {
            jQuery('.loginradius-birthdate').datepicker({
                dateFormat: 'mm-dd-yy',
                maxDate: new Date(),
                minDate: "-100y",
                changeMonth: true,
                changeYear: true,
                yearRange: (minYear + ":" + maxYear)
            });
        });
    } else {
        jQuery(".loginradius-birthdate").live("focus", function () {
            jQuery('.loginradius-birthdate').datepicker({
                dateFormat: 'mm-dd-yy',
                maxDate: new Date(),
                minDate: "-100y",
                changeMonth: true,
                changeYear: true,
                yearRange: (minYear + ":" + maxYear)
            });
        });
    }

}
function unLinkAccount(name, id) {
    handleResponse(true, "");
    if (confirm('Are you sure you want to unlink!')) {
        jQuery('#fade').show();
        var array = {};
        array['value'] = 'accountUnLink';
        array['provider'] = name;
        array['providerId'] = id;
        var form = document.createElement('form');
        var key;
        form.action = '';
        form.method = 'POST';
        for (key in array) {
            var hiddenToken = document.createElement('input');
            hiddenToken.type = 'hidden';
            hiddenToken.value = array[key];
            hiddenToken.name = key;
            form.appendChild(hiddenToken);
        }
        document.body.appendChild(form);
        form.submit();
    } else {
        jQuery('#fade').hide();
    }
}


function handleResponse(isSuccess, message, show, status) {
    status = status ? status : "status";
    if (status == "error" && window.LoginRadiusSSO) {
        LoginRadiusSSO.init(commonOptions.appName);
        LoginRadiusSSO.logout(window.location);
    }
    if (typeof show != 'undefined' && !show) {
        jQuery('#fade').show();
    }
    if (message != null && message != "") {
        jQuery('#lr-loading').hide();
        jQuery('.messageinfo').text(message);
        jQuery(".messages").show();
        jQuery('.messageinfo').show();
        jQuery(".messages").removeClass("error status");
        jQuery(".messages").addClass(status);
        if (isSuccess) {
            jQuery('form').each(function () {
                this.reset();
            });
        }
        jQuery("html, body").animate({scrollTop: 0}, "slow");
    } else {
        jQuery(".messages").hide();
        jQuery('.messageinfo').hide();
        jQuery('.messageinfo').text("");
    }
}
function linking() {
    jQuery(".lr-linked-data, .lr-unlinked-data").html('');
    jQuery(".lr-linked").each(function () {
        jQuery(".lr-linked-data").append(jQuery(this).html());
    });
    jQuery(".lr-unlinked").each(function () {
        jQuery(".lr-unlinked-data").append(jQuery(this).html());
    });
    var linked_val = jQuery('.lr-linked-data').html();
    var unlinked_val = jQuery('.lr-unlinked-data').html();
    if (linked_val != '') {

        jQuery(".lr-linked-data").prepend('Connected Account<br>');
    }
    if (unlinked_val != '') {
        jQuery(".lr-unlinked-data").prepend('Choose Social Account to connect<br>');
    }
    jQuery('#interfacecontainerdiv').hide();
}
LRObject.$hooks.register('startProcess', function () {
    jQuery('#lr-loading').show();
}
);
LRObject.$hooks.register('endProcess', function () {
    if (jQuery('.lr_account_linking') && jQuery('#interfacecontainerdiv').text() != '') {
        linking();
    }   
}
);
LRObject.$hooks.register('socialLoginFormRender', function () {
    jQuery('#lr-loading').hide();
    jQuery('#lr-sign-in').removeClass('lr-form-active');
    jQuery('.interfacecontainerdiv').hide();

    jQuery('#lr-social-register').addClass('lr-form-active');
    
});
LRObject.$hooks.register('afterFormRender', function (name) {
    if (name == 'resetpassword') {
        jQuery('.lr-heading').text('Reset Password');
        jQuery('#lr-reset-pw').addClass('lr-form-active');
        // jQuery('#lr-reset-pw').show();
        jQuery('#lr-sign-in').removeClass('lr-form-active');
        jQuery('.interfacecontainerdiv').hide();
    }
});

function callSocialInterface() {
    var custom_interface_option = {};
    custom_interface_option.templateName = 'loginradiuscustom_tmpl';
    LRObject.util.ready(function () {
        LRObject.customInterface(".interfacecontainerdiv", custom_interface_option);
    });
    jQuery('#lr-loading').hide();
}
function initializeLoginCiamForm() {
//initialize Login form
    var login_options = {};
    login_options.onSuccess = function (response) {
        handleResponse(true, "");
        ciamRedirect(response.access_token);
    };
    login_options.onError = function (response) {
        if (response[0].Description != null) {
            handleResponse(false, response[0].Description, "", "error");
        }
    };
    login_options.container = "login-container";

    LRObject.util.ready(function () {
        LRObject.init("login", login_options);
    });
    jQuery('#lr-loading').hide();
}

function initializeRegisterCiamForm() {
    var registration_options = {}
    registration_options.onSuccess = function (response) {
        if (response.ErrorCode != null && response.ErrorCode != '') {
            handleResponse(false, response[0].Description, "", "error");
        } else {
            if (response.access_token != null && response.access_token != "") {
                handleResponse(true, "");
                ciamRedirect(response.access_token);
            } else {
                handleResponse(false, "An email has been sent to " + jQuery("#loginradius-registration-emailid").val() + ".Please verify your email address.");
            }
        }
        jQuery('input[type="text"],input[type="email"],input[type="password"], select, textarea').val('');
    };
    registration_options.onError = function (response) {
        if (response[0].Description != null) {
            handleResponse(false, response[0].Description, "", "error");
        }
    };
    registration_options.container = "registeration-container";
    LRObject.util.ready(function () {
        LRObject.init("registration", registration_options);
    });

    jQuery('#lr-loading').hide();
}
function initializeResetPasswordCiamForm(commonOptions) {
    //initialize reset password form and handel email verifaction
    var vtype = LRObject.util.getQueryParameterByName("vtype");
    if (vtype != null && vtype != "") {
        if (vtype == "reset") {
            var resetpassword_options = {};
            resetpassword_options.container = "resetpassword-container";
            resetpassword_options.onSuccess = function (response) {
                handleResponse(true, "Your password has been successfully set.");
            };
            resetpassword_options.onError = function (errors) {
                handleResponse(false, errors[0].Description, "", "error");
            }
            LRObject.util.ready(function () {
                LRObject.init("resetPassword", resetpassword_options);
            });

        } else {
            var verifyemail_options = {};
            verifyemail_options.onSuccess = function (response) {
                //On Success this callback will call
                if (response.access_token != null && response.access_token != "") {
                    handleResponse(true, "");
                    ciamRedirect(response.access_token);
                } else {
                    handleResponse(true, "Your email has been verified successfully");
                }
            };
            verifyemail_options.onError = function (errors) {
                handleResponse(false, errors[0].Description, "", "error");
            }

            LRObject.util.ready(function () {
                LRObject.init("verifyEmail", verifyemail_options);
            });
        }
    }
    jQuery('#lr-loading').hide();
}
function initializeSocialRegisterCiamForm() {
    var sl_options = {};
    sl_options.onSuccess = function (response) {
        if (response.IsPosted) {
            handleResponse(true, "An email has been sent to " + jQuery("#loginradius-social-registration-emailid").val() + ".Please verify your email address.");
            jQuery('#social-registration-form').hide();
        } else {
            handleResponse(true, "", true);
            ciamRedirect(response.access_token);
        }
    };
    sl_options.onError = function (response) {
        if (response[0].Description != null) {
            handleResponse(false, response[0].Description, "", "error");
            jQuery('#social-registration-form').hide();
        }
    };
    sl_options.container = "social-registration-container";

    LRObject.util.ready(function () {
        LRObject.init('socialLogin', sl_options);
    });

    jQuery('#lr-loading').hide();
}

function initializeForgotPasswordCiamForms() {
    //initialize forgot password form
    var forgotpassword_options = {};
    forgotpassword_options.container = "forgotpassword-container";
    forgotpassword_options.onSuccess = function (response) {
        handleResponse(false, "An email has been sent to " + jQuery("#loginradius-forgotpassword-emailid").val() + " with reset Password link");
    };
    forgotpassword_options.onError = function (response) {
        if (response[0].Description != null) {
            handleResponse(false, response[0].Description, "", "error");
        }
    }
    LRObject.util.ready(function () {
        LRObject.init("forgotPassword", forgotpassword_options);
    });
    jQuery('#lr-loading').hide();
}

function ciamRedirect(token, name) {
    var str = window.location.href;
    var callback = str.replace("frontend", "backend");

    if (window.redirect) {
        redirect(token, name);
    } else {
        var token_name = name ? name : 'token';
        
        jQuery('#fade').show();
        var form = document.createElement('form');
        form.action = callback;
        form.method = 'POST';

        var hiddenToken = document.createElement('input');
        hiddenToken.type = 'hidden';
        hiddenToken.value = token;
        hiddenToken.name = token_name;
        form.appendChild(hiddenToken);

        document.body.appendChild(form);
        form.submit();
    }
}


