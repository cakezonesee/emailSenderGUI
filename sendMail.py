# This project is to create GUI interface with tkinter for user to send email to predefined email address
# Where user have to put in their email address but in fact the email that use to send the email is not user's email
# but actually was sent by the predefined email address which mean user don't have to use their password and don't have to give permission to access their email
# the header of the email will be in the format --> {user's email address} - Subject: {subject}\n\n{email's body} instead

import tkinter as tk
from tkinter.font import Font
import smtplib


class mail:

    def __init__(self, window):

        self.window = window
        self.window.title('My email sender.')
 
        width = int(self.window.winfo_screenwidth() * 0.05)
        height = int(self.window.winfo_screenheight() * 0.02)

        # set font style
        bold_font = Font(family='Angsana new', size=16, weight='bold', slant='roman')

        # create widget where user write their email address
        self.sender = tk.Label(self.window, text='Your Email:', font=bold_font)
        self.sender.grid(row=0, column=0, sticky='e')
        self.sendEn = tk.Entry(self.window, width=50)
        self.sendEn.grid(row=0, column=1, sticky = 'w')

        # for subject
        self.subject = tk.Label(self.window, text='Subject:', font=bold_font)
        self.subject.grid(row=1, column=0, sticky='e')
        self.subEn = tk.Entry(self.window, width=50)
        self.subEn.grid(row=1, column=1, sticky = 'w')

        # for email body
        self.text = tk.Label(self.window, text='TEXT', font=bold_font)
        self.text.grid(row=2, column=0, sticky='e')
        self.sep_text = tk.Frame(self.window, height=2, bd=1, relief="sunken")
        self.sep_text.grid(row=2, column=1, sticky="ew")
        self.textEn = tk.Text(self.window, width= width, height= height, relief='groove', border=5)
        self.textEn.grid(row=3, column=0, columnspan=2)

        # for send button
        self.sendBu = tk.Button(self.window, text='SEND', font=bold_font, command=self.sendMail, width=15, relief='groove')
        self.sendBu.grid(row=4, column=1, sticky='e')

        # set row and column that will resize when window size is changed
        self.window.rowconfigure(3, weight=1)
        self.window.columnconfigure(1, weight=1)
       
       # bind resize event to window
        self.window.bind("<Configure>", self.on_resize)
      
       # set predefined current width and height of textEn box
        self.orig_width = self.textEn.winfo_width()
        self.orig_height = self.textEn.winfo_height()

    # Function to resize of self.textEn when the width and height of self.window is changed
    def on_resize(self, event):

        # find the scale factor to scale the resized width and height of textEn when window's size is changed
        width_scale = event.width / self.orig_width
        height_scale = event.height / self.orig_height
        scale_factor = min(width_scale, height_scale)
        
        # scale original size by factor
        width = int(self.orig_width * scale_factor)
        height = int(self.orig_height * scale_factor)

        # set new width and height of textEn
        self.textEn.config(width=width, height=height)

    def sendMail(self):
        
        # this is object for pop-up window
        global popUP

        # Define the sender, recipient, subject, and body of the email
        sender = self.sendEn.get()
        recipient = 'cakezonesee@gmail.com'
        subject = self.subEn.get()
        body = self.textEn.get(1.0, tk.END)

        # check if user enter their email address or not if not, the email will not be sent
        if sender != '':
            # Create the message headers
            message = f'Subject: {sender}\n\nSubject: {subject}\n\n{body}'

            # Connect to the SMTP server
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

                # Identify yourself to the SMTP server
                smtp.ehlo()

                # Start Transport Layer Security (TLS) encryption
                smtp.starttls()

                # Re-identify yourself as an encrypted connection
                smtp.ehlo()

                # Login to the SMTP server with your email account
                smtp.login('cakezonesee@gmail.com', 'iwjymxpzqsjsqdnw')
                # Send the email message
                smtp.sendmail(sender, recipient, message)

            self.sendEn.delete(0, 'end')
            self.subEn.delete(0, 'end')
            self.textEn.delete(1.0, tk.END)

            # create pop-up window to show if the email was sent successfully or not
            pop_font = Font(family='Angsana new', size=20, weight='bold', slant='italic')
            popUP = tk.Toplevel(self.window)
            popUP.title('Sending Result!!')
            self.popFrame = tk.Frame(popUP)
            self.popFrame.grid(row=0, column=0)
            self.popLabel = tk.Label(self.popFrame, text='Email was sent successfully!!', font=pop_font, fg='green')
            self.popLabel.grid(row=0, column=0, sticky='ew')

        # show pop-up window for when the email was not sent
        else:

            self.sendEn.delete(0, 'end')
            self.subEn.delete(0, 'end')
            self.textEn.delete(1.0, tk.END)

            pop_font = Font(family='Angsana new', size=20, weight='bold', slant='italic')
            popUP = tk.Toplevel(self.window)
            popUP.title('Sending Result!!')
            self.popFrame = tk.Frame(popUP)
            self.popFrame.grid(row=0, column=0)
            self.popLabel = tk.Label(self.popFrame, text='Something went wrong :(, check your email again please ^^', font=pop_font, fg='red')
            self.popLabel.grid(row=0, column=0, sticky='ew')


if __name__ == '__main__':
    window = tk.Tk()
    my_mail = mail(window)
    window.mainloop()