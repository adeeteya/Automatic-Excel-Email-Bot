import smtplib, ssl, openpyxl,getpass#If you are using a mac then you should install the "certifi" module.
port = 587  #This port works for Gmail,for different mail services you might need a different port.
file=open("config.txt",'r')
temp=file.readline()
smtp_server=temp[12:len(temp)-1]#Smpt service taken from the config file.
temp=file.readline()
sender_email=temp[9:len(temp)-1]#You Could Change the Email Address in the config file.
print("Email id:",sender_email)
password=getpass.getpass("Password:")#User inputs the pasword here, the password wont be visible in the terminal.
temp=file.readline()
wb=openpyxl.load_workbook(temp[10:len(temp)-1])#The Name of the Excel Document,also it should be in the same directory as the program.
temp=file.readline()
file.close()
sheet=wb.get_sheet_by_name(temp[11:len(temp)-1])#The Name of the Sheet where the data is present.
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    for i in range(2,(sheet.max_row+1)):#The Range of values present in the excel sheet.
         message = """\
Subject:Marks

Name              Marks
"""#The message and Subject can be changed according to the user's needs.
         s='A'+str(i);s1='B'+str(i);s2='C'+str(i)#Strings are initialised according to the cell's names.
         receiver_email=str(sheet[s1].value)#Contains The Receiver's email address.
         message+=str(sheet[s].value)+"              "+str(sheet[s2].value)#Contains the message to be sent as an e-mail.
         server.sendmail(sender_email,receiver_email,message)
print("The Emails have been sent successfully.")
