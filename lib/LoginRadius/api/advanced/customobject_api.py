# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class CustomObjectApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def create_custom_object_by_token(self, access_token, object_name, payload):
        """This API is used to write information in JSON format to the custom object for the specified account.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            object_name: LoginRadius Custom Object Name
            payload: LoginRadius Custom Object Name
		
        Returns:
            Response containing Definition for Complete user custom object data
        6.1
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))
        if(payload is None):
            raise Exception(self._lr_object.get_validation_message("payload"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["objectName"] = object_name

        resource_path = "identity/v2/auth/customobject"
        return self._lr_object.execute("POST", resource_path, query_parameters, payload)

    def update_custom_object_by_token(self, access_token, object_name, object_record_id,
        payload, update_type=None):
        """This API is used to update the specified custom object data of the specified account. If the value of updatetype is 'replace' then it will fully replace custom object with the new custom object and if the value of updatetype is 'partialreplace' then it will perform an upsert type operation
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            object_name: LoginRadius Custom Object Name
            object_record_id: Unique identifier of the user's record in Custom Object
            payload: LoginRadius Custom Object Name
            update_type: Possible values: replace, partialreplace.
		
        Returns:
            Response containing Definition for Complete user custom object data
        6.2
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))

        if(self._lr_object.is_null_or_whitespace(object_record_id)):
            raise Exception(self._lr_object.get_validation_message("object_record_id"))
        if(payload is None):
            raise Exception(self._lr_object.get_validation_message("payload"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["objectName"] = object_name
        if(update_type is not None):
            query_parameters["updateType"] = update_type

        resource_path = "identity/v2/auth/customobject/" + object_record_id
        return self._lr_object.execute("PUT", resource_path, query_parameters, payload)

    def get_custom_object_by_token(self, access_token, object_name):
        """This API is used to retrieve the specified Custom Object data for the specified account.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            object_name: LoginRadius Custom Object Name
		
        Returns:
            Complete user CustomObject data
        6.3
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["objectName"] = object_name

        resource_path = "identity/v2/auth/customobject"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_custom_object_by_record_id_and_token(self, access_token, object_name, object_record_id):
        """This API is used to retrieve the Custom Object data for the specified account.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            object_name: LoginRadius Custom Object Name
            object_record_id: Unique identifier of the user's record in Custom Object
		
        Returns:
            Response containing Definition for Complete user custom object data
        6.4
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))

        if(self._lr_object.is_null_or_whitespace(object_record_id)):
            raise Exception(self._lr_object.get_validation_message("object_record_id"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["objectName"] = object_name

        resource_path = "identity/v2/auth/customobject/" + object_record_id
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def delete_custom_object_by_token(self, access_token, object_name, object_record_id):
        """This API is used to remove the specified Custom Object data using ObjectRecordId of a specified account.
        
        Args:
            access_token: Uniquely generated identifier key by LoginRadius that is activated after successful authentication.
            object_name: LoginRadius Custom Object Name
            object_record_id: Unique identifier of the user's record in Custom Object
		
        Returns:
            Response containing Definition of Delete Request
        6.5
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))

        if(self._lr_object.is_null_or_whitespace(object_record_id)):
            raise Exception(self._lr_object.get_validation_message("object_record_id"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["objectName"] = object_name

        resource_path = "identity/v2/auth/customobject/" + object_record_id
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def create_custom_object_by_uid(self, object_name, payload, uid):
        """This API is used to write information in JSON format to the custom object for the specified account.
        
        Args:
            object_name: LoginRadius Custom Object Name
            payload: LoginRadius Custom Object Name
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition for Complete user custom object data
        19.1
        """

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))
        if(payload is None):
            raise Exception(self._lr_object.get_validation_message("payload"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["objectName"] = object_name

        resource_path = "identity/v2/manage/account/" + uid + "/customobject"
        return self._lr_object.execute("POST", resource_path, query_parameters, payload)

    def update_custom_object_by_uid(self, object_name, object_record_id, payload,
        uid, update_type=None):
        """This API is used to update the specified custom object data of a specified account. If the value of updatetype is 'replace' then it will fully replace custom object with new custom object and if the value of updatetype is partialreplace then it will perform an upsert type operation.
        
        Args:
            object_name: LoginRadius Custom Object Name
            object_record_id: Unique identifier of the user's record in Custom Object
            payload: LoginRadius Custom Object Name
            uid: UID, the unified identifier for each user account
            update_type: Possible values: replace, partialreplace.
		
        Returns:
            Response containing Definition for Complete user custom object data
        19.2
        """

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))

        if(self._lr_object.is_null_or_whitespace(object_record_id)):
            raise Exception(self._lr_object.get_validation_message("object_record_id"))
        if(payload is None):
            raise Exception(self._lr_object.get_validation_message("payload"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["objectName"] = object_name
        if(update_type is not None):
            query_parameters["updateType"] = update_type

        resource_path = "identity/v2/manage/account/" + uid + "/customobject/" + object_record_id
        return self._lr_object.execute("PUT", resource_path, query_parameters, payload)

    def get_custom_object_by_uid(self, object_name, uid):
        """This API is used to retrieve all the custom objects by UID from cloud storage.
        
        Args:
            object_name: LoginRadius Custom Object Name
            uid: UID, the unified identifier for each user account
		
        Returns:
            Complete user CustomObject data
        19.3
        """

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["objectName"] = object_name

        resource_path = "identity/v2/manage/account/" + uid + "/customobject"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_custom_object_by_record_id(self, object_name, object_record_id, uid):
        """This API is used to retrieve the Custom Object data for the specified account.
        
        Args:
            object_name: LoginRadius Custom Object Name
            object_record_id: Unique identifier of the user's record in Custom Object
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition for Complete user custom object data
        19.4
        """

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))

        if(self._lr_object.is_null_or_whitespace(object_record_id)):
            raise Exception(self._lr_object.get_validation_message("object_record_id"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["objectName"] = object_name

        resource_path = "identity/v2/manage/account/" + uid + "/customobject/" + object_record_id
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def delete_custom_object_by_record_id(self, object_name, object_record_id, uid):
        """This API is used to remove the specified Custom Object data using ObjectRecordId of specified account.
        
        Args:
            object_name: LoginRadius Custom Object Name
            object_record_id: Unique identifier of the user's record in Custom Object
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        19.5
        """

        if(self._lr_object.is_null_or_whitespace(object_name)):
            raise Exception(self._lr_object.get_validation_message("object_name"))

        if(self._lr_object.is_null_or_whitespace(object_record_id)):
            raise Exception(self._lr_object.get_validation_message("object_record_id"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        query_parameters["objectName"] = object_name

        resource_path = "identity/v2/manage/account/" + uid + "/customobject/" + object_record_id
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})
