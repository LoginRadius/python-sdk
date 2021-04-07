# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class SottApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def generate_sott(self, time_difference=None):
        """This API allows you to generate SOTT with a given expiration time.
        
        Args:
            time_difference: The time difference you would like to pass, If you not pass difference then the default value is 10 minutes
		
        Returns:
            Sott data For Registration
        18.28
        """

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()
        if(time_difference is not None):
            query_parameters["timeDifference"] = time_difference

        resource_path = "identity/v2/manage/account/sott"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})
