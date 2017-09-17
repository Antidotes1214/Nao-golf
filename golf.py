#coding-utf8
import naoqi

class GeneratedClass:
    def __init__(self):
        pass

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.memory = ALProxy("ALMemory")
        self.redball = ALProxy("ALRedBallDetection")
        self.landmark = ALProxy("ALLandMarkDetection")
        self.tts = ALProxy("ALTextToSpeech")
        self.motion = ALProxy("ALMotion")
        self.posture = ALProxy("ALRobotPosture")
        self.camera = ALProxy("ALVideoDevice")
    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        #self.onStopped() #activate the output of the box
        import math
        import time
        import sys

        import Image
        self.motion.wakeUp()
        rnumber = 1
        self.camera.setActiveCamera(1)
        maxstepx = 0.04
        maxstepy = 0.14
        maxsteptheta = 0.4
        maxstepfrequency = 0.6
        stepheight = 0.02
        torsowx = 0.0
        torsowy = 0.0
        #机器人行走参数
        self.motion.setMoveArmsEnabled(False, False)

        '''self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(0.0,0.0,-math.pi/2,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])
        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(0.5,0.0,0.0,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])'''
        self.tts.say("我好想打高尔夫，能不能给我一个红球？")
        isenabled = True
        effectornamelist = ["HeadYaw"]
        timelist = [0.5]
        targetlist = [45*math.pi/180.0]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,True)
        time.sleep(3.5)
        effectornamelist = ["HeadYaw"]
        timelist = [0.5]
        targetlist = [-45*math.pi/180.0]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,False)
        time.sleep(3.5)
        effectornamelist = ["HeadYaw"]
        timelist = [0.5]
        targetlist = [-45*math.pi/180.0]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,True)
        time.sleep(3.5)
        effectornamelist = ["HeadYaw"]
        timelist = [0.5]
        targetlist = [45*math.pi/180.0]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,False)
        time.sleep(3.5)
        #机器人加载红球识别EVENT，然后左右摆头找红球



        memvalue = "redBallDetected"
        period = 1000
        self.redball.subscribe("Redball",period,0.0)

        for i in range(0,5):
            time.sleep(1.5)
            val = self.memory.getData(memvalue)
            if (val and isinstance(val,list) and len(val) >= 2):
                self.tts.say("哈哈!我看到了!")
                ballinfo = val[1]
                thetah = ballinfo[0]
                thetav = ballinfo[1]+(39.7*math.pi/180.0)
                print "thetah = ",thetah
                print thetav
                #机器人找到红球之后，获取红球的水平和垂直偏向角
                break
            else:
                self.tts.say("球在哪里呢?")


#motion.angleInterpolation(effectornamelist,targetlist2,timelist,isenabled)
        h = 0.478
        isenabled = False
        x = 0.0
        y = 0.0
        theta = thetah
        print "the first thetah = ",theta


        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(x,y,theta,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]]) #第一次，机器人转到正对红球的方向
        time.sleep(0.5)
        val = self.memory.getData(memvalue)
        ballinfo = val[1]
        thetah = ballinfo[0]
        thetav = ballinfo[1]+(39.7*math.pi/180.0)
        x = h/(math.tan(thetav)) - 0.2
        print "the first x = ",x
        theta = 0.0
        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(x,y,theta,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])
        print "dierci"
        #第二次，机器人走到距离红球20厘米的位置
        self.motion.waitUntilMoveIsFinished()
        effectornamelist = ["HeadPitch"]
        timelist = [0.5]
        targetlist = [30*math.pi/180.0]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,isenabled)
        val = self.memory.getData(memvalue)
        ballinfo = val[1]
        thetah = ballinfo[0]
        thetav = ballinfo[1]+(69.7*math.pi/180.0)
        print "The second thetah = ",thetah

        x = 0.0
        y = 0.0
        theta = thetah
        print theta
        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(x,y,theta,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])
        print "disanci"
        #第三次，机器人再次对准红球，进行修正
        time.sleep(1.5)
        val = self.memory.getData(memvalue)
        ballinfo = val[1]
        thetah = ballinfo[0]
        thetav = ballinfo[1]+(69.7*math.pi/180.0)
        x = (h-0.1)/(math.tan(thetav)) - 0.1

        theta = 0.0
        print " x = ",x
        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(x,y,theta,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])
        print "disici"
        #第四次，机器人走到距离红球10厘米的位置
        val = self.memory.getData(memvalue)
        ballinfo = val[1]
        thetah = ballinfo[0]
        thetav = ballinfo[1]+(69.7*math.pi/180.0)
        dx = (h-0.1)/(math.tan(thetav))
        print "the ball distance = ",dx

        #机器人对红球进行最终定位

#mark detection


        #self.posture.goToPosture("Stand",0.5)
        self.camera.setActiveCamera(0)
        memvalue1 = "LandmarkDetected"
        period = 700
        self.landmark.subscribe("Test_LandMark",period,0.0)
        effectornamelist = ["HeadPitch"]
        timelist = [0.5]
        targetlist = [0.0]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,True)
        #加载mark识别的EVENT
        for i in range(0,5):
            time.sleep(1.5)
            val = self.memory.getData(memvalue1)
            if (val and isinstance(val,list) and len(val) >= 2):
                self.tts.say("哈哈!我看到球洞了!")
                markinfo = val[1]
                shapeinfo = markinfo[0]
                rshapeinfo = shapeinfo[0]
                markid = shapeinfo[1]
                alpha = rshapeinfo[1]
                beta = rshapeinfo[2]
                sizex = rshapeinfo[3]
                sizey = rshapeinfo[4]
                heading = rshapeinfo[5]
                panduan = 0

                print "alpha =  ",alpha
                print "beta = ",beta,"sizex = ",sizex,"sizey = ",sizey,"heading",heading
                print "markid:",markid


                break
            else:
                self.tts.say("球洞在哪里呢?")
                effectornamelist = ["HeadYaw"]
                timelist = [0.5]
                targetlist = [math.pi/4]
                self.motion.angleInterpolation(effectornamelist,targetlist,timelist,isenabled)
                time.sleep(3.5)
                val = self.memory.getData(memvalue1)
                if (val and isinstance(val,list) and len(val) >= 2):
                    self.tts.say("哈哈!我看到球洞了!")
                    markinfo = val[1]
                    shapeinfo = markinfo[0]
                    rshapeinfo = shapeinfo[0]
                    markid = shapeinfo[1]
                    alpha = rshapeinfo[1]
                    beta = rshapeinfo[2]
                    sizex = rshapeinfo[3]
                    sizey = rshapeinfo[4]
                    heading = rshapeinfo[5]
                    panduan = 1
                    break
                else:
                    self.tts.say("球洞在哪里呢?")
                    effectornamelist = ["HeadYaw"]
                    timelist = [1.5]
                    targetlist = [-math.pi/4]
                    self.motion.angleInterpolation(effectornamelist,targetlist,timelist,True)
                    time.sleep(3.5)
                    val = self.memory.getData(memvalue1)
                    if (val and isinstance(val,list) and len(val) >= 2):
                        self.tts.say("哈哈!我看到球洞了!")
                        markinfo = val[1]
                        shapeinfo = markinfo[0]
                        rshapeinfo = shapeinfo[0]
                        markid = shapeinfo[1]
                        alpha = rshapeinfo[1]
                        beta = rshapeinfo[2]
                        sizex = rshapeinfo[3]
                        sizey = rshapeinfo[4]
                        heading = rshapeinfo[5]
                        panduan = 2
                        break
                    else:
                        self.tts.say("球洞在哪里呢?")
                        effectornamelist = ["HeadYaw"]
                        timelist = [1.5]
                        targetlist = [0.0]
                        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,True)
                        time.sleep(3.5)
                        panduan = 0
                        continue
                    #机器人对mark进行识别，如果前方没有mark，机器人会左右摆头45度寻找mark，直到找到为止


        r = 0.093/2
        #mark的半径，在场上需要根据实际情况调整
        h = 0.05
        #mark与机器人摄像头的高度差，在场上需要根据实际情况调整
        effectornamelist = ["HeadYaw"]
        timelist = [0.5]
        targetlist = [alpha]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,isenabled)
        #机器人的头转向mark
        time.sleep(1.5)
        val1 = self.memory.getData(memvalue1)
        #val1 = self.memory.getData(memvalue1)
        f=open(r'test.txt','w')
        f.close()
        markinfo1 = val1[1]
        print markinfo1
        print markinfo1
        shapeinfo1 = markinfo1[0]
        rshapeinfo1 = shapeinfo1[0]
        k = 0.0913
        size = rshapeinfo1[4]
        d1 = k/size
        #使用等比例法对mark进行测距
        print "the distance2 = ",d1
        if panduan ==1:
            alpha += math.pi/4
        elif panduan ==2:
            alpha -= math.pi/4
        else:
            alpha = alpha
        #获取mark的位置信息



# calculation


        theta3 = abs(thetah - alpha)
        dball = dx
        dmark = d1
        dbm2 = dx*dx + d1*d1 -2*dx*d1*math.cos(theta3)
        dbm = math.sqrt(dbm2)
        ctheta4 = (dball*dball + dbm2 - dmark*dmark)/(2*dball*dbm)
        theta4 = math.acos(ctheta4)
        #解三角形
        if thetah - alpha >= 0:
            if theta4 >= math.pi/2:
                theta = theta4 - math.pi/2
                y = dball*math.sin(theta4)

                #y = dball*math.cos(theta4)
                #y -= 0.1
            elif theta4 < math.pi/2:
                theta = math.pi/2 - theta4
                y = dball*math.sin(theta4)

                #y = dball*math.cos(theta4)
                #y -= 0.1
        elif theta4 >= math.pi/2:
            theta = 3*math.pi/2 - theta4
            y = -dball*math.sin(theta4)
            #y = dball*math.cos(theta4)
            #y -= 0.1
        else:
            theta = -math.pi/2 - theta4
            y = -dball*math.sin(theta4)
            #y = dball*math.cos(theta4)
            #y -= 0.1

        print "finalx = ",x,"finaly = ",y
        theta -= math.pi/2
        if abs(theta) > 3*math.pi/4:
            if theta >= 0:
                thetaz1 = theta - math.pi/2
                self.motion.setMoveArmsEnabled(False, False)
                self.motion.moveTo(0.0,0.0,math.pi/2,
                    [["MaxStepX",maxstepx],
                     ["MaxStepY",maxstepy],
                     ["MaxStepTheta",maxsteptheta],
                     ["MaxStepFrequency",maxstepfrequency],
                     ["StepHeight",stepheight],
                     ["TorsoWx",torsowx],
                     ["TorsoWy",torsowy]])
                self.motion.setMoveArmsEnabled(False, False)
                self.motion.moveTo(0.0,0.0,thetaz1,
                    [["MaxStepX",maxstepx],
                     ["MaxStepY",maxstepy],
                     ["MaxStepTheta",maxsteptheta],
                     ["MaxStepFrequency",maxstepfrequency],
                     ["StepHeight",stepheight],
                     ["TorsoWx",torsowx],
                     ["TorsoWy",torsowy]])
            else:
                thetaz1 = theta + math.pi/2
                self.motion.setMoveArmsEnabled(False, False)
                self.motion.moveTo(0.0,0.0,-math.pi/2,
                    [["MaxStepX",maxstepx],
                     ["MaxStepY",maxstepy],
                     ["MaxStepTheta",maxsteptheta],
                     ["MaxStepFrequency",maxstepfrequency],
                     ["StepHeight",stepheight],
                     ["TorsoWx",torsowx],
                     ["TorsoWy",torsowy]])
                self.motion.setMoveArmsEnabled(False, False)
                self.motion.moveTo(0.0,0.0,thetaz1,
                    [["MaxStepX",maxstepx],
                     ["MaxStepY",maxstepy],
                     ["MaxStepTheta",maxsteptheta],
                     ["MaxStepFrequency",maxstepfrequency],
                     ["StepHeight",stepheight],
                     ["TorsoWx",torsowx],
                     ["TorsoWy",torsowy]])

        #为减小误差，当转向角绝对值大于135度时，机器人将分两次进行转向
        else:


            self.motion.setMoveArmsEnabled(False, False)
            self.motion.moveTo(0.0,0.0,theta,
                [["MaxStepX",maxstepx],
                 ["MaxStepY",maxstepy],
                 ["MaxStepTheta",maxsteptheta],
                 ["MaxStepFrequency",maxstepfrequency],
                 ["StepHeight",stepheight],
                 ["TorsoWx",torsowx],
                 ["TorsoWy",torsowy]])
        time.sleep(1.0)
        #x -= 0.1
        y += 0.05
        #修正阈值，需要在场上根据实际情况进行调整
        '''self.motion.moveTo(x,0.0,0.0,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])'''
        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(0.0,y,0.0,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])
       #机器人，球，mark三点一线

#bizhang
        self.camera.setActiveCamera(1)
        effectornamelist = ["HeadPitch"]
        timelist = [0.5]
        targetlist = [-math.pi/9]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,True)

        resolution = 2    # VGA
        colorSpace = 11   # RGB


        videoClient = self.camera.subscribe("python_client", resolution, colorSpace, 5)
        naoImage = self.camera.getImageRemote(videoClient)
        self.camera.unsubscribe(videoClient)
        imageWidth = naoImage[0]
        imageHeight = naoImage[1]
        array = naoImage[6]

  # Create a PIL Image from our pixel array.
        im = Image.fromstring("RGB", (imageWidth, imageHeight), array)

  # Save the image.
        im.save("camImage.png", "PNG")
        im.show()

        img = im.convert('L')
        img.save("Image.png", "PNG")
        img.show()

        pixels = img.load()
        for x in range(imageWidth):
            for y in range(imageHeight):
                pixels[x,y] = 255 if pixels[x,y] >200 else 0

        img.save("Image.png", "PNG")

        pxl = img.load()

        count = 0
        num = 1
        flag = 0
        x = imageWidth/2
        for y in range(0,imageHeight-5):
            if pxl[x,y] == 255 and pxl[x,y+1] == 255 and pxl[x,y+2] == 255 and pxl[x,y+3] == 255 and pxl[x,y+4] == 255:
                if flag == 0:
                    count = num

                else:
                    count = count+1
                    flag = 0
                    num = count
            elif count >=1 and pxl[x,y] == 0 and pxl[x,y+1] == 0 and pxl[x,y+2]== 0 and pxl[x,y+3]==0 and pxl[x,y+4]== 0:
                flag = 1
        print count
        #使用图像识别白色障碍物和边线
        effectornamelist = ["HeadPitch"]
        timelist = [0.5]
        targetlist = [0.0]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,True)
        if count > 1 and dmark > 0.8:
            self.tts.say("有障碍物")
            theta = math.pi/6
            self.motion.setMoveArmsEnabled(False, False)
            self.motion.moveTo(0.0,0.0,theta,
                    [["MaxStepX",maxstepx],
                     ["MaxStepY",maxstepy],
                     ["MaxStepTheta",maxsteptheta],
                     ["MaxStepFrequency",maxstepfrequency],
                     ["StepHeight",stepheight],
                     ["TorsoWx",torsowx],
                     ["TorsoWy",torsowy]])
                    #偏转30度以使击出的球避开障碍物，在场上需要根据实际情况调整
        theta = math.pi/2
        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(0.0,0.0,theta,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])
        x = -0.2
        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(x,0.0,0.0,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])
        y = 1*dball*math.cos(theta4) - 0.1
        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(0.0,y,0.0,
            [["MaxStepX",maxstepx],
             ["MaxStepY",maxstepy],
             ["MaxStepTheta",maxsteptheta],
             ["MaxStepFrequency",maxstepfrequency],
             ["StepHeight",stepheight],
             ["TorsoWx",torsowx],
             ["TorsoWy",torsowy]])
            #机器人走到击球位置
        #self.posture.goToPosture("StandInit",0.5)
        effectornamelist = ["HeadYaw"]
        timelist = [0.5]
        targetlist = [0.0]
        self.motion.angleInterpolation(effectornamelist,targetlist,timelist,True)
        self.camera.setActiveCamera(1)
        time.sleep(2.0)
        self.tts.say("哈哈,我看到了")
        val = self.memory.getData(memvalue)
        ballinfo = val[1]

        thetav = ballinfo[1]+(39.7*math.pi/180.0)
        print "thetah = ",thetah
        x = -h/(math.tan(thetav)) + 0.1
        self.motion.setMoveArmsEnabled(False, False)
        self.motion.moveTo(x,0.0,0.0,
         [["MaxStepX",maxstepx],
          ["MaxStepY",maxstepy],
          ["MaxStepTheta",maxsteptheta],
          ["MaxStepFrequency",maxstepfrequency],
          ["StepHeight",stepheight],
          ["TorsoWx",torsowx],
          ["TorsoWy",torsowy]])
        #击球前进行最后修正



        self.onStopped()


    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
