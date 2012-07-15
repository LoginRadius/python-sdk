LoginRadius's Python SDK is used to implement Social Login on your Python website
==========

LoginRadius's Python SDK is a development kit that lets you integrate Social Login through providers such as Facebook, Google, Twitter, and over 20 more on a Python website. The SDK also fetches user profile data and can be customized from your LoginRadius user account. Ex: social icon sets, login interface, provider settings, etc.

Steps to implement LoginRadius Python SDK
===

Step 1: Add SDK file reference to your Python website

  a. Copy the LoginRadius SDK file to your project directory.
  
  b. Include SDK class file on your callback page.
      from login import LoginRadius
      
Step 2: Create LoginRadius object in your code file

  On your callback page, create a LoginRadius object using your unique LoginRadius API Secret.
      def login_with_loginradius(request):  
      login = LoginRadius(request, SECRET_KEY)
          
Step 3: Validate, authenticate and store data from LoginRadius: 

Validate the object using 'IsAuthenticated' variable. After successful validation, access user profile data such as ID, First Name, Last Name, Email using profile.ID, profile.FirstName, profile.LastName, etc.

        from login import LoginRadius  
  
        def login_with_loginradius(request):  
        login = LoginRadius(request, SECRET_KEY)  
        if login.is_authenticated:  
            profile = login.user_profile  
            # profile is a dict with all the information retrieved by the provider

Note: Few providers like Twitter, LinkedIn, etc. doesn't provide email address with User Profile data, so you need to handle these cases in your callback page.

These are the quick and easy steps to integrate Social Login on your Python website, if you have any questions or need a further assistance please contact us at hello@loginradius.com.