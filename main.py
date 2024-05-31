import google.generativeai as genai
print(dir(genai))

class NLPModel:
    def get_model(self):
        genai.configure(api_key="AIzaSyBfeE0VaE8O2JhZjPDkFWjt83XP_1yrhos")
        model = genai.GenerativeModel("gemini-pro")
        return model


class NLPApp(NLPModel):
    def __init__(self):
        self.__database = {}
        self.__first_menu()

    def __first_menu(self):
        first_input = input("""
        Hi, how would you like to proceed?
        1. Not a memer ? Register
        2. Already a member ? Sign in
        3. Exit              
        """)

        if first_input =='1':
            #Register
            self.__register()
            self.__first_menu()
        
        elif first_input=='2':
            #login
            self.__login()

        else:
            exit()

    def __second_menu(self):
        second_input = input("""
        What would you like to know today?
        1. Sentiment Analysis
        2. Language Translation
        3. Languagae Detection                                                  
        """)

        if second_input == '1':
            #Sentiment Analysis
            self.__sentiment_analysis()

        elif second_input == '2':
            # language translation
            self.__language_translation()

        elif second_input == '3':
            #language detection
            self.__language_detection()

        else:
            exit()

    def __register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter the password: ")

        if email in self.__database:
            print("Email already exists")

        else:
            self.__database[email]=[name,password]
            print("Registeration successful")
            self.__first_menu()

    def __login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        if email in self.__database:
            if password == self.__database[email][1]:
                print("login successful")
                self.__second_menu()
            else:
                print("The details you entered does not match our records. Please try again")
                self.__login()

            
        else:
            print("The email you entered is not registered")
            self.__first_menu()

    def __sentiment_analysis(self):
        user_input = input("Enter your text")
        model = super().get_model()
        response = model.generate_content(f"give me the sentiment of this text: {user_input}")
        result = response.text
        print(result)
        self.__second_menu()

    def __language_translation(self):
        user_input = input("Enter your text")
        model = NLPModel.get_model(self)
        response = model.generate_content(f"give me hindi translation of this sentence: {user_input}")
        result = response.text
        print(result)
        self.__second_menu()

    def __language_detection(self):
        user_input = input ("Enter your text")
        model = super().get_model()
        response = model.generate_content(f"give me the language used in this sentence: {user_input}")
        result = response.text
        print(result)
        self.__second_menu()




obj = NLPApp()


