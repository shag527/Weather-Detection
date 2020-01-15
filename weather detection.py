import tkinter as tk
import requests

HEIGHT = 700
WIDTH = 800
root=tk.Tk()

def format_response(weather):
	try:
		name=weather['name']
		desc=(weather['weather'][0]['description'])
		icon=(weather['weather'][0]['icon'])
		temp=(weather['main']['temp'])
		pressure=(weather['main']['pressure'])
		humidity=(weather['main']['humidity'])
		wind_speed=(weather['wind']['speed'])
		final_str='City       : %s\nConditions : %s\nTemperature: %s(F)\nPressure   : %s(mb)\nHumidity   : %s(Percent) \nWind Speed : %s(m/s)'%(name,desc,temp,pressure,humidity,wind_speed)
	except:
		final_str='There was a problem retrieving \ninformation'
	return final_str

def get_weather(entry):
	weather_key='650d738f9c92b5791bd3405e1d6c92c7'
	url='https://api.openweathermap.org/data/2.5/weather'
	params={'APPID':weather_key,'q':entry,'units':'imperial'}
	response=requests.get(url,params=params,verify=False)
	weather=response.json()
	label['text']=format_response(weather)


canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

back_img=tk.PhotoImage(file='landscape3.png')

back_label=tk.Label(root,image=back_img)
back_label.place(relwidth=1,relheight=1)

frame=tk.Frame(root, bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.65,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=('Courier',20))
entry.place(relwidth=0.67,relheight=1)

button=tk.Button(frame,text='Search',font=('Courier',16),command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame=tk.Frame(root,bg='#80c1ff',bd=5)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.5,relheight=0.35,anchor='n')

label=tk.Label(lower_frame,bg='white',font=('Consolas',17),anchor='nw',justify='left',bd=4)
label.place(relwidth=1,relheight=1)

root.mainloop()



















