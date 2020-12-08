from flask import Flask, render_template
import os
import sys
import webbrowser

#os.system('chromium-browser %U')

class Finder:
    def __init__(self, *args, **kwargs):
        self.server_name = kwargs['server_name']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}

    def run(self):
        command = """sudo iwlist wlan0 scan | grep -ioE 'ssid:"(.*{})'"""
        result = os.popen(command.format(self.server_name))
        result = list(result)

        if "Device or resource busy" in result:
            return None
        else:
            ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
            print("Successfully get ssids {}".format(str(ssid_list)))

        for name in ssid_list:
            try:
                result = self.connection(name)
            except Exception as exp:
                print("Couldn't connect to name : {}. {}".format(name, exp))
            else:
                if result:
                    print("Successfully connected to {}".format(name))

    def connection(self, name):
        try:
            os.system("nmcli d wifi connect {} password {} iface {}".format(name, self.password, self.interface_name))
        except:
            raise
        else:
            return True


app = Flask(__name__)

@app.route('/')
def front():
    pw = sys.argv[1]
    return render_template('front.html', password=pw)


@app.route('/back')
def back():
	server_name= "Li-Pass"	
	pw = sys.argv[1]
	interface_name = "wlan0"
	f = Finder(server_name=server_name, password=pw, interface=interface_name)
	f.run()
	return render_template('back.html', password=pw)

app.run(port=8080, debug=True)

	


