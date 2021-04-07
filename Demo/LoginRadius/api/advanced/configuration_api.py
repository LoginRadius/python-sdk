# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class ConfigurationApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def get_configurations(self):
        """This API is used to get the configurations which are set in the LoginRadius Dashboard for a particular LoginRadius site/environment

		Returns:
		    Response containing LoginRadius App configurations which are set in the LoginRadius Dashboard for a particular LoginRadius site/environment
        100
        """

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()

        resource_path = "ciam/appinfo"
        return self._lr_object.execute("GET", resource_path, query_parameters, None)

    def get_server_info(self, time_difference=None):
        """This API allows you to query your LoginRadius account for basic server information and server time information which is useful when generating an SOTT token.
        
        Args:
            time_difference: The time difference you would like to pass, If you not pass difference then the default value is 10 minutes
		
        Returns:
            Response containing Definition of Complete service info data
        3.1
        """

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        if(time_difference is not None):
            query_parameters["timeDifference"] = time_difference

        resource_path = "identity/v2/serverinfo"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})
