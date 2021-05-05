import tkinter as tk 
import threading 
from socket import socket,AF_INET,SOCK_STREAM

class Chat:
	'''服务器类
	'''
	def __init__(self):
		#创建服务器套接字并监听在11231端口，等待客户端发起连接
		self.sock = socket(AF_INET,SOCK_STREAM)
		self.sock.bind(('localhost',11231))
		self.sock.listen()
		self.extension_sock = None	#该属性在客户端连接成功后为临时套接字
		window = tk.Tk()	#创建视窗
		window.title("Chat1")#为视窗添加标题
		self.text = tk.Text(window)	#在视窗添加文本区
		self.text.pack()		#将文本区域作用到视窗
		'''在文本区域写入内容，这些文字会显示在视窗上
			参数有两个
			第一个是文本位置，tk.END 的值就是'end'
			即文本内容显示在文本区域的最后位置
			第二个是文本内容
		'''
		self.text.insert(tk.END,('\t\t\t\t--------------\n\t\t\t\t' 
								'Wecolme to Chat \n\t\t\t'
								'Enjoy youself \n\t\t\t\t-------------\n\n\n'))
		self.text.insert(tk.END,"[NO PERSON] Waiting for someone\n")
		frame = tk.Frame(window)	#创建视窗容器
		frame.pack()	#将其作用到视窗上
		#在容器上创建标签
		label = tk.Label(frame,text="Enter your Message:")
		#定义一个字符串对象
		self.message = tk.StringVar()
		#在容器上定义文本输入框，参数为容器和字符串对象
		entry_area = tk.Entry(frame,textvariable = self.message)
		#在容器中定义一个发送消息的按钮
		#参数分别为：容器对象，按钮名称，点击按钮后执行的函数，背景色
		send_button = tk.Button(frame,text='Send',command=self.send_message,bg='#40E0D0')
		#设置标签，文本输入框，按钮的坐标
		label.grid(row=1,column=1)
		entry_area.grid(row=1,column=2)
		send_button.grid(row=1,column=4)
		#创建子线程并启动
		thread = threading.Thread(target=self.handle)
		thread.start()
		#启动视窗
		window.mainloop()
		
		#点击Send  按钮后执行的操作
	def send_message(self):
		#获取输入框的内容
		message = self.message.get()
		#该属性默认值为 None ，收到客户端的连接后，该属性值为临时套接字
		if self.extension_sock:
			self.extension_sock.send(message.encode())
		#将输入框的内容打印到文本区域
		self.text.insert(tk.END,'[Your Message] {} \n'.format(message))
		#子线程内运行的函数
	def handle(self):
		#该步骤为阻塞运行，直到有客户端发来连接请求
		extension_sock, addr = self.sock.accept()
		#将临时套接字赋值给该实例属性
		self.extension_sock = extension_sock
		while True:
			#套接字的 recv 方法也是阻塞运行，直到客户端发来数据
			message = extension_sock.recv(1024).decode()
			#将客户端发来的数据打印到文本区域
			self.text.insert(tk.END,'[Other\'s Message] {} \n'.format(message))

if __name__ =='__main__':
		Chat()
