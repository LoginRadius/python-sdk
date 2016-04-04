jQuery(document).ready(function () {
    //handleResponse(true, "");
    jQuery("#fade, #lr-loading").click(function () {
        jQuery('#fade, #lr-loading').hide();
    });   
    // showAndHideUI();
      initializeLoginRaasForm();
       initializeRegisterRaasForm();
      initializeSocialRegisterRaasForm();
      initializeForgotPasswordRaasForms();

       callSocialInterface();
initializeResetPasswordRaasForm(raasoption);
});
//if possible, use a much better toggle
$(document).ready(function() {
    $('.lr-link').click(function(){
        var dataForm = $(this).attr("data-form");
          $('.interfacecontainerdiv').css({'display':'block'});
$('.lr-heading').text('Login with');
        if(dataForm == 'lr-forgot-pw'){
        $('.interfacecontainerdiv').css({'display':'none'});
        $('.lr-heading').text('Forgot Password');
        }
        $('.lr-traditional-frame').removeClass('lr-form-active');

        $("#"+dataForm).addClass('lr-form-active');
    });

    // this makes the first element with that class visible.. if you don't want this.. add that class manually
    $('.lr-traditional-frame:eq(0)').addClass('lr-form-active');
});

//tabs
jQuery(document).ready(function() {
    jQuery('.lr-menu-buttons .lr-buttons').click(function(){
        var dataTab = jQuery(this).attr("data-tab");

        jQuery('.lr-menu-buttons .lr-buttons').removeClass('lr-tab-active');
        jQuery('.lr-profile-frame .lr-frame').removeClass('lr-tab-active');

        jQuery(this).addClass('lr-tab-active');
        jQuery("#"+dataTab).addClass('lr-tab-active');
    });

    // this makes the first element with that class visible.. if you don't want this.. add that class manually
    jQuery('.lr-menu-buttons .lr-buttons:eq(0)').addClass('lr-tab-active');
    jQuery('.lr-profile-frame .lr-frame:eq(0)').addClass('lr-tab-active');
});

// Show Password

jQuery(document).ready(function() {
    jQuery('.lr-show-pw').click(function(){
        var dataTab = jQuery('.lr-tab-active').attr("data-tab");
        var placeholder ='';
        var showPass = function() {
            jQuery('.'+dataTab).find('input:password').each(function() {
              
                jQuery("<input type='text' class='showPass' />").attr({ name: this.name, value: this.value }).insertBefore(this);
            }).remove();
        };
        var hidePass = function() {
            jQuery('.'+dataTab).find('input.showPass').each(function() {
                
                jQuery("<input type='Password' />").attr({ name: this.name, value: this.value }).insertBefore(this);
            }).remove();
        };

        if (jQuery('.'+dataTab+' input:password').is(':visible')) {
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
        jQuery('body').on('focus', '.loginradius-raas-birthdate', function () {
            jQuery('.loginradius-raas-birthdate').datepicker({
                dateFormat: 'mm-dd-yy',
                maxDate: new Date(),
                minDate: "-100y",
                changeMonth: true,
                changeYear: true,
                yearRange: (minYear + ":" + maxYear)
            });
        });
    } else {
        jQuery(".loginradius-raas-birthdate").live("focus", function () {
            jQuery('.loginradius-raas-birthdate').datepicker({
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
    }
    else {
        jQuery('#fade').hide();
    }
}


function handleResponse(isSuccess, message, show, status) {
    status = status ? status : "status";
    if (status == "error" && window.LoginRadiusSSO) {
        LoginRadiusSSO.init(raasoption.appName);
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
        jQuery("html, body").animate({ scrollTop: 0 }, "slow");
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
LoginRadiusRaaS.$hooks.setProcessHook(function () {

    // console.log("start process", '');
    jQuery('#lr-loading').show();
}, function () {
    if (jQuery('.lr_account_linking') && jQuery('#interfacecontainerdiv').text() != '') {
        linking();
    }
    if(raasoption.formRenderDelay){
        setTimeout(function(){ jQuery('#lr-loading').hide(); }, raasoption.formRenderDelay-1);
    }

    //  jQuery('#lr-loading').hide();
});
LoginRadiusRaaS.$hooks.socialLogin.onFormRender = function () {
    jQuery('#lr-loading').hide();
	jQuery('#lr-sign-in').removeClass('lr-form-active');
	jQuery('.interfacecontainerdiv').hide();
	
    jQuery('#lr-social-register').addClass('lr-form-active');
    show_birthdate_date_block();
    //ShowformbyId("social_registration_from");
};
function callSocialInterface() {
    LoginRadiusRaaS.CustomInterface(".interfacecontainerdiv", raasoption);
    jQuery('#lr-loading').hide();
}
function initializeLoginRaasForm() {
//initialize Login form
    LoginRadiusRaaS.init(raasoption, 'login', function (response) {
        handleResponse(true, "");
        raasRedirect(response.access_token);
    }, function (response) {
        if (response[0].description != null) {
            handleResponse(false, response[0].description, "", "error");
        }
    }, "login-container");
    jQuery('#lr-loading').hide();

}

function initializeRegisterRaasForm() {
    LoginRadiusRaaS.init(raasoption, 'registration', function (response, data) {      
        if (response.access_token != null && response.access_token != "") {
                    handleResponse(true, "");
                    raasRedirect(response.access_token);
        }else{ 
             handleResponse(false, "An email has been sent to " + jQuery("#loginradius-raas-registration-emailid").val() + ".Please verify your email address.");
                window.setTimeout(function() {
                        window.location.replace(homeDomain);  
                }, 7000);                   
        }
    }, function (response) {      
        if (response[0].description != null) {
            handleResponse(false, response[0].description, "", "error");
        }
    }, "registeration-container");
    jQuery('#lr-loading').hide();
}
function initializeResetPasswordRaasForm(raasoption) {
    //initialize reset password form and handel email verifaction
    var vtype = $LR.util.getQueryParameterByName("vtype");
    if (vtype != null && vtype != "") {
        LoginRadiusRaaS.init(raasoption, 'resetpassword', function (response) {
            handleResponse(true, "Password reset successfully");
            window.location = raasoption.emailVerificationUrl;
        }, function (response) {
            handleResponse(false, response[0].description, "", "error");
        }, "resetpassword-container");   
        if (vtype == "reset") {
            LoginRadiusRaaS.init(raasoption, 'emailverification', function (response) {
                handleResponse(true, "");
                jQuery('.lr-heading').text('Reset Password');
                jQuery('#lr-reset-pw').show();
                jQuery('#lr-sign-in').hide();
                jQuery('.interfacecontainerdiv').hide();
            }, function (response) {
                handleResponse(false, response[0].description, "", "error");
            });
        } else {
            LoginRadiusRaaS.init(raasoption, 'emailverification', function (response) {               
                //On Success this callback will call
                if (response.access_token != null && response.access_token != "") {
                    handleResponse(true, "");
                    raasRedirect(response.access_token);
                } else {
                    handleResponse(true, "Your email has been verified successfully");
                } 
            }, function (response) {
                // on failure this function will call ‘errors’ is an array of error with message.
                handleResponse(false, response[0].description, "", "error");
            });
        }
    }
    jQuery('#lr-loading').hide();
}
function initializeSocialRegisterRaasForm() {
    //initialize social Login form
    LoginRadiusRaaS.init(raasoption, 'sociallogin', function (response) {
        if (response.isPosted) {
            handleResponse(true, "An email has been sent to " + jQuery("#loginradius-raas-social-registration-emailid").val() + ".Please verify your email address.");
            jQuery('#lr-social-register').hide();
        } else {
            handleResponse(true, "", true);
            raasRedirect(response);
        }
    }, function (response) {
        if (response[0].description != null) {
            handleResponse(false, response[0].description, "", "error");
            jQuery('#lr-social-register').hide();
        }
    }, "social-registration-container");

    jQuery('#lr-loading').hide();

}

function initializeForgotPasswordRaasForms() {
    //initialize forgot password form
    LoginRadiusRaaS.init(raasoption, 'forgotpassword', function (response) {     
         handleResponse(false, "An email has been sent to " + jQuery("#loginradius-raas-forgotpassword-emailid").val() + " with reset Password link.");
            window.setTimeout(function() {
                    window.location.replace(homeDomain);
            }, 7000);
      
    }, function (response) {
        if (response[0].description != null) {
            handleResponse(false, response[0].description, "", "error");
        }
    }, "forgotpassword-container");
    jQuery('#lr-loading').hide();
}
function initializeAccountLinkingRaasForms() {
    LoginRadiusRaaS.init(raasoption, "accountlinking", function (response) {
        handleResponse(true, "");
        raasRedirect(response);
    }, function (response) {
        jQuery('#fade').hide();
        if (response[0].description != null) {
            handleResponse(false, response[0].description, "", "error");
        }
    }, "interfacecontainerdiv");
    jQuery('#lr-loading').hide();
}
function initializeChangePasswordRaasForms() {
   // initializeAccountLinkingRaasForms();
    LoginRadiusRaaS.passwordHandleForms("setpasswordbox", "changepasswordbox", function (israas) {
//var password_div = jQuery('a[href*="/changepassword"]');
        var password_div = jQuery('#page-title');
        if (israas) {
            password_div.html('Change Password');
            jQuery("#changepasswordbox").show();
        } else {
            password_div.html('Set Password');
            jQuery("#setpasswordbox").show();
        }
    }, function () {
        document.forms['setpassword'].action = window.location;
        document.forms['setpassword'].submit();
    }, function () {

    }, function () {
        document.forms['changepassword'].action = window.location;
        document.forms['changepassword'].submit();
    }, function () {

    }, raasoption);
    jQuery('#lr-loading').hide();
}
function raasRedirect(token, name) {
    var str = window.location.href; 
    var callback = str.replace("frontend", "backend");

    if (window.redirect) {
        redirect(token, name);
    }
    else {
        var token_name = name ? name : 'token';
        var source = typeof lr_source != 'undefined' && lr_source ? lr_source : '';

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


