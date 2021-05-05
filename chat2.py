import tkinter as tk
import threading 
from socket import socket,AF_INET,SOCK_STREAM

class Chat:
	'''
	客户端类
	'''
	def __init__(self):
		window = tk.Tk()	#创建视窗
		window.title("Chat2")	#为视窗添加标题
		self.text = tk.Text(window)	#在视窗上添加文件区域
		self.text.pack()		#将文本区域作用到视窗
		'''在文本区域写入内容，这些文字会显示在视窗上
		参数有两个
		第一个是文本位置，tk.END 的值其实是字符串‘end’
		意为将文本内容显示在文本区域的最后位置
		第二个是文本内容
		'''
		self.text.insert(tk.END,('\t\t\t----------\n\t\t\t\t' 'Wecolme to Chat \n\t\t\t\t '
								   'Enjoy yourself \n\t\t\t\t----------------\n\n\n'))
		frame = tk.Frame(window)	#创建视窗容器
		frame.pack 		#将其做用到视窗上
		#在容器上创建标签
		label = tk.Label(frame,text="Enter your Message :")
		#定义一个字符串对象
		self.message = tk.StringVar()
		#在容器上定义文本输入框，参数为容器和字符串对象
		entry_area = tk.Entry(frame,textvariable=self.message)
		#在容器中定义一个发送信息按钮和一个连接服务器的按钮
		#参数分别为：容器对象，按钮名称,点击按钮后执行的函数，背景色
		send_button = tk.Button(frame,text="send",command=self.send_message,bg='#40E0D0')
		link_button = tk.Button(window,text="Link",command=self.link_chat,bg='#40E0D0')
		link_button.pack()
		#设置标签，文本输入框，按钮的坐标
		label.grid(row=1,column=1)
		entry_area.grid(row=1,column=2)
		send_button.grid(row=1,column=4)
		#启动视窗
		window.mainloop()

	#d点击‘send’按钮时执行的函数，
	def send_message(self):
 		#self.message	是字符串对象
 		#它的get 方法可以获取在输入框中输入的内容
		message = self.message.get()
		self.sock.send(message.encode())
		self.text.insert(tk.END,"[Your Message] {}\n".format(message))

	#点击“link”按钮时执行的函数
	def link_chat(self):
		#创建客户端套接字
		self.sock = socket(AF_INET,SOCK_STREAM)
		addr = ('localhost',11231)
		#向服务器发送连接请求
		self.sock.connect(addr)
		self.text.insert(tk_END,'Linked sucess\n')
		#创建子线程并启动
		thread = threading.Thread(target=self.handle)
		thread.start()

	#在线程内运行的函数
	def handle(self):
		while True:
			#阻塞运行，直到服务器发来消息
			message = self.sockrecv(1024).decode()
			#将消息打印到文本区域中
			self.text.insert(tk.END,'[Other\'s Message] {}\n'.format(message))

if __name__ == '__main__':
	Chat()
		
		
