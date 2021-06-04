from kivy.app import App
from kivy.core.window import Window # allow for setting of window properties e.g. window color and size
from kivy.uix.widget import Widget
from kivy.clock import Clock # required for clock scheduling or repeat events
from datetime import datetime
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.text import LabelBase # custom font import and use
from kivy.utils import get_color_from_hex # use hex inplace of RGBA
from kivy.factory import Factory # enables for access of popup widget items

#todo remove multitouch on Desktop Environments


# Define the different Type of Windows
class LandingPage(Screen):
    # todo: implement a yes/no popup
    pass
class EmployeeLogin(Screen):
    pass



class ProfileWindow(Screen):
    pass

class WindowManager(ScreenManager):
    def login(self):
        print("hello")
        return True 



# defining the design file 
design_file = Builder.load_file('window.kv')
class MyApp(App):
########## Time update #############
    def on_start(self):
        Clock.schedule_interval(self.update,1)

    def update(self,nap):
        self.date= datetime.now().strftime('%d %B, %Y')
        self.time = datetime.now().strftime('%I:%M:%S')
        self.root.get_screen('landingpage').ids.timestamp.text = self.date+' '+self.time
##########3 time End ###############

############# Popup hook for pinpad ##############3
    
    #instantiating popup class object 
    login_popup = Factory.MyPopup()
    exit_popup = Factory.ExitPopup()
    def open_exit_dialog(self):
        self.exit_popup.open()
    
    def open_popup(self):
        self.login_popup.open()
    def close_popup(self):
        self.login_popup.ids.calc_input.text = 'Enter Pin'
        self.login_popup.dismiss()

    def program_exit(self):
        quit()

    def close_exit_popup(self):
        self.exit_popup.dismiss()

    ############# POPUP INPUT PAD FUNCTION DEFINITIONS ###############

    def hello_on(self):
        self.login_popup.ids['backspace_button'].background_color  = (0,0,0,.55555)
        self.login_popup.ids.my_image.source = 'icons/backspace_normal.png'
    def hello_off(self):
        self.login_popup.ids['backspace_button'].background_color  = (0.7,0.7,0.7,1)
        self.login_popup.ids.my_image.source = 'icons/backspace_down.png'

    def ok_on(self):
        self.login_popup.ids['submit'].background_color  = (0,0,0,.55555)
    def ok_off(self):
        self.login_popup.ids['submit'].background_color  = (0.7,0.7,0.7,1)

    def backspace(self):
        self.hello_on()
        prior = self.login_popup.ids.calc_input.text
        if prior == 'Enter Pin':
            pass
        else:

            if prior == '':
                prior = 'Enter Pin'
                self.login_popup.ids.clear = "BACK"
            else:
                prior = prior[:-1]

            if prior == '':
                prior = 'Enter Pin'
            self.login_popup.ids.calc_input.text = prior
    def button_press(self,button):
        #create a variable to hold prior text values
        prior = self.login_popup.ids.calc_input.text


        if prior == 'Error':
            self.login_popup.ids.calc_input.text = 'Enter Pin'
            self.login_popup.ids.calc_input.text ='{button}'.format(button=button)

        elif prior == 'Enter Pin':
            self.login_popup.ids.calc_input.text = ''
            self.login_popup.ids.calc_input.text = '{button}'.format(button=button)


        else:
            self.login_popup.ids.calc_input.text = '{prior}{button}'.format(prior=prior,button=button)


    def clear_all(self):
        self.login_popup.ids.calc_input.text = '0'


    def equals(self):
        prior = self.login_popup.ids.calc_input.text
        self.ok_on()

        # Error handling for divide by zero


        try:
            # Evaluate Math operations
            # todo: Employ eval security measures
            answer = eval(prior)

            # Output the answer on-screen
            self.login_popup.ids.calc_input.text = str(answer)
        except :
            self.login_popup.ids.calc_input.text = "Error"

######################### End of Popup Funcdefs #########3

    def build(self):
        return design_file

if __name__ == '__main__':
    # Clearing Window Color
    Window.clearcolor = get_color_from_hex('#101216')
    
    #Defining the Robot font_family import from directory
    LabelBase.register(name='Roboto',
            fn_regular='roboto/Roboto-Thin.ttf',
            fn_bold='roboto/Roboto-Medium.ttf')

    MyApp().run()



