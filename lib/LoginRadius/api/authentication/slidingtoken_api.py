# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class SlidingTokenApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def sliding_access_token(self, access_token):
        """
        
        Args:
            access_token: 
		
        Returns:
            Response containing Definition of Complete Token data
        1.3
        """

        if(self._lr_object.is_null_or_whitespace(access_token)):
            raise Exception(self._lr_object.get_validation_message("access_token"))

        query_parameters = {}
        query_parameters["access_token"] = access_token
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "identity/v2/auth/access_token/sliding_token"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})
