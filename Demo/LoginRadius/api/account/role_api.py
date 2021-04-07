# -- coding: utf-8 --
# Created by LoginRadius Development Team
# Copyright 2019 LoginRadius Inc. All rights reserved.
#


class RoleApi:

    def __init__(self, lr_object):
        """
        :param lr_object: this is the reference to the parent LoginRadius object.
        """
        self._lr_object = lr_object

    def get_roles_by_uid(self, uid):
        """API is used to retrieve all the assigned roles of a particular User.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Complete Roles data
        18.6
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/role"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def assign_roles_by_uid(self, account_roles_model, uid):
        """This API is used to assign your desired roles to a given user.
        
        Args:
            account_roles_model: Model Class containing Definition of payload for Create Role API
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Complete Roles data
        18.7
        """
        if(account_roles_model is None):
            raise Exception(self._lr_object.get_validation_message("account_roles_model"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/role"
        return self._lr_object.execute("PUT", resource_path, query_parameters, account_roles_model)

    def unassign_roles_by_uid(self, account_roles_model, uid):
        """This API is used to unassign roles from a user.
        
        Args:
            account_roles_model: Model Class containing Definition of payload for Create Role API
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        18.8
        """
        if(account_roles_model is None):
            raise Exception(self._lr_object.get_validation_message("account_roles_model"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/role"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, account_roles_model)

    def get_role_context_by_uid(self, uid):
        """This API Gets the contexts that have been configured and the associated roles and permissions.
        
        Args:
            uid: UID, the unified identifier for each user account
		
        Returns:
            Complete user RoleContext data
        18.9
        """

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/rolecontext"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def get_role_context_by_context_name(self, context_name):
        """The API is used to retrieve role context by the context name.
        
        Args:
            context_name: Name of context
		
        Returns:
            Complete user RoleContext data
        18.10
        """

        if(self._lr_object.is_null_or_whitespace(context_name)):
            raise Exception(self._lr_object.get_validation_message("context_name"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/rolecontext/" + context_name
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def update_role_context_by_uid(self, account_role_context_model, uid):
        """This API creates a Context with a set of Roles
        
        Args:
            account_role_context_model: Model Class containing Definition of RoleContext payload
            uid: UID, the unified identifier for each user account
		
        Returns:
            Complete user RoleContext data
        18.11
        """
        if(account_role_context_model is None):
            raise Exception(self._lr_object.get_validation_message("account_role_context_model"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/rolecontext"
        return self._lr_object.execute("PUT", resource_path, query_parameters, account_role_context_model)

    def delete_role_context_by_uid(self, context_name, uid):
        """This API Deletes the specified Role Context
        
        Args:
            context_name: Name of context
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        18.12
        """

        if(self._lr_object.is_null_or_whitespace(context_name)):
            raise Exception(self._lr_object.get_validation_message("context_name"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/rolecontext/" + context_name
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def delete_roles_from_role_context_by_uid(self, context_name, role_context_remove_role_model, uid):
        """This API Deletes the specified Role from a Context.
        
        Args:
            context_name: Name of context
            role_context_remove_role_model: Model Class containing Definition of payload for RoleContextRemoveRole API
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        18.13
        """

        if(self._lr_object.is_null_or_whitespace(context_name)):
            raise Exception(self._lr_object.get_validation_message("context_name"))
        if(role_context_remove_role_model is None):
            raise Exception(self._lr_object.get_validation_message("role_context_remove_role_model"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/rolecontext/" + context_name + "/role"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, role_context_remove_role_model)

    def delete_additional_permission_from_role_context_by_uid(self, context_name, role_context_additional_permission_remove_role_model, uid):
        """This API Deletes Additional Permissions from Context.
        
        Args:
            context_name: Name of context
            role_context_additional_permission_remove_role_model: Model Class containing Definition of payload for RoleContextAdditionalPermissionRemoveRole API
            uid: UID, the unified identifier for each user account
		
        Returns:
            Response containing Definition of Delete Request
        18.14
        """

        if(self._lr_object.is_null_or_whitespace(context_name)):
            raise Exception(self._lr_object.get_validation_message("context_name"))
        if(role_context_additional_permission_remove_role_model is None):
            raise Exception(self._lr_object.get_validation_message("role_context_additional_permission_remove_role_model"))

        if(self._lr_object.is_null_or_whitespace(uid)):
            raise Exception(self._lr_object.get_validation_message("uid"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/account/" + uid + "/rolecontext/" + context_name + "/additionalpermission"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, role_context_additional_permission_remove_role_model)

    def get_roles_list(self):
        """This API retrieves the complete list of created roles with permissions of your app.
        
        Returns:
            Complete user Roles List data
        41.1
        """

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/role"
        return self._lr_object.execute("GET", resource_path, query_parameters, {})

    def create_roles(self, roles_model):
        """This API creates a role with permissions.
        
        Args:
            roles_model: Model Class containing Definition of payload for Roles API
		
        Returns:
            Complete user Roles data
        41.2
        """
        if(roles_model is None):
            raise Exception(self._lr_object.get_validation_message("roles_model"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/role"
        return self._lr_object.execute("POST", resource_path, query_parameters, roles_model)

    def delete_role(self, role):
        """This API is used to delete the role.
        
        Args:
            role: Created RoleName
		
        Returns:
            Response containing Definition of Delete Request
        41.3
        """

        if(self._lr_object.is_null_or_whitespace(role)):
            raise Exception(self._lr_object.get_validation_message("role"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/role/" + role
        return self._lr_object.execute("DELETE", resource_path, query_parameters, {})

    def add_role_permissions(self, permissions_model, role):
        """This API is used to add permissions to a given role.
        
        Args:
            permissions_model: Model Class containing Definition for PermissionsModel Property
            role: Created RoleName
		
        Returns:
            Response containing Definition of Complete role data
        41.4
        """
        if(permissions_model is None):
            raise Exception(self._lr_object.get_validation_message("permissions_model"))

        if(self._lr_object.is_null_or_whitespace(role)):
            raise Exception(self._lr_object.get_validation_message("role"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/role/" + role + "/permission"
        return self._lr_object.execute("PUT", resource_path, query_parameters, permissions_model)

    def remove_role_permissions(self, permissions_model, role):
        """API is used to remove permissions from a role.
        
        Args:
            permissions_model: Model Class containing Definition for PermissionsModel Property
            role: Created RoleName
		
        Returns:
            Response containing Definition of Complete role data
        41.5
        """
        if(permissions_model is None):
            raise Exception(self._lr_object.get_validation_message("permissions_model"))

        if(self._lr_object.is_null_or_whitespace(role)):
            raise Exception(self._lr_object.get_validation_message("role"))

        query_parameters = {}
        query_parameters["apiKey"] = self._lr_object.get_api_key()
        query_parameters["apiSecret"] = self._lr_object.get_api_secret()

        resource_path = "identity/v2/manage/role/" + role + "/permission"
        return self._lr_object.execute("DELETE", resource_path, query_parameters, permissions_model)
