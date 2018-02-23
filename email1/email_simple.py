import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.utils import parseaddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


my_sender = '1016255338@qq.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user = 'darren3raffey@outlook.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
my_psw = "lypjrckrgeavbdja"

def email(str_s, picture_name):
     ret = True
     try:
          print(1)
          msg = MIMEMultipart()
          msg.attach(MIMEText(str_s,'html','utf-8'))
          msg['From'] = formataddr(["luotianyi02",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
          msg['To'] = formataddr(["loser",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
          msg['Subject'] = "python提示" #邮件的主题，也可以说是标题
          with open('%s.png'%picture_name, 'rb') as f:
              # 设置附件的MIME和文件名，这里是png类型:
              mime = MIMEBase('image', 'png', filename='test.png')
              # 加上必要的头信息:
              mime.add_header('Content-Disposition', 'attachment', filename='test.png')
              mime.add_header('Content-ID', '<0>')
              mime.add_header('X-Attachment-Id', '0')
              # 把附件的内容读进来:
              mime.set_payload(f.read())
              # 用Base64编码:
              encoders.encode_base64(mime)
              # 添加到MIMEMultipart:
              msg.attach(mime)
          server = smtplib.SMTP_SSL("smtp.qq.com", 465)  #发件人邮箱中的SMTP服务器，端口是25    rddbxyjtgqsnbbfg
          print(2)
          server.login(my_sender, my_psw)    #括号中对应的是发件人邮箱账号、邮箱密码mtkdkuhwdpfhbcah   lypjrckrgeavbdja
          print(3)
          server.sendmail(my_sender, [my_user,], msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
          server.quit()   #这句是关闭连接的意思
                                                                      #except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
     except smtplib.SMTPException as e:
          print("Falied,%s"%e )
          ret=False  
     if ret:
          print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
     else:
          print("filed")  #如果发送失败则会返回filed

def sendemail(picture_name,run_log):
     html ="""
<html> 
<head>返回状态</head> 
<body>
<p style="line-height:0.9"> <br>..I.<br>\&nbsp;&nbsp;&nbsp;)<br>&nbsp;|&nbsp;|<br>run_log :</p>
<p>%s</p> <!-- log -->
<p><img src="cid:0"></br></p>  <!-- 图片-->
</body> 
</html> 
"""%run_log
     email(html,picture_name)

if __name__ == '__main__':
     print('这是测试________________________________________________')
     # sendemail('test','test code 测试代码')
     




