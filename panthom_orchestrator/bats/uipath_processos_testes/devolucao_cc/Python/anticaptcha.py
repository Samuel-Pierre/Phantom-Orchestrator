#pip3 install anticaptchaofficial

from anticaptchaofficial.imagecaptcha import *

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("2da6ec885521f59da0faf34312f5059b")

def Captcha():
    captcha_text = solver.solve_and_return_solution("C:\\SVNRobo\\desenvolvimento\\tahto\\proativo\\credito\\futuro\\image\\captcha.png")
    if captcha_text != 0:
        #print ("captcha text : "+captcha_text)
        return captcha_text
    else:
        #print ("task finished with error : "+solver.error_code)
        return "task finished with error : "+solver.error_code