
import turtle as te

WriteSteps = 10  
Speed = 10          # Sampling times of Bezier function
Xh, Yh = 0, 0       # Record the handle of the previous Bessel function
te.pensize(4)
te.speed(Speed)
te.tracer(10)

def move_to(point):
    te.penup()
    te.goto(point)
    te.pendown()

def bezier_point(points, timestep, dimension=2):
    degree = len(points) - 1
    if(degree == 0):
        return points[0]
    else:
        new_points = []
        for idx in range(degree):
            temp = []
            for d in range(dimension):
                temp.append(points[idx][d] * (1.0 - timestep) +
                            points[idx + 1][d] * timestep)
            new_points.append(tuple(temp))
        return bezier_point(tuple(new_points), timestep, dimension)


def bezier_curve(points, dimension=None):
    if(dimension is None):
        dimension = len(points[0])

    move_to(points[0])
    for timestep in range(0, WriteSteps + 1):
        p = bezier_point(points, timestep / WriteSteps, dimension)
        te.goto(p)
    te.penup()


def bezier_curve_through(points, relative: bool = False):
    global Xh
    global Yh
    curr = te.position()
    points = list(points)
    if(relative):
        for i in range(len(points)):
           points[i] = tuple([c1 + c2 for c1, c2 in zip(points[i], curr)])
           print(points[i])
    points.insert(0, curr)
    bezier_curve(tuple(points))
    Xh = points[-1][0] - points[-2][0]
    Yh = points[-1][1] - points[-2][1]



def smooth_bezier_curve(points, relative: bool = False):
    global Xh
    global Yh
    points = list(points)
    points.insert(0, (Xh + te.position()[0], Yh + te.position()[1]))
    if(relative):
        points[0] = (points[0][0] - te.position()[0],
                     points[0][1] - te.position()[1])
    bezier_curve_through(tuple(points), relative)


def line_between(source, destination):
    move_to(source)
    te.pendown()
    te.goto(destination)

def main():
    """
    Layer 1
    """
    ############ Head With Ears ###############
    te.fillcolor("#F6D02F")
    move_to((84.0,38.0))
    te.begin_fill()
    smooth_bezier_curve(((107,61),(118,97),(114,134),(102,161),(77,188),(62,199)))
    move_to((70,191))
    smooth_bezier_curve(((100,200),(137,215),(175,242),(207,277),(216,297)))
    smooth_bezier_curve(((216,297),(174,292),(140,281),(106,267),(68,243)))
    move_to((70,244))
    smooth_bezier_curve(((56,229),(39,224),(36,221)))
    smooth_bezier_curve(((33,222),(10,232),(-17,238),(-46,240),(-76,231),(-100,220),(-116.0,207.0)))
    move_to((-116.0,207.0))
    smooth_bezier_curve(((-115.0,208.0),(-139.0,203.0),(-159.0,195.0),(-185.0,184.0),(-212.0,162.0),(-233.0,142.0),(-255.0,115.0),(-272.0,88.0),(-280.0,75.0)))
    smooth_bezier_curve(((-278.0,76.0),(-256.0,80.0),(-236.0,91.0),(-217.0,101.0),(-196.0,116.0),(-177.0,129.0),(-159.0,144.0),(-141.0,158.0)))
    smooth_bezier_curve(((-142.0,157.0),(-147.0,147.0),(-152.0,133.0),(-154.0,108.0),(-149.0,81.0),(-142.0,63.0),(-135.0,45.0),(-116.0,25.0),(-102.0,17.0),(-96.0,15.0)))


    ###################################### Right Hand ########################################3
    move_to((-107.0,24.0))
    smooth_bezier_curve(((-107.0,24.0),(-118.0,16.0),
    (-129.0,9.0),(-153.0,-4.0),(-177.0,-20.0),(-197.0,-36.0),
    (-203.0,-45.0),(-211.0,-53.0),(-217.0,-60.0),(-223.0,-65.0))) 
    #hand
    te.pendown()
    te.seth(200)
    te.fd(10)
    te.seth(280)
    te.fd(7)
    te.seth(210)
    te.fd(10)
    te.seth(300)
    te.circle(10, 80)
    te.seth(220)
    te.fd(10)
    te.seth(300)
    te.circle(10, 80)
    te.seth(240)
    te.fd(12)
    te.seth(0)
    te.fd(13)
    te.seth(240)
    te.circle(10, 70)
    te.seth(10)
    te.circle(10, 70)
    smooth_bezier_curve(((-204.0,-108.0),(-195.0,-106.0),(-174.0,-101.0),
    (-157.0,-95.0),(-141.0,-90.0),(-127.0,-83.0),(-120.0,-80.0)))
    smooth_bezier_curve(((-120.0,-78.0),(-116.0,-68.0),(-113.0,-55.0),
    (-111.0,-41.0),(-107.0,-21.0),(-105.0,-11.0)))
    
    
    ##############################  Left leg and Left Body ###############################333333333
    move_to((-117.0,-79.0))
    smooth_bezier_curve(((-117.0,-82.0),(-123.0,-94.0),(-126.0,-103.0),
    (-131.0,-120.0),(-134.0,-136.0),(-139.0,-156.0),(-139.0,-166.0),
    (-139.0,-172.0),(-138.0,-178.0),(-134.0,-190.0),(-131.0,-199.0),(-126.0,-214.0),
    (-122.0,-226.0),(-115.0,-234.0),(-115.0,-235.0),(-111.0,-239.0),(-107.0,-246.0)))
    move_to((-112.0,-237.0))
    smooth_bezier_curve(((-127.0,-253.0),(-140.0,-267.0),(-155.0,-288.0),(-163.0,-301.0),(-159.0,-310.0)))
    te.pendown()
    te.seth(60)
    te.circle(-100, 20)
    te.left(180)
    te.circle(100, 20)
    te.seth(300)
    te.circle(10, 70)
    te.seth(60)
    te.circle(-100, 20)
    te.left(180)
    te.circle(100, 20)
    te.seth(10)
    te.circle(100, 60)
    te.seth(180)
    te.circle(-100, 10)
    te.left(180)
    te.circle(100, 10)
    te.seth(5)
    te.circle(100, 10)
    te.circle(-100, 40)
    te.circle(100, 35)
    te.left(180)
    te.circle(-100, 10)

    ############################## Right Leg, Right Body, Right Hand #########################################3
    move_to((67.0,-262.0))
    te.seth(290)
    te.circle(100, 55)
    te.circle(10, 50)
    te.seth(120)
    te.circle(100, 20)
    te.left(180)
    te.circle(-100, 20)
    te.seth(0)
    te.circle(10, 50)
    te.seth(110)
    te.circle(100, 20)
    te.left(180)
    te.circle(-100, 20)
    te.seth(30)
    te.circle(20, 50)
    te.seth(100)
    te.circle(90, 40)
    move_to((123.0,-256.0))
    smooth_bezier_curve(((123.0,-256.0),(130.0,-252.0),(138.0,-238.0),
    (148.0,-220.0),(151.0,-200.0),(153.0,-172.0),(149.0,-156.0),(139.0,-138.0),
    (132.0,-122.0),(127.0,-100.0),(122.0,-81.0),(120.0,-64.0),(117.0,-46.0),(117.0,-24.0)))
    move_to((118.0,-34.0))
    te.pendown()
    te.seth(43)
    te.circle(200, 60)
    te.right(10)
    te.fd(10)
    te.circle(5, 160)
    te.seth(90)
    te.circle(5, 160)
    
    te.seth(90)
    te.fd(10)
    te.seth(90)
    te.circle(5, 180)
    te.fd(10)
    te.left(180)
    te.left(20)
    te.fd(10)
    te.circle(5, 170)
    te.fd(10)
    te.seth(240)
    te.circle(50, 30)
    smooth_bezier_curve(((131.0,121.0),(127.0,111.0),(123.0,99.0),
    (118.0,88.0),(112.0,75.0),(102.0,62.0),(98.0,58.0)))
    te.end_fill()
    move_to((174.0,166.0))
    te.seth(-90)
    te.fd(3)
    te.circle(-4, 180)
    te.fd(3)
    te.seth(-90)
    te.fd(3)
    te.circle(-4, 180)
    te.fd(3)
    move_to((138.0,163.0))
    te.seth(-20)
    te.fd(5)
    te.circle(-5, 160)
    te.fd(5)

    ####################### Tail ###################################
    move_to((138.0,-134.0))
    te.fillcolor("#F6D02F")
    te.begin_fill()
    line_between((138.0,-134.0),(167.0,-117.0))
    line_between((167.0,-117.0),(127.0,-57.0))
    line_between((127.0,-57.0),(201.0,-16.0))
    line_between((201.0,-16.0),(163.0,30.0))
    move_to((163.0,30.0))
    smooth_bezier_curve(((163.0,30.0),(170.0,48.0),(176.0,67.0),(179.0,80.0),
    (180.0,105.0),(180.0,132.0),(177.0,151.0),(176.0,158.0)))
    move_to((176.0,158.0))
    line_between((176.0,158.0),(313.0,255.0))
    line_between((313.0,255.0),(351.0,108.0))
    line_between((351.0,108.0),(256.0,50.0))
    line_between((256.0,50.0),(291.0,-22.0))
    line_between((291.0,-22.0),(201.0,-78.0))
    line_between((201.0,-78.0),(223.0,-125.0))
    line_between((223.0,-125.0),(167.0,-155.0))
    line_between((167.0,-155.0),(173.0,-174.0))
    line_between((173.0,-174.0),(144.0,-181.0))
    te.end_fill()

    ################### Brown Pactch In Tail ######################
    te.fillcolor('#923E24')
    te.begin_fill()
    move_to((138.0,-134.0))
    line_between((138.0,-134.0),(167.0,-117.0))
    line_between((167.0,-117.0),(150.0,-90.0))
    te.pencolor('#923e24')
    line_between((150.0,-90.0),(170.0,-100.0))
    line_between((170.0,-100.0),(168.0,-82.0))
    line_between((168.0,-82.0),(181.0,-96.0))
    line_between((181.0,-96.0),(185.0,-78.0))
    line_between((185.0,-78.0),(197.0,-91.0))
    line_between((197.0,-91.0),(201.0,-78.0))
    te.pencolor("black")
    line_between((201.0,-78.0),(223.0,-125.0))
    line_between((223.0,-125.0),(167.0,-155.0))
    line_between((167.0,-155.0),(173.0,-174.0))
    line_between((173.0,-174.0),(144.0,-181.0))
    move_to((200.0,-77.0))
    te.pencolor('black')
    te.end_fill()
    move_to((144.0,-181.0))
    smooth_bezier_curve(((144.0,-174.0),(142.0,-166.0),
    (142.0,-158.0),(140.0,-151.0),(140.0,-144.0),(137.0,-135.0)))

    ####################### Plain Red Cap ################################
    move_to((-181.0,148.0))
    te.fillcolor('#CD0000')
    te.begin_fill()
    smooth_bezier_curve(((-181.0,148.0),(-161.0,157.0),(-141.0,166.0),(-113.0,173.0),
    (-87.0,179.0),(-68.0,184.0),(-54.0,186.0),(-46.0,187.0),(-31.0,190.0),(-24.0,191.0),
    (0.0,191.0),(14.0,191.0),(31.0,191.0),(35.0,192.0),(42.0,198.0),(50.0,207.0),(62.0,227.0)))
    line_between((62.0,227.0), (82.0,261.0))
    move_to((82.0,261.0))
    line_between((82.0,261.0), (64.0,332.0))
    smooth_bezier_curve(((64.0,332.0),(59.0,339.0),(49.0,346.0),(37.0,350.0),(24.0,353.0),(7.0,358.0),
    (-4.0,361.0),(-13.0,363.0),(-26.0,363.0),(-40.0,364.0),(-63.0,362.0),(-84.0,359.0),(-100.0,353.0),
    (-115.0,348.0),(-128.0,341.0),(-141.0,335.0),(-150.0,328.0),(-161.0,321.0),(-169.0,314.0),
    (-183.0,301.0),(-191.0,291.0),(-193.0,282.0),(-193.0,274.0),(-191.0,266.0)))
    move_to((-191.0,266.0))
    line_between((-191.0,266.0), (-171.0,206.0))
    line_between((-171.0,206.0),(-186.0,158.0))
    smooth_bezier_curve(((-186.0,158.0),(-186.0,151.0),(-184.0,148.0),(-183.0,146.0),(-181.0,148.0)))
    te.end_fill()
    move_to((-170.0,204.0))
    smooth_bezier_curve(((-170.0,204.0),(-157.0,210.0),(-146.0,216.0),(-135.0,222.0),(-127.0,227.0),
    (-117.0,232.0),(-98.0,238.0),(-73.0,246.0),(-49.0,252.0),(-36.0,251.0),(-10.0,256.0),
    (16.0,257.0),(33.0,259.0),(55.0,259.0),(65.0,258.0),(74.0,258.0),(78.0,261.0)))

   
    ######################## Green Symbol On Hat ###########################
    move_to((-151.0,325.0))
    te.fillcolor('#444444')
    te.begin_fill()
    smooth_bezier_curve(((-155.0,324.0),(-152.0,313.0),(-146.0,299.0),(-138.0,286.0),
    (-130.0,278.0),(-121.0,268.0),(-109.0,261.0),(-90.0,254.0),(-79.0,252.0),(-71.0,244.0),
    (-60.0,251.0),(-53.0,250.0),(-44.0,253.0),(-25.0,266.0),(-11.0,278.0),(-1.0,290.0),
    (5.0,305.0),(9.0,324.0),(9.0,339.0),(7.0,355.0),(5.0,360.0)))
    smooth_bezier_curve(((7.0,356.0),(-6.0,358.0),(-21.0,360.0),(-31.0,361.0),(-40.0,361.0),
    (-50.0,360.0),(-59.0,357.0),(-69.0,357.0),(-81.0,356.0),(-95.0,352.0),(-110.0,348.0),
    (-118.0,343.0),(-128.0,340.0),(-136.0,335.0),(-144.0,330.0),(-155.0,324.0)))
    te.end_fill()
    move_to((-68.0,305.0))
    te.pencolor('#228B22')
    te.dot(35)
    move_to((-38.0,309.0))
    te.fillcolor('#228B22')
    te.begin_fill()
    te.seth(100)
    te.circle(30, 180)
    te.seth(190)
    te.fd(15)
    te.seth(100)
    te.circle(-45, 180)
    te.right(90)
    te.fd(15)
    te.end_fill()
    te.pencolor('#000000')


    # left cheek
    move_to((-130.0,46.0))
    te.seth(300)
    te.fillcolor('#DD4D28')
    te.begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            te.lt(3)
            te.fd(a)
        else:
            a += 0.05
            te.lt(3)
            te.fd(a)
    te.end_fill()
    # right cheek
    move_to((103.0,80.0))
    te.seth(60)
    te.fillcolor('#DD4D28')
    te.begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            te.lt(3)
            te.fd(a)
        else:
            a += 0.05
            te.lt(3)
            te.fd(a)
    te.end_fill()


    ####################### Mouth ########################
    move_to((-11.0,42.0))
    te.fillcolor('#88141D')
    te.begin_fill()
    #
    l1 = []
    l2 = []
    te.seth(190)
    a = 0.7
    #left curvature of mouth
    for i in range(28):
        a += 0.1
        te.right(3)
        te.fd(a)
        l1.append(te.position())
    move_to((-11.0,42.0))
    te.seth(10)
    a = 0.7
    #right curvature of mouth
    for i in range(28):
        a += 0.1
        te.left(3)
        te.fd(a)
        l2.append(te.position())

    #################### Tongue and Color ################
    te.seth(10)
    te.circle(50, 15)
    te.left(180)
    te.circle(-50, 15)
    te.circle(-50, 40)
    te.seth(233)
    te.circle(-50, 55)
    te.left(180)
    te.circle(50, 12.1)
    te.end_fill()
    move_to((11.0,68.0))
    te.fillcolor('#DD716F')
    te.begin_fill()
    te.seth(145)
    te.circle(40, 86)
    te.penup()
    for pos in reversed(l1[:20]):
        te.goto(pos[0], pos[1] + 1.5)
    for pos in l2[:20]:
        te.goto(pos[0], pos[1] + 1.5)
    te.pendown()
    te.end_fill()
    move_to((-18.0,116.0))
    smooth_bezier_curve(((-18.0,116.0),(-26.0,116.0)))


  
    ##################### Black Patch in Ears ####################
    move_to((-243.0,127.0))
    te.fillcolor("#000000")
    te.begin_fill()
    smooth_bezier_curve(((-243.0,127.0),(-249.0,120.0),(-246.0,124.0),(-251.0,115.0),(-258.0,107.0),
    (-264.0,99.0),(-271.0,88.0),(-281.0,75.0),(-282.0,75.0),(-279.0,71.0),(-281.0,74.0),(-273.0,74.0),
    (-264.0,78.0),(-252.0,84.0),(-243.0,89.0),(-233.0,94.0),(-217.0,104.0),(-206.0,113.0),(-199.0,113.0)))
    te.end_fill()
    move_to((138.0,279.0))
    te.begin_fill()
    smooth_bezier_curve(((138.0,279.0),(143.0,281.0),(157.0,286.0),(165.0,290.0),(175.0,294.0),(184.0,295.0),
    (194.0,299.0),(203.0,301.0),(210.0,304.0),(211.0,305.0),(215.0,305.0),(216.0,306.0),(220.0,306.0),
    (218.0,302.0),(216.0,299.0),(213.0,291.0),(206.0,282.0),(202.0,277.0),(196.0,272.0),(189.0,263.0),
    (182.0,258.0),(175.0,250.0),(169.0,246.0),(162.0,240.0),(157.0,236.0),(159.0,240.0),(153.0,234.0),
    (154.0,249.0),(153.0,262.0),(149.0,273.0),(147.0,280.0)))
    te.end_fill()


    ################# Left Eye #################################
    move_to((-87.0,102.0))
    te.seth(0)
    te.fillcolor('#333333')
    te.begin_fill()
    te.circle(22)
    te.end_fill()
    move_to((-87.0, 112.0))
    te.fillcolor('#000000')
    te.begin_fill()
    te.circle(10)
    te.end_fill()
    move_to((-81.0, 124.0))
    te.fillcolor('#ffffff')
    te.begin_fill()
    te.circle(10)
    te.end_fill()
    #################### Right Eye #############################
    move_to((33.0,123.0))
    te.seth(0)
    te.fillcolor('#333333')
    te.begin_fill()
    te.circle(22)
    te.end_fill()
    move_to((33,133))
    te.fillcolor('#000000')
    te.begin_fill()
    te.circle(10)
    te.end_fill()
    move_to((27, 145))
    te.fillcolor('#ffffff')
    te.begin_fill()
    te.circle(10)
    te.end_fill()

    te.hideturtle()
    te.done()
    # Wait for the user to click to exit
    te.exitonclick()
    
if __name__ == '__main__':
    main()
    