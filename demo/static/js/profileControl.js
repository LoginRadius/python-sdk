$(function () {
    update_profile();
    change_password();
    set_password();
    account_update();
    account_linking();
    custom_object();
    reset_mfa();
    roles();
    logout();
});

function update_profile() {
    if (localStorage.getItem("LRTokenKey") === null) {
        window.location.href = "/minimal";
        return;
    }

    $.ajax({
        type: "GET",
        url: "/user",
        dataType: "json",
        data: $.param({
            token: localStorage.getItem("LRTokenKey")
        }),
        success: function (res) {
            $("#profile-name").html("<b>" + res.FullName + "</b>");
            $("#profile-provider").text("Provider: " + res.Provider);
            $("#profile-email").text(res.Email[0].Value);
            $("#profile-lastlogin").text("Last Login Date: " + res.LastLoginDate);

            $("#user-updateaccount-firstname").val(res.FirstName);
            $("#user-updateaccount-lastname").val(res.LastName);
            $("#user-updateaccount-about").val(res.About);


        },
        error: function (xhr, status, error) {
            localStorage.removeItem("LRTokenKey");
            localStorage.removeItem("lr-user-uid");
            window.location.href = "/minimal";
        }
    });
}

function change_password() {
    $("#btn-user-changepassword").click(function () {
        if ($('#user-changepassword-oldpassword').val().trim() == '' || $('#user-changepassword-newpassword').val().trim() == '') {
            $("#user-changepassword-message").text("All fields are required.");
            $("#user-changepassword-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "PUT",
            url: "/password/change",
            dataType: "json",
            data: $.param({
                token: localStorage.getItem('LRTokenKey'),
                oldpassword: $("#user-changepassword-oldpassword").val(),
                newpassword: $("#user-changepassword-newpassword").val()
            }),
            success: function (res) {
                $("#user-changepassword-message").text("Password successfully changed.");
                $("#user-changepassword-message").attr("class", "success-message");
            },
            error: function (xhr, status, error) {
                $("#user-changepassword-message").text(xhr.responseText);
                $("#user-changepassword-message").attr("class", "error-message");
            }
        });
    });
}

function set_password() {
    $("#btn-user-setpassword").click(function () {
        if ($('#user-setpassword-password').val().trim() == '') {
            $("#user-setpassword-message").text("All fields are required.");
            $("#user-setpassword-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "PUT",
            url: "/password/set",
            dataType: "json",
            data: $.param({
                uid: localStorage.getItem('lr-user-uid'),
                password: $("#user-setpassword-password").val()
            }),
            success: function (res) {
                $("#user-setpassword-message").text("Password successfully changed.");
                $("#user-setpassword-message").attr("class", "success-message");
            },
            error: function (xhr, status, error) {
                $("#user-setpassword-message").text(xhr.responseText);
                $("#user-setpassword-message").attr("class", "error-message");
            }
        });
    });
}

function account_update() {
    $("#btn-user-updateaccount").click(function () {
        if ($('#user-updateaccount-firstname').val().trim() == '' || $('#user-updateaccount-lastname').val().trim() == '' || $('#user-updateaccount-about').val().trim() == '') {
            $("#user-updateaccount-message").text("All fields are required.");
            $("#user-updateaccount-message").attr("class", "error-message");
            return;
        }

        $.ajax({
            type: "PUT",
            url: "/account",
            dataType: "json",
            data: $.param({
                uid: localStorage.getItem('lr-user-uid'),
                firstname: $("#user-updateaccount-firstname").val(),
                lastname: $("#user-updateaccount-lastname").val(),
                about: $("#user-updateaccount-about").val()
            }),
            success: function (res) {
                $("#user-updateaccount-message").text("Account successfully updated.");
                $("#user-updateaccount-message").attr("class", "success-message");
                update_profile();
            },
            error: function (xhr, status, error) {
                $("#user-updateaccount-message").text(xhr.responseText);
                $("#user-updateaccount-message").attr("class", "error-message");
            }
        });
    });
}

function account_linking() { // uses js-library
    let script = $(
        '<script type="text/html" id="loginradiuscustom_tmpl_link">' +
        '<# if(isLinked) { #>' +
        '<div class="lr-linked">' +
        '<a class="lr-provider-label" href="javascript:void(0)" title="<#= Name #>" alt="Connected" onclick=\'return LRObject.util.unLinkAccount(\"<#= Name.toLowerCase() #>\",\"<#= providerId #>\")\'><#=Name#> is connected | Delete</a>' +
        '</div>' +
        '<# }  else {#>' +
        '<div class="lr-unlinked">' +
        '<a class="lr-provider-label" href="javascript:void(0)" onclick="return LRObject.util.openWindow(\'<#= Endpoint #>\');" title="<#= Name #>" alt="Sign in with <#=Name#>">' +
        '<#=Name#></a></div>' +
        '<# } #>' +
        '</script>'
    );

    $("#script-accountlinking").append(script);

    let la_options = {};
    la_options.container = "interfacecontainerdiv";
    la_options.templateName = 'loginradiuscustom_tmpl_link';
    la_options.onSuccess = function () {
        $("#interfacecontainerdiv").empty();
        LRObject.util.ready(function () {
            LRObject.init("linkAccount", la_options);
        });
    };
    la_options.onError = function (errors) {
        $("#user-accountlinking-message").text(errors[0].Description);
        $("#user-accountlinking-message").attr("class", "error-message");
    };

    let unlink_options = {};
    unlink_options.onSuccess = function () {
        $("#interfacecontainerdiv").empty();
        LRObject.util.ready(function () {
            LRObject.init("linkAccount", la_options);
        });
    };
    unlink_options.onError = function (errors) {
        $("#user-accountlinking-message").text(errors[0].Description);
        $("#user-accountlinking-message").attr("class", "error-message");
    };

    LRObject.util.ready(function () {
        LRObject.init("linkAccount", la_options);
        LRObject.init("unLinkAccount", unlink_options);
    });
}

function custom_object() {
    create_customobject();
    update_customobject();
    delete_customobject();
    get_customobject();
}

function create_customobject() {
    $("#btn-user-createcustomobj").click(function () {
        var input = $("#user-createcustomobj-data").val();
        if (!IsJsonString(input)) {
            $("#user-createcustomobj-message").text("Please input a valid JSON object in the data field.");
            $("#user-createcustomobj-message").attr("class", "error-message");
            return;
        }
        if ($('#user-createcustomobj-objectname').val().trim() == '') {
            $("#user-createcustomobj-message").text("All fields are required.");
            $("#user-createcustomobj-message").attr("class", "error-message");
            return;
        }

        $.ajax({
            type: "POST",
            url: "/customobject?objectname=" + $("#user-createcustomobj-objectname").val() + '&uid=' + localStorage.getItem('lr-user-uid'),
            contentType: 'application/json',
            dataType: "json",
            data: input,
            success: function (res) {
                $("#user-createcustomobj-message").text("Object successfully created.");
                $("#user-createcustomobj-message").attr("class", "success-message");
            },
            error: function (xhr, status, error) {
                $("#user-createcustomobj-message").text(xhr.responseText);
                $("#user-createcustomobj-message").attr("class", "error-message");
            }
        });
    });
}

function update_customobject() {
    $("#btn-user-updatecustomobj").click(function () {

        var input = $("#user-updatecustomobj-data").val();
        if (!IsJsonString(input)) {
            $("#user-updatecustomobj-message").text("Please input a valid JSON object in the data field.");
            $("#user-updatecustomobj-message").attr("class", "error-message");
            return;
        }
        if ($('#user-updatecustomobj-objectname').val().trim() == '') {
            $("#user-updatecustomobj-message").text("All fields are required.");
            $("#user-updatecustomobj-message").attr("class", "error-message");
            return;
        }

        $.ajax({
            type: "PUT",
            url: "/customobject?objectname=" + $("#user-updatecustomobj-objectname").val() + "&objectrecordid=" + $("#user-updatecustomobj-objectrecordid").val() + '&uid=' + localStorage.getItem('lr-user-uid'),
            contentType: 'application/json',
            dataType: "json",
            data: input,
            success: function (res) {
                $("#user-updatecustomobj-message").text("Object successfully updated.");
                $("#user-updatecustomobj-message").attr("class", "success-message");
            },
            error: function (xhr, status, error) {
                $("#user-updatecustomobj-message").text(xhr.responseText);
                $("#user-updatecustomobj-message").attr("class", "error-message");
            }
        });
    });
}

function delete_customobject() {
    $("#btn-user-deletecustomobj").click(function () {
        if ($('#user-deletecustomobj-objectname').val().trim() == '') {
            $("#user-deletecustomobj-message").text("All fields are required.");
            $("#user-deletecustomobj-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "DELETE",
            url: "/customobject?objectname=" + $("#user-deletecustomobj-objectname").val() + "&objectrecordid=" + $("#user-deletecustomobj-objectrecordid").val() + '&uid=' + localStorage.getItem('lr-user-uid'),
            dataType: "json",
            success: function (res) {
                $("#user-deletecustomobj-message").text("Custom object deleted successfully.");
                $("#user-deletecustomobj-message").attr("class", "success-message");
            },
            error: function (xhr, status, error) {
                $("#user-deletecustomobj-message").text(xhr.responseText);
                $("#user-deletecustomobj-message").attr("class", "error-message");
            }
        });
    });
}

function get_customobject() {
    $("#btn-user-getcustomobj").click(function () {
        if ($('#user-getcustomobj-objectname').val().trim() == '') {
            $("#user-getcustomobj-message").text("All fields are required.");
            $("#user-getcustomobj-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "GET",
            url: "/customobject?objectname=" + $("#user-getcustomobj-objectname").val() + '&uid=' + localStorage.getItem('lr-user-uid'),
            dataType: "json",
            success: function (res) {
                $('#table-customobj tr').remove();
                $("#user-getcustomobj-message").text("");
                $("#user-getcustomobj-message").attr("class", "success-message");
                $('<tr>' +
                    '<th>Object ID</th><th>Custom Object</th>' +
                    '<tr>').appendTo("#table-customobj > tbody:last-child");

                for (let i = 0; i < res.data.length; i++) {
                    $("<tr><td>" + res.data[i].Id + "</td></tr>").appendTo("#table-customobj > tbody:last-child");
                    $("<td>", {
                        text: JSON.stringify(res.data[i].CustomObject)
                    }).appendTo("#table-customobj > tbody:last-child > tr:last-child");
                }
            },
            error: function (xhr) {
                $('#table-customobj tr').remove();
                $("#user-getcustomobj-message").text(xhr.responseText);
                $("#user-getcustomobj-message").attr("class", "error-message");
            }
        });
    });
}

function reset_mfa() {
    $("#btn-user-mfa-resetgoogle").click(function () {
        $.ajax({
            type: "DELETE",
            url: "/mfa/reset?uid=" + localStorage.getItem('lr-user-uid'),
            dataType: "json",
            success: function (res) {
                $("#user-mfa-message").text("Google Authenticator settings reset.");
                $("#user-mfa-message").attr("class", "success-message");
            },
            error: function (xhr) {
                $("#user-mfa-message").text(xhr.responseText);
                $("#user-mfa-message").attr("class", "error-message");
            }
        });
    });
}

function roles() {
    create_role();
    delete_role();
    assign_role();
    get_all_roles();
    get_user_roles();
}

function create_role() {
    $("#btn-user-createrole").click(function () {
        if ($('#user-roles-createrole').val().trim() == '') {
            $("#user-createrole-message").text("All fields are required.");
            $("#user-createrole-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "POST",
            url: "/role",
            dataType: "json",
            data: $.param({
                role: $("#user-roles-createrole").val()
            }),
            success: function (res) {
                $("#user-createrole-message").text("Role created successfully.");
                $("#user-createrole-message").attr("class", "success-message");
                get_all_roles();
                get_user_roles();
            },
            error: function (xhr, status, error) {
                $("#user-createrole-message").text(xhr.responseText);
                $("#user-createrole-message").attr("class", "error-message");
            }
        });
    });
}

function delete_role() {
    $("#btn-user-deleterole").click(function () {
        if ($('#user-roles-deleterole').val().trim() == '') {
            $("#user-deleterole-message").text("All fields are required.");
            $("#user-deleterole-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "DELETE",
            url: "/role?role=" + $("#user-roles-deleterole").val(),
            dataType: "json",
            success: function (res) {
                $("#user-deleterole-message").text("Role deleted successfully.");
                $("#user-deleterole-message").attr("class", "success-message");
                get_all_roles();
                get_user_roles();
            },
            error: function (xhr, status, error) {
                $("#user-deleterole-message").text(xhr.responseText);
                $("#user-deleterole-message").attr("class", "error-message");
            }
        });
    });
}

function assign_role() {
    $("#btn-user-assignrole").click(function () {
        if ($('#user-roles-assignrole').val().trim() == '') {
            $("#user-assignrole-message").text("All fields are required.");
            $("#user-assignrole-message").attr("class", "error-message");
            return;
        }
        $.ajax({
            type: "PUT",
            url: "/role/user",
            dataType: "json",
            data: $.param({
                uid: localStorage.getItem('lr-user-uid'),
                role: $("#user-roles-assignrole").val()
            }),
            success: function (res) {
                $("#user-assignrole-message").text("Role added to current user successfully.");
                $("#user-assignrole-message").attr("class", "success-message");
                get_user_roles();
            },
            error: function (xhr) {
                $("#user-assignrole-message").text(xhr.responseText);
                $("#user-assignrole-message").attr("class", "error-message");
            }
        });
    });
}

function get_all_roles() {
    $.ajax({
        type: "GET",
        url: "/role",
        dataType: "json",
        success: function (res) {
            $('#table-allroles tr:not(:first)').remove();
            if (res.data) {
                for (let i = 0; i < res.data.length; i++) {
                    $("<tr></tr>").appendTo("#table-allroles > tbody:last-child");
                    $("<td>", {
                        text: res.data[i].Name
                    }).appendTo('#table-allroles > tbody:last-child > tr:last-child');
                }
            }
        },
        error: function (xhr) {
            //console.log("Get All Roles err::", xhr.responseText);
        }
    });
}

function get_user_roles() {
    $.ajax({
        type: "GET",
        url: "/role/user?" + 'uid=' + localStorage.getItem('lr-user-uid'),
        dataType: "json",
        success: function (res) {
            $('#table-userroles tr:not(:first)').remove();
            if (res.Roles) {
                for (let i = 0; i < res.Roles.length; i++) {
                    $("<tr></tr>").appendTo("#table-userroles > tbody:last-child");
                    $("<td>", {
                        text: res.Roles[i]
                    }).appendTo('#table-userroles > tbody:last-child > tr:last-child');
                }
            }
        },
        error: function (xhr) {
            //console.log("Get User Roles err::", xhr.responseText);
        }
    });
}

function logout() {
    $("#menu-logout").click(function () {
        $.ajax({
            type: "GET",
            url: "/logout",
            dataType: "json",
            data: $.param({
                token: localStorage.getItem("LRTokenKey")
            }),
            success: function (res) {
                localStorage.removeItem("LRTokenKey");
                localStorage.removeItem("lr-user-uid");
                window.location.href = "/minimal";
            },
            error: function (xhr, status, error) {
                //console.log("Logout err::", xhr.responseText);
            }
        });
    });
}

function IsJsonString(str) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}