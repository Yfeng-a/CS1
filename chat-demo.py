import tkinter as tk

class Chat:
	
	def __init__(self):
		window = tk.Tk()	#创建视窗
		window.title("Chat")	#为视窗添加标题
		self.text = tk.Text(window) #在视窗上添加文本区域
		self.text.pack()	#将文本区域作用于视窗
		'''
		在文本区域写入内容，这些文字会显示在视窗上
		参数有两个
		第一个是文本位置，tk.END 的值其实就是字符串‘send‘
		意为将文本内容显示在文本区域最后位置
		第二个是文本内容
		'''
		self.text.insert(tk.END,('\t\t\t\t-----------------------------\n\t\t\t\t' 
									'Wecome to Chat \n\t\t\t\t'  
									'Enjoy youself \n\t\t\t\t-----------------\n\n\n'))
		frame = tk.Frame(window) 	#创建视窗容器
		frame.pack()	#将其应用到视窗上
		#在容器上创建标签
		label = tk.Label(frame,text="Enter your Messgge:")
		#定义一个字符串对象
		self.message = tk.StringVar()
		#在容器上定义文本输入框，参数为容器和字符串对象
		entry_area = tk.Entry(frame,textvariable=self.message)
		#在容器中定义一个发送信息的按钮
		#参数分别为：容器对象，按钮名称，点击按钮后执行的函数，背景色
		send_button = tk.Button(frame,text="Send",command=self.send_button,bg='#40E0D0')
		#设置标签文本输入框，按钮的坐标
		label.grid(row=1,column=1)
		entry_area.grid(row=1,column=2)	
		send_button.grid(row=1,column=4)
		#启动视窗
		window.mainloop()
		
		#点击send按钮时执行的函数
	def send_button(self):
		#self.massage 是字符串对象
		#它的 get 方法可以获取在输入框中输入的内容
		message = self.message.get()
		self.text.insert(tk.END,"[Your Message] {}\n".format(message))

if __name__=='__main__':
	Chat()
