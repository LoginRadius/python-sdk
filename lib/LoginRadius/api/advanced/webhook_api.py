# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2025 LoginRadius Inc. All rights reserved.
#


class WebHookApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def get_webhook_subscription_detail(self, hook_id):
        """This API is used to get details of a webhook subscription by Id
        
        Args:
            hook_id: Unique ID of the webhook
		
        Returns:
            Response containing Definition for Complete WebHook data
        40.1
        """

        if(self._lr_object.is_null_or_whitespace(hook_id)):
            raise Exception(self._lr_object.get_validation_message("hook_id"))

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()

        resource_path = "v2/manage/webhooks/" + hook_id
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def create_webhook_subscription(self, web_hook_subscribe_model):
        """This API is used to create a new webhook subscription on your LoginRadius site.
        
        Args:
            web_hook_subscribe_model: Model Class containing Definition of payload for Webhook Subscribe API
		
        Returns:
            Response containing Definition for Complete WebHook data
        40.2
        """
        if(web_hook_subscribe_model is None):
            raise Exception(self._lr_object.get_validation_message("web_hook_subscribe_model"))

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()

        resource_path = "v2/manage/webhooks"
        return self._lr_object.execute("POST", resource_path, query_parameters, web_hook_subscribe_model)

    def delete_webhook_subscription(self, hook_id):
        """This API is used to delete webhook subscription
        
        Args:
            hook_id: Unique ID of the webhook
		
        Returns:
            Response containing Definition of Delete Request
        40.3
        """

        if(self._lr_object.is_null_or_whitespace(hook_id)):
            raise Exception(self._lr_object.get_validation_message("hook_id"))

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()

        resource_path = "v2/manage/webhooks/" + hook_id
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def update_webhook_subscription(self, hook_id, web_hook_subscription_update_model):
        """This API is used to update a webhook subscription
        
        Args:
            hook_id: Unique ID of the webhook
            web_hook_subscription_update_model: Model Class containing Definition for WebHookSubscriptionUpdateModel Property
		
        Returns:
            Response containing Definition for Complete WebHook data
        40.4
        """

        if(self._lr_object.is_null_or_whitespace(hook_id)):
            raise Exception(self._lr_object.get_validation_message("hook_id"))
        if(web_hook_subscription_update_model is None):
            raise Exception(self._lr_object.get_validation_message("web_hook_subscription_update_model"))

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()

        resource_path = "v2/manage/webhooks/" + hook_id
        return self._lr_object.execute("PUT", resource_path, query_parameters, web_hook_subscription_update_model)

    def list_all_webhooks(self):
        """This API is used to get the list of all the webhooks
        
        Returns:
            Response Containing List of Webhhook Data
        40.5
        """

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()

        resource_path = "v2/manage/webhooks"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_webhook_events(self):
        """This API is used to retrieve all the webhook events.
        
        Returns:
            Model Class containing Definition for WebHookEventModel Property
        40.6
        """

        query_parameters = {}
        query_parameters["apikey"] = self._lr_object.get_api_key()
        query_parameters["apisecret"] = self._lr_object.get_api_secret()

        resource_path = "v2/manage/webhooks/events"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})
