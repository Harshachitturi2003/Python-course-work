data={'john@123.com':12223,
          'vinay234@.com':4545}
mail=input("Enter the mail :")
pwd=int(input("Enter the password:"))

if data.get(mail)==pwd:
    print("Valid Login")
else:
    print("Invalid Login")