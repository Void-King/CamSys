import wxsent2user
wxid = 'o__Cr1Y4gVbFpJv18yUdHN7cr4RI'
atk = '20_wlkNlYV_iMeFv4_spgWXKYPJiGnanmA3yOyNdysMFzjMApuvzwt2vpBMaa12hQcF3rPHRmty1kYAodYi81hRbAzZNEb8MVLfsyPv9KSss22iIqKrGPYUTegzcfCke6wMWxSnmk5NiFMv6EyAMYRbAJAGSL'
pic = './output2.jpg'
vid = './output2.mp4'
pic2 = '2019.03.29.09.54.27.jpg'
pic3 = '2019.03.29.09.53.57.jpg'
msg = 'Face Detected!'
wxsent2user.setp2user(wxid, atk, pic3)
wxsent2user.setm2user(wxid, atk, msg)
wxsent2user.setp2user(wxid, atk, pic2)
x = input('asdf')
wxsent2user.setv2user(wxid, atk, pic, vid)