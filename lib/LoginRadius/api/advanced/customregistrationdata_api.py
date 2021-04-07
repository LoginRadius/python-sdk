# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class CustomRegistrationDataApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def auth_get_registration_data(self, type, limit=None, parent_id=None,
        skip=None):
        """This API is used to retrieve dropdown data.
        
        Args:
            type: Type of the Datasource
            limit: Retrieve number of records at a time(max limit is 50)
            parent_id: Id of parent dropdown member(if any).
            skip: Skip number of records from start
		
        Returns:
            Complete user Registration data
        7.1
        """

        if(self._lr_object.is_null_or_whitespace(type)):
            raise Exception(self._lr_object.get_validation_message("type"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(limit is not None):
            query_parameters["limit"] = limit
        if(not self._lr_object.is_null_or_whitespace(parent_id)):
            query_parameters["parentId"] = parent_id
        if(skip is not None):
            query_parameters["skip"] = skip

        resource_path = "identity/v2/auth/registrationdata/" + type
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def validate_registration_data_code(self, code, record_id):
        """This API allows you to validate code for a particular dropdown member.
        
        Args:
            code: Secret Code
            record_id: Selected dropdown item’s record id
		
        Returns:
            Response containing Definition of Complete Validation data
        7.2
        """

        if(self._lr_object.is_null_or_whitespace(code)):
            raise Exception(self._lr_object.get_validation_message("code"))

        if(self._lr_object.is_null_or_whitespace(record_id)):
            raise Exception(self._lr_object.get_validation_message("record_id"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        body_parameters = {}
        body_parameters["code"] = code
        body_parameters["recordId"] = record_id

        resource_path = "identity/v2/auth/registrationdata/validatecode"
        return self._lr_object.execute("POST", resource_path, query_parameters, body_parameters)

    def get_registration_data(self, type, limit=None, parent_id=None,
        skip=None):
        """This API is used to retrieve dropdown data.
        
        Args:
            type: Type of the Datasource
            limit: Retrive number of records at a time(max limit is 50
            parent_id: Id of parent dropdown member(if any).
            skip: Skip number of records from start
		
        Returns:
            Complete user Registration data Fields
        16.1
        """

        if(self._lr_object.is_null_or_whitespace(type)):
            raise Exception(self._lr_object.get_validation_message("type"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(limit is not None):
            query_parameters["limit"] = limit
        if(not self._lr_object.is_null_or_whitespace(parent_id)):
            query_parameters["parentId"] = parent_id
        if(skip is not None):
            query_parameters["skip"] = skip

        resource_path = "identity/v2/manage/registrationdata/" + type
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def add_registration_data(self, registration_data_create_model_list):
        """This API allows you to fill data into a dropdown list which you have created for user Registration. For more details on how to use this API please see our Custom Registration Data Overview
        
        Args:
            registration_data_create_model_list: Model Class containing Definition of List of Registration Data
		
        Returns:
            Response containing Definition of Complete Validation data
        16.2
        """
        if(registration_data_create_model_list is None):
            raise Exception(self._lr_object.get_validation_message("registration_data_create_model_list"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/registrationdata"
        return self._lr_object.execute("POST", resource_path, query_parameters, registration_data_create_model_list)

    def update_registration_data(self, registration_data_update_model, record_id):
        """This API allows you to update a dropdown item
        
        Args:
            registration_data_update_model: Model Class containing Definition of payload for Registration Data update API
            record_id: Registration data RecordId
		
        Returns:
            Complete user Registration data Field
        16.3
        """
        if(registration_data_update_model is None):
            raise Exception(self._lr_object.get_validation_message("registration_data_update_model"))

        if(self._lr_object.is_null_or_whitespace(record_id)):
            raise Exception(self._lr_object.get_validation_message("record_id"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/registrationdata/" + record_id
        return self._lr_object.execute("PUT", resource_path, query_parameters, registration_data_update_model)

    def delete_registration_data(self, record_id):
        """This API allows you to delete an item from a dropdown list.
        
        Args:
            record_id: Registration data RecordId
		
        Returns:
            Response containing Definition of Delete Request
        16.4
        """

        if(self._lr_object.is_null_or_whitespace(record_id)):
            raise Exception(self._lr_object.get_validation_message("record_id"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/registrationdata/" + record_id
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def delete_all_records_by_data_source(self, type):
        """This API allows you to delete all records contained in a datasource.
        
        Args:
            type: Type of the Datasource
		
        Returns:
            Response containing Definition of Delete Request
        16.5
        """

        if(self._lr_object.is_null_or_whitespace(type)):
            raise Exception(self._lr_object.get_validation_message("type"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/registrationdata/type/" + type
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})
