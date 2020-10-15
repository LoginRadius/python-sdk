# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class WebHookApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def get_web_hook_subscribed_u_r_ls(self, event):
        """This API is used to fatch all the subscribed URLs, for particular event
        
        Args:
            event: Allowed events: Login, Register, UpdateProfile, ResetPassword, ChangePassword, emailVerification, AddEmail, RemoveEmail, BlockAccount, DeleteAccount, SetUsername, AssignRoles, UnassignRoles, SetPassword, LinkAccount, UnlinkAccount, UpdatePhoneId, VerifyPhoneNumber, CreateCustomObject, UpdateCustomobject, DeleteCustomObject
		
        Returns:
            Response Containing List of Webhhook Data
        40.1
        """

        if(self._lr_object.is_null_or_whitespace(event)):
            raise Exception(self._lr_object.get_validation_message("event"))

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()
        query_parameters["event"] = event

        resource_path = "api/v2/webhook"
        return self._lr_object.execute("GET", resource_path, query_parameters, None)

    def web_hook_subscribe(self, web_hook_subscribe_model):
        """API can be used to configure a WebHook on your LoginRadius site. Webhooks also work on subscribe and notification model, subscribe your hook and get a notification. Equivalent to RESThook but these provide security on basis of signature and RESThook work on unique URL. Following are the events that are allowed by LoginRadius to trigger a WebHook service call.
        
        Args:
            web_hook_subscribe_model: Model Class containing Definition of payload for Webhook Subscribe API
		
        Returns:
            Response containing Definition of Complete Validation data
        40.2
        """
        if(web_hook_subscribe_model is None):
            raise Exception(self._lr_object.get_validation_message("web_hook_subscribe_model"))

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()

        resource_path = "api/v2/webhook"
        return self._lr_object.execute("POST", resource_path, query_parameters, web_hook_subscribe_model)

    def webhook_test(self):
        """API can be used to test a subscribed WebHook.
        
        Returns:
            Response containing Definition of Complete Validation data
        40.3
        """

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()

        resource_path = "api/v2/webhook/test"
        return self._lr_object.execute("GET", resource_path, query_parameters, None)

    def web_hook_unsubscribe(self, web_hook_subscribe_model):
        """API can be used to unsubscribe a WebHook configured on your LoginRadius site.
        
        Args:
            web_hook_subscribe_model: Model Class containing Definition of payload for Webhook Subscribe API
		
        Returns:
            Response containing Definition of Delete Request
        40.4
        """
        if(web_hook_subscribe_model is None):
            raise Exception(self._lr_object.get_validation_message("web_hook_subscribe_model"))

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()

        resource_path = "api/v2/webhook"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, web_hook_subscribe_model)
