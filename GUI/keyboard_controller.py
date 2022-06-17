import rclpy

from rclpy.node import Node

from std_msgs.msg import String

import time

from pynput import keyboard

import getpass

from tkinter import *

import getpass





class Feature2(Node):



	def Forward(self):

		msg = String()

		msg.data = "MOVEF:1000"

		self.publisher.publish(msg)

		print("Forward")

	def Backward(self):

		msg = String()

		msg.data = "MOVEB:1000"

		self.publisher.publish(msg)

		print("Backward")



	def Leftward(self):

		msg = String()

		msg.data = "TURNL:0200"

		self.publisher.publish(msg)

		print("Leftward")



	def Rightward(self):

		msg = String()

		msg.data = "TURNR:0200"

		self.publisher.publish(msg)

		print("Rightward")







	def Stop(self):

		msg = String()

		msg.data = "STOPR:0000"

		self.publisher.publish(msg)

		print("Stop")





	def __init__(self):

		super().__init__('Feature2')

		self.publisher = self.create_publisher(String, '/robot/control', 10)

		self.subscription = self.create_subscription(String,'/robot/right',self.listener_callback,10)

		self.subscription

		



	def listener_callback(self, msg):

		win_1 = Tk()

		win_1.title("Controls")

		win_1.config(bg= "#828481")

		distance = Label(win_1,text = msg.data)

		distance.place(x=100, y=100)

		win_1.mainloop()

		print("Forward")

		print(msg.data)

		if int(msg.data[:-2]) < 10:

			message = String()

			message.data = "TURNR:0100"

			self.publisher.publish(message)

			print("Right")

			

		else:

			msg_1 = String()

			msg_1.data = "MOVEF:1000"

			self.publisher.publish(msg_1)

		time.sleep(5)

		



def main(args=None):

    rclpy.init(args=args)

    virtual_keyboard = Feature2()

    win = Tk()

    win.title("ZUMO ROBOT")

    win.config(bg= "white")

    

    def moveForward():

        Feature2().Forward()



    def moveBackward():

        Feature2().Backward()



    def moveLeft():

        Feature2().Leftward()



    def moveRight():

        Feature2().Rightward()



    def stop():

        Feature2().Stop()



    def dis():

    	rclpy.spin(virtual_keyboard)





    input1 = StringVar()

    

    	

    def speed_input():

    	user_input = textInput.get()

    	global spd

    	spd = user_input

    	



    control_frame = Frame(win, width = 200, height = 200, bg= "white", highlightthickness=2, highlightbackground="white") 

    control_frame.grid()

    btnframe = Frame(control_frame, width = 150, height = 150, bg="white")

    btnframe.grid()

    name = Label(btnframe, width=12, height = 1, text = "GUI ", font = "bold", bg = "#037481")

    name.grid(row = 0, column=2)

    textInput = Entry(btnframe, bd = 10, textvariable = input1, bg = "black",foreground = "green")

    textInput.grid(row = 6, column=5)

    speedTitle = Label(btnframe, text = "Please enter the speed",bg = "#037481")

    speedTitle.grid(row = 5, column=5)

    speed_fix = Button(btnframe, text = "Speed", command = speed_input, bg = "grey")

    speed_fix.grid(row = 6, column=2)

    up_control = Button(btnframe, text = "UP", command = moveForward, bg = "yellow")

    up_control.grid(row=2, column=2 ,padx=5 , pady=5)

    down_control = Button(btnframe, text = "BACK", bg="yellow", command = moveBackward)

    down_control.grid(row=4, column=2 ,padx=5 , pady=5)

    right_control = Button(btnframe, text = "RIGHT", bg="yellow", command = moveRight)

    right_control.grid(row=3, column=3 ,padx=5 , pady=5)

    left_control = Button(btnframe, text = "LEFT", bg="yellow", command = moveLeft)

    left_control.grid(row=3, column=0 ,padx=5 , pady=5)

    stop_control = Button(btnframe, text = "STOP", bg="red", command = stop)

    stop_control.grid(row=17, column=0 ,padx=5 , pady=5)

    automatic = Button(btnframe, text = "automatic mode", command = dis, bg = "grey")

    automatic.grid(row=5, column=2 ,padx=5 , pady=5)

    left_control.grid(row=3, column=0 ,padx=5 , pady=5)

    win.mainloop()

    virtual_keyboard.destroy_node()

    

    rclpy.shutdown()



if __name__ == '__main__':

    	main()