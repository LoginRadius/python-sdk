LoginRadius's Python SDK is used to implement Social Login on your Python website
==========

LoginRadius's Python SDK is a development kit that lets you integrate Social Login through providers such as Facebook, Google, Twitter, and over 20 more on a Python website. The SDK also fetches user profile data and can be customized from your LoginRadius user account. Ex: social icon sets, login interface, provider settings, etc.

Steps to implement LoginRadius Python SDK
===

Step 1: Add SDK file reference to your Python website

  a. Copy the LoginRadius SDK file to your project directory.
  
  b. Include SDK class file on your callback page.
      
      from LoginRadius import LoginRadius
      
Step 2: Create LoginRadius object in your code file

  On your callback page, create a LoginRadius object using your unique LoginRadius API Secret.
      
     login = LoginRadius(API_SECRET, Token)
          
Step 3: Validate, authenticate and store data from LoginRadius API: 

         from LoginRadius import LoginRadius
  
        login = LoginRadius(API_SECRET, Token)  
        profile = login.loginradius_get_data()

Note: Few providers like Twitter, LinkedIn, etc. doesn't provide email address with User Profile data, so you need to handle these cases in your callback page.

Live Demo
===
Please look at the 'demo project' in repository for the working demo.

SDK documentation
===
SDK documentation link for complete SDK functions: http://api.loginradius.com/python/


If you have any questions or need a further assistance please contact us at hello@loginradius.com.
