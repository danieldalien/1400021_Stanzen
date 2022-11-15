#Script Stamp

D1 = {
    "X1" : 1  ,
    "X2" : 2  , 
    "X3" : 4  ,
    "X4" : 8  ,
    "X5" : 16 ,
    "X6" : 32 ,
    "X7" : 64 ,
    "X8" : 128
}

pneumatic = {
    "first_block" : "MPA_Outputs_40003" ,
    "second_block" : "2_Outputs_40004"
}

DI_Signals = {
    "first_block" : "1_DI_45395" ,
    "second_block" :"2_DI_45397" , 
    "third_block" : "3_DI_45399"            
}

handpress_clam = {
    "go_bp" : [ pneumatic["first_block"] , 1 ]  ,
    "go_wp" : [ pneumatic["first_block"] , 2 ]  , 
    "status_bp" : [ DI_Signals["first_block"] , 2 ] ,
    "status_wp" : [ DI_Signals["first_block"] , 1 ] 
}

rotary_gripper_turn = {
    "go_bp" : [ pneumatic["first_block"] , 4 ]  ,
    "go_wp" : [ pneumatic["first_block"] , 8 ]  , 
    "status_bp" : [ DI_Signals["first_block"] , 4 , 8 ] ,
    "status_wp" : [ DI_Signals["first_block"] , 16 , 32 ] 
}

rotary_gripper = {
    "go_bp" : [ pneumatic["first_block"] , 16 ]  ,
    "go_wp" : [ pneumatic["first_block"] , 32 ]  , 
    "status_bp" : [ DI_Signals["first_block"] , 4 , 16 ] ,
    "status_wp" : [ DI_Signals["first_block"] , 8 , 32 ] 
}

rotary_gripper_grip_and_turn = {

  "turn_bp_open" : [ pneumatic["first_block"] , 20 ] ,
  "turn_bp_closed" : [ pneumatic["first_block"] , 36 ] ,
  "turn_wp_open" : [ pneumatic["first_block"] , 24 ] ,
  "turn_wp_closed" : [ pneumatic["first_block"] , 40 ] ,

  "status_turn_bp_open" : [ DI_Signals["first_block"] , 16 ] ,
  "status_turn_bp_closed" : [ DI_Signals["first_block"] , 32 ] ,
  "status_turn_wp_open" : [ DI_Signals["first_block"] , 4 ] ,
  "status_turn_wp_closed" : [ DI_Signals["first_block"] , 8 ] 

}

stroke_horizontal_cylinder = {
    "go_bp" : [ pneumatic["first_block"] , 128 ]  ,
    "go_wp" : [ pneumatic["first_block"] , 64 ]  , 
    "status_bp" : [ DI_Signals["first_block"] , 64 ] ,
    "status_wp" : [ DI_Signals["first_block"] , 128 ] 
}

stroke_verticale_cylinder = {
    "go_bp" : [ pneumatic["second_block"] , 16 ]  ,
    "go_wp" : [ pneumatic["second_block"] , 32 ]  , 
    "status_bp" : [ DI_Signals["second_block"] , 1 ] ,
    "status_wp" : [ DI_Signals["second_block"] , 2 ] 
}

transfer_cylinder = {
    "go_bp" : [ pneumatic["second_block"] , 2 ]  ,
    "go_wp" : [ pneumatic["second_block"] , 1 ]  , 
    "status_bp" : [ DI_Signals["second_block"] , 4 ] ,
    "status_wp" : [ DI_Signals["second_block"] , 8 ] 
}

taster_cylinder = {
  "status_bp" : [ DI_Signals["second_block"] , 16 ] , 
  "status_wp" : [ DI_Signals["second_block"] , 32 ]
}

test_head = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["second_block"] , 64 ]
}

inlet_sensor_left = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 1 ]
}

inlet_sensor_right = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 2 ]
}

venturi_vacuum_1 = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 4 ]
}

venturi_vacuum_2 = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 8 ]
}

venturi_vacuum_3 = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 16 ]
}

venturi_vacuum_4 = {
  "status_bp" : -1 , 
  "status_wp" : [ DI_Signals["third_block"] , 32 ]
}

####################################

class calc():

    def __init__(self) -> None:
        
        pass

    def calc_positions(self):
        """
        Calculates the waypoints
        """


        # Station Magazin
        h_SM = 145 # max hoehe station magazin
        y_SM = 95 #Abstand zwischen beiden stationen
        global Global_15_S1M
        global System_11_S1M 
        global System_21_S2M
        global System_25_S2M
        
        System_11_S1M    = posx(Global_15_S1M)
        System_11_S1M[2] = System_11_S1M[2] + h_SM
        System_21_S2M    = posx(System_11_S1M)
        System_21_S2M[1] = System_21_S2M[1] - y_SM
        System_25_S2M    = posx(Global_15_S1M)
        System_25_S2M[1] = System_25_S2M[1] - y_SM
        #tp_popup("System_11_S1M : {0}".format(System_11_S1M), DR_PM_ALARM)

        #Station SS1 lever
        global Global_40_S1S
        global System_41_S1S
        System_41_S1S = posx(Global_40_S1S)
        System_41_S1S[2] = System_41_S1S[2] + 30

        #Station SS1 First Place
        global Global_35_S1S
        global System_31_S1S
        global System_32_S1S

        System_32_S1S = posx(Global_35_S1S)
        System_32_S1S[0] = System_32_S1S[0] - 2.46
        System_32_S1S[2] = System_32_S1S[2] + 2.46

        System_31_S1S = posx(Global_35_S1S)
        System_31_S1S[0] = System_31_S1S[0] + 48.92
        System_31_S1S[2] = System_31_S1S[2] + 53.81

        #Station SS1 First Pick

        global Global_55_S1S
        global System_51_S1S
        global System_52_S1S
        global System_56_S1S

        System_56_S1S = posx(Global_55_S1S)
        System_56_S1S[0] = System_56_S1S[0] + 24.51
        System_56_S1S[2] = System_56_S1S[2] + 24.51

        System_52_S1S = posx(Global_55_S1S)
        System_52_S1S[0] = System_52_S1S[0] + 53.64
        System_52_S1S[2] = System_52_S1S[2] + 62.14
        
        System_51_S1S = posx(Global_55_S1S)
        System_51_S1S[0] = System_51_S1S[0] - 4.24
        System_51_S1S[2] = System_51_S1S[2] + 4.24

        #Station SR First Place

        global Global_65_SR
        global System_61_SR
        global System_62_SR
        global System_63_SR
        global System_66_SR

        System_61_SR = posx(Global_65_SR)
        System_61_SR[1] = System_61_SR[1] + 30
        System_61_SR[2] = System_61_SR[2] + 30 

        System_62_SR = posx(Global_65_SR)
        System_62_SR[1] = System_62_SR[1] + 30
        System_62_SR[2] = System_62_SR[2] + 2.5

        System_63_SR = posx(Global_65_SR)
        System_63_SR[2] = System_63_SR[2] + 2.5

        System_66_SR = posx(Global_65_SR)#Rückzug
        System_66_SR[0] = System_66_SR[0] + 70


        #Station SR Pick
        global Global_75_SR
        global System_71_SR
        global System_76_SR
        global System_77_SR
        #old_Global_75_SR = posx(-760 , 33.19 , 180.93 , 179.99 , 90.01 , 90.88)

        System_71_SR = posx(Global_75_SR)
        System_71_SR[0] = System_71_SR[0] + 10

        System_76_SR = posx(Global_75_SR)
        System_76_SR[2] = System_76_SR[2] + 15
        System_77_SR = posx(Global_75_SR)
        System_77_SR[0] = System_77_SR[0] + 65
        System_77_SR[2] = System_77_SR[2] + 15

        #Station SS1 Second Place
        global Global_85_S1S
        global System_81_S1S
        global System_82_S1S
        global System_86_S1S

        System_82_S1S = posx(Global_85_S1S)
        System_82_S1S[0] = System_82_S1S[0] - 2.81
        System_82_S1S[2] = System_82_S1S[2] + 2.81

        System_81_S1S = posx(Global_85_S1S)
        System_81_S1S[0] = System_81_S1S[0] + 48.92
        System_81_S1S[2] = System_81_S1S[2] + 53.81

        System_86_S1S = posx(Global_85_S1S)
        System_86_S1S[0] = System_86_S1S[0] - 4.36
        System_86_S1S[2] = System_86_S1S[2] + 9.1

        #Station SS1 Second Pick
        global Global_95_S1S
        global System_96_S1S # Ruckzug
        global System_91_S1S # Vorposition

        System_96_S1S = posx(Global_95_S1S)
        System_96_S1S[1] = System_96_S1S[1] + 103.55

        System_91_S1S = posx(Global_95_S1S)
        System_91_S1S[0] = System_91_S1S[0] + 57.95
        System_91_S1S[2] = System_91_S1S[2] + 57.95

        #Station ST
        global Global_105_ST
        global System_101_ST

        System_101_ST = posx(Global_105_ST)
        System_101_ST[2] = System_101_ST[2] + 42.65

        #Station S2S
        global Global_115_S2S
        global System_111_S2S

        System_111_S2S = posx(Global_115_S2S)
        System_111_S2S[2] = System_111_S2S[2] + 50
     
#####################################  
     
class modbus( ):


    def __init__(self , D1 , pneumatic , DI_Signals , handpress_clam , rotary_gripper_turn , rotary_gripper , rotary_gripper_grip_and_turn , stroke_horizontal_cylinder , stroke_verticale_cylinder , transfer_cylinder , taster_cylinder , test_head , inlet_sensor_left , inlet_sensor_right , venturi_vacuum_1 , venturi_vacuum_2 , venturi_vacuum_3 , venturi_vacuum_4) :

        self.id_handpress_clam = "handpress_clam"
        self.id_rotary_gripper_turn = "rotary_gripper_turn"
        self.id_rotary_gripper = "rotary_gripper"
        self.id_rotary_gripper_grip_and_turn = "rotary_gripper_grip_and_turn" 
        self.id_stroke_horizontal_cylinder = "stroke_horizontal_cylinder"
        self.id_stroke_verticale_cylinder = "stroke_verticale_cylinder"
        self.id_transfer_cylinder = "transfer_cylinder"
        self.id_taster_cylinder = "taster_cylinder"
        self.id_test_head = "test_head"
        self.id_inlet_sensor_left = "inlet_sensor_left"
        self.id_inlet_sensor_right = "inlet_sensor_right"
        self.id_venturi_vacuum_1 = "venturi_vacuum_1"
        self.id_venturi_vacuum_2 = "venturi_vacuum_2"
        self.id_venturi_vacuum_3 = "venturi_vacuum_3"
        self.id_venturi_vacuum_4 = "venturi_vacuum_4"


        self.handpress_clam = handpress_clam
        self.rotary_gripper_turn = rotary_gripper_turn
        self.rotary_gripper = rotary_gripper
        self.rotary_gripper_grip_and_turn = rotary_gripper_grip_and_turn
        self.stroke_horizontal_cylinder = stroke_horizontal_cylinder
        self.stroke_verticale_cylinder = stroke_verticale_cylinder
        self.transfer_cylinder = transfer_cylinder
        self.taster_cylinder = taster_cylinder
        self.test_head = test_head
        self.inlet_sensor_left = inlet_sensor_left
        self.inlet_sensor_right = inlet_sensor_right
        self.venturi_vacuum_1 = venturi_vacuum_1
        self.venturi_vacuum_2 = venturi_vacuum_2
        self.venturi_vacuum_3 = venturi_vacuum_3
        self.venturi_vacuum_4 = venturi_vacuum_4
        self.D1 = D1
        self.pneumatic = pneumatic
        self.DI_Signals = DI_Signals
        
        self.timeout = 4

    def stop_at_signal( self , id , signal):
        """"
        signal = Stop at bp or stop at wp 
        """
        t = 0 
        while True :
            wp , bp = self.get_status_signal(id)

            if signal == "bp":
                if bp:
                    stop(DR_SSTOP)
                    break
            elif signal == "wp":
                if wp:
                    stop(DR_SSTOP)
                    break   
                         
            if t > self.timeout+15:
                tp_popup("timeout at stop_at_signal()",DR_PM_ALARM)
                exit()
            else:
                wait(0.01)
                t = t + 0.01
    
    def get_cylinder( self , id ):

        #if id == self.rotary_gripper_turn or self.rotary_gripper :
        #  tp_popup("Diese id = {0} ist nicht Konfiguriert".format(id), DR_PM_ALRAM)
        #  exit()

        cylinder = {}

        if id == self.id_handpress_clam :
            cylinder = self.handpress_clam

        elif id == self.id_rotary_gripper_turn:
            cylinder = self.rotary_gripper_turn

        elif id == self.id_rotary_gripper:
            cylinder = self.rotary_gripper

        elif id == self.id_stroke_horizontal_cylinder:
            cylinder = self.stroke_horizontal_cylinder

        elif id == self.id_stroke_verticale_cylinder:
            cylinder = self.stroke_verticale_cylinder

        elif id == self.id_transfer_cylinder:
            cylinder = self.transfer_cylinder

        else:
            tp_popup("Kenne diese id = {0} nicht".format(id), DR_PM_ALARM)

        return cylinder

    def get_signal( self , id ):

        status = {}

        if id == self.id_taster_cylinder:
            status = self.taster_cylinder

        elif id == self.id_test_head:
            status = self.test_head

        elif id == self.id_inlet_sensor_left:
            status = self.inlet_sensor_left

        elif id == self.id_inlet_sensor_right:
            status = self.inlet_sensor_right

        elif id == self.id_venturi_vacuum_1:
            status = self.venturi_vacuum_1

        elif id == self.id_venturi_vacuum_2:
            status = self.venturi_vacuum_2

        elif id == self.id_venturi_vacuum_3:
            status = self.venturi_vacuum_3

        elif id == self.id_venturi_vacuum_4:
            status = self.venturi_vacuum_4

        elif id == self.id_handpress_clam:
            status = self.handpress_clam

        elif id == self.id_stroke_horizontal_cylinder:
            status = self.stroke_horizontal_cylinder

        elif id == self.id_stroke_verticale_cylinder:
            status = self.stroke_verticale_cylinder

        elif id == self.id_transfer_cylinder:
            status = self.transfer_cylinder

    
        else:
            tp_popup("Kenne diese id = {0} nicht".format(id), DR_PM_ALARM)

        return status 

    def get_status_rotary_gripper ( self ):

        if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
            status = "bp_open"
        elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
            status = "bp_closed"
        elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
            status = "wp_open"
        elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
            status = "wp_closed"
        else :
            status = "Unknown"
            tp_popup("Unknown status at rotary gripper" , DR_PM_ALARM)
        
        return status 

    def move_all( self , position = "bp" ):
        global System_first_block_output
        global System_second_block_output


        if position == "bp" :

            set_modbus_output(self.pneumatic["first_block"] , 149 )
            set_modbus_output(self.pneumatic["second_block"] , 18 )

        elif position == "wp" :
            set_modbus_output(self.pneumatic["first_block"] , 106 )
            set_modbus_output(self.pneumatic["second_block"] , 33 )
        
        elif position == "restart":
            set_modbus_output(self.pneumatic["first_block"]  , int(System_first_block_output) )
            set_modbus_output(self.pneumatic["second_block"] , int(System_second_block_output) )

    def get_status_signal( self , id ):
        """"
        get status of modbus component 
        """

        id_signal = self.get_signal(id)
        wp = False
        bp = False

        if id == self.id_taster_cylinder or id == self.id_handpress_clam or id == self.id_stroke_horizontal_cylinder or id == self.id_stroke_verticale_cylinder or id == self.id_taster_cylinder:

            if id_signal["status_wp"][1] & get_modbus_input(id_signal["status_wp"][0]) != 0 :
                wp = True 
            if id_signal["status_bp"][1] & get_modbus_input(id_signal["status_bp"][0]) != 0 : 
                bp = True 
            return wp , bp 
        else : 

            if id_signal["status_wp"][1] & get_modbus_input(id_signal["status_wp"][0]) != 0 :
                wp = True 
            else :
                bp = True

            return wp , bp

    def get_set_output( self , id = 0 , status = 0 ):  
        """
        Gets current modbus output and add/substracts the new state .
        Afterwards it sets the new output

        id = id of modbus component
        status : go_bp , go_wp , turn_bp_open, turn_bp_closed , turn_wp_open , turn_wp_closed 
        """

        global System_first_block_output
        global System_second_block_output

        # First Block 
        first_block_output = 0 
        second_block_output = 0

        if self.handpress_clam["status_bp"][1] & get_modbus_input(self.handpress_clam["status_bp"][0]) != 0 :
      
            first_block_output = first_block_output + self.handpress_clam["go_bp"][1]
        elif self.handpress_clam["status_wp"][1] & get_modbus_input(self.handpress_clam["status_wp"][0]) != 0 :
            first_block_output = first_block_output + self.handpress_clam["go_wp"][1]
        else:
            tp_popup("problem at handpress_clam" , DR_PM_ALARM)

        #tp_popup("output = {0}".format(first_block_output), DR_PM_ALARM)

        if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
            first_block_output = first_block_output + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
        elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
            first_block_output = first_block_output + self.rotary_gripper_grip_and_turn["turn_bp_closed"][1]
        elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
            first_block_output = first_block_output + self.rotary_gripper_grip_and_turn["turn_wp_open"][1]
        elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
            first_block_output = first_block_output + self.rotary_gripper_grip_and_turn["turn_wp_closed"][1]
        else:
            tp_popup("problem at rotary_gripper_turn" , DR_PM_ALARM)

        #tp_popup("output = {0}".format(first_block_output), DR_PM_ALARM)

        if self.stroke_horizontal_cylinder["status_bp"][1] & get_modbus_input(self.stroke_horizontal_cylinder["status_bp"][0]) != 0 :
            first_block_output = first_block_output + self.stroke_horizontal_cylinder["go_bp"][1]
        elif self.stroke_horizontal_cylinder["status_wp"][1] & get_modbus_input(self.stroke_horizontal_cylinder["status_wp"][0]) != 0 :
            first_block_output = first_block_output + self.stroke_horizontal_cylinder["go_wp"][1]
        else:
            tp_popup("stroke_horizontal_cylinder" , DR_PM_ALARM)
   

        # Second Block
        second_block_output = 0 

        if self.stroke_verticale_cylinder["status_bp"][1] & get_modbus_input(self.stroke_verticale_cylinder["status_bp"][0]) != 0 :
            second_block_output = second_block_output + self.stroke_verticale_cylinder["go_bp"][1]
        elif self.stroke_verticale_cylinder["status_wp"][1] & get_modbus_input(self.stroke_verticale_cylinder["status_wp"][0]) != 0 :
            second_block_output = second_block_output + self.stroke_verticale_cylinder["go_wp"][1]
        else:
            tp_popup("problem at stroke_verticale_cylinder" , DR_PM_ALARM)

        if self.transfer_cylinder["status_bp"][1] & get_modbus_input(self.transfer_cylinder["status_bp"][0]) != 0 :
            second_block_output = second_block_output + self.transfer_cylinder["go_bp"][1]
        elif self.transfer_cylinder["status_wp"][1] & get_modbus_input(self.transfer_cylinder["status_wp"][0]) != 0 :
            second_block_output = second_block_output + self.transfer_cylinder["go_wp"][1]
        else:
            tp_popup("problem at transfer_cylinder" , DR_PM_ALARM)


        if id != self.id_rotary_gripper_grip_and_turn : 
            cylinder = self.get_cylinder(id)
            id_block = cylinder["status_bp"][0]
            merker = 0
        else :
            id_block = self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]
            merker = 1


        if id_block == self.DI_Signals["first_block"] :

            if merker == 0 :
                if status == "go_bp":
                    if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                        first_block_output = first_block_output - cylinder["go_wp"][1] + cylinder["go_bp"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

                elif status == "go_wp":
                    if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                        first_block_output = first_block_output - cylinder["go_bp"][1] + cylinder["go_wp"][1]
                    elif cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                        first_block_output = first_block_output 
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

            elif merker == 1 :
                if status == "turn_bp_open":
                    if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_open"][1] + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

                elif status == "turn_bp_closed":
                    if self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_open"][1] + self.rotary_gripper_grip_and_turn["turn_bp_closed"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_open"][1] + self.rotary_gripper_grip_and_turn["turn_bp_closed"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_bp_open"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

                elif status == "turn_wp_open":
                    if self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_open"][1] + self.rotary_gripper_grip_and_turn["turn_wp_open"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_wp_open"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_wp_open"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

                elif status == "turn_wp_closed":
                    if self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        first_block_output = first_block_output 
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_open"][1] + self.rotary_gripper_grip_and_turn["turn_wp_closed"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_bp_closed"][1] + self.rotary_gripper_grip_and_turn["turn_wp_closed"][1]
                    elif self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        first_block_output = first_block_output - self.rotary_gripper_grip_and_turn["turn_wp_open"][1] + self.rotary_gripper_grip_and_turn["turn_wp_closed"][1]
                    else:
                        tp_popup("Problem at get_set_output" , DR_PM_ALARM)

        elif id_block == self.DI_Signals["second_block"] :
            if status == "go_bp":
                if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                    second_block_output = second_block_output 
                elif cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                    second_block_output = second_block_output - cylinder["go_wp"][1] + cylinder["go_bp"][1]
                else:
                    tp_popup("Problem at get_set_output" , DR_PM_ALARM)

            elif status == "go_wp":
                if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                    second_block_output = second_block_output - cylinder["go_bp"][1] + cylinder["go_wp"][1]
                elif cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                    second_block_output = second_block_output 
                else:
                    tp_popup("Problem at get_set_output" , DR_PM_ALARM)

        elif id_block == self.DI_Signals["third_block"] :
            pass
        

        set_modbus_output(self.pneumatic["first_block"] , first_block_output )
        set_modbus_output(self.pneumatic["second_block"] , second_block_output )

        while True :
            t = 0
            if id != self.id_rotary_gripper_grip_and_turn : 
                if status == "go_bp":

                    if cylinder["status_bp"][1] & get_modbus_input(cylinder["status_bp"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)

                if status == "go_wp":

                    if cylinder["status_wp"][1] & get_modbus_input(cylinder["status_wp"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)
            else :

                if status == "turn_bp_open":

                    if self.rotary_gripper_grip_and_turn["status_turn_bp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_open"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)

                elif status == "turn_bp_closed":

                    if self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_bp_closed"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)

                elif status == "turn_wp_open":

                    if self.rotary_gripper_grip_and_turn["status_turn_wp_open"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_open"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)


                elif status == "turn_wp_closed":

                    if self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][1] & get_modbus_input(self.rotary_gripper_grip_and_turn["status_turn_wp_closed"][0]) != 0 :
                        break 
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout get_set_output",DR_PM_ALARM)
                        elif t > self.timeout/2:
                            set_modbus_output(self.pneumatic["first_block"] , first_block_output )
                            set_modbus_output(self.pneumatic["second_block"] , second_block_output )
                        else:
                            t = t + 0.1
                            wait(0.1)

        System_first_block_output = first_block_output
        System_second_block_output = second_block_output

        return first_block_output , second_block_output

    def set_digital_output_wait_input(self , output , set_status ):
        """
        Sets digital output and waits for modbus signal for confirmation 

        output = Integer 
        set_status = "go_wp" or "go_bp"
        """

        if output == 6 : # Greifer Vertikal
            signal = self.id_venturi_vacuum_1
        elif output == 8 : # Greifer Horizontal
            signal = self.id_venturi_vacuum_2
        elif output == 10 : # S1
            signal = self.id_venturi_vacuum_3
        elif output == 12 :
            signal = self.id_taster_cylinder
        elif output == 13 : # SP
            signal = self.id_venturi_vacuum_4
        else :
            signal = "unkown"
            tp_popup("Kenne output:  {0} nicht ! (set_digital_output_wait_input) ".format(output) , DR_PM_ALARM)
            exit()

        if signal != "unkown":
            if set_status == "go_bp":
                set_digital_output(-(output))
                t = 0
                while True: 
                    wp , bp = self.get_status_signal(signal)

                    if bp == True and wp == False :
                        break
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout at output {0}".format(output) , DR_PM_ALARM)
                            exit()
                        else:
                            wait(0.1)
                            t = t + 0.1

            elif set_status == "go_wp":
                set_digital_output((output))
                t = 0
                while True: 
                    wp , bp = self.get_status_signal(signal)

                    if wp == True and bp == False :
                        break
                    else:
                        if t > self.timeout:
                            tp_popup("Timeout at output {0}".format(output) , DR_PM_ALARM)
                            exit()
                        else:
                            wait(0.1)
                            t = t + 0.1

            else :
                tp_popup("Wrong set status " , DR_PM_ALARM)
                exit()

#####################################

class vacuum() :

    def __init__(self ):
        # Here the diffrent outputs need to be configured.
        self.t_timeout = 5
        self.S1S_vacuum_out = 0
        self.S1S_vacuum_check_in = 0
        self.SP_vacuum_out = 0
        self.SP_vacuum_check_in = 0
        self.RD_vacuum_out = 0
        self.RD_vacuum_check_in = 0
        self.c_error = error()
        self.c_modbus = modbus(
                    D1 , 
                    pneumatic , 
                    DI_Signals , 
                    handpress_clam , 
                    rotary_gripper_turn , 
                    rotary_gripper , 
                    rotary_gripper_grip_and_turn ,
                    stroke_horizontal_cylinder , 
                    stroke_verticale_cylinder , 
                    transfer_cylinder , 
                    taster_cylinder , 
                    test_head ,
                    inlet_sensor_left , 
                    inlet_sensor_right ,
                    venturi_vacuum_1 , 
                    venturi_vacuum_2 , 
                    venturi_vacuum_3 , 
                    venturi_vacuum_4 ) 

    def vacuum_id(self,id):
        """
        Vacuum_id: returns for a given id , the corrsponding DO
        """        
        if id == id_S1S:
            id_output = self.S1S_vacuum_out
            id_input = self.S1S_vacuum_check_in
        elif id == id_SP:
            id_output = self.SP_vacuum_out
            id_input = self.SP_vacuum_check_in
        elif id == id_RD :
            id_output = self.RD_vacuum_out
            id_input = self.RD_vacuum_check_in
        else : 
            print("Unkown Vaccum ID :"  + id )
            tp_popup("[vacuum] Unkown Vaccum ID : {0}".format(id), DR_PM_ALARM)

        return id_output , id_input

    def vacuum_control(self , id , check_state ):

        """
        vacuum_control checks wheter or not vacuum was reached .

        :param id: id of the component which should be checked for vacuum 
        :param check_state: Check for vacuum or no vacuum 

        :return: TRUE FALSE or Error  
        """ 
        ### Variabeln Deklarieren ###
        global Global_Vak_Ok
        global Global_Disturbance

        Global_Vak_Ok = 0
        timeout_vak_check = self.t_timeout
        id_output , id_input = 1000,5000
        t = 0 
        ### Ende ###
        if check_state == True :
            if id == 10 :
                while True :
                    if self.c_modbus.get_status_signal(self.c_modbus.id_venturi_vacuum_3) == True:
                        break
                    else:
                        if t >self.t_timeout :
                            tp_popup("timeout vacuum" , DR_PM_ALARM)
                            exit()
                        else :
                            wait(0.1)
                            t = t + 0.1

        elif check_state == False:
            if id == 10 :
                while True :
                    if self.c_modbus.get_status_signal(self.c_modbus.id_venturi_vacuum_3) == False:
                        break
                    else:
                        if t >self.t_timeout :
                            tp_popup("timeout vacuum" , DR_PM_ALARM)
                            exit()
                        else :
                            wait(0.1)
                            t = t + 0.1

    def vacuum(self , id , set_state , vacuum_check = True):
        """
        vacuum sets or resets vacuum for given id .

        :param id: id of the component where vacuum should be set or reset  
        :param state: Va

        :return: TRUE FALSE or Error  
        """ 
        ##########################
        ##########################
        #id_output , id_input = self.vacuum_id(id)
        if set_state == True :
            set_digital_output( id , ON )

        elif set_state == False : 
            set_digital_output(id , OFF )

        else : 
            tp_popup("[Vacuum] Unsupported vacuum state: {0} , Use True to start vacuum  and False to stop".format(set_state), DR_PM_ALARM)
        
        if vacuum_check:
            self.vacuum_control(id , set_state)

#####################################

class drive() :

    def __init__(self , override = 100 , blend_radius = 0 , deltaZ = 50) :
        self.override = override 
        self.blend_radius = blend_radius
        self.deltaZ = deltaZ

    def relative_mvt(self , pose_ini = 0 , ref = "DR_BASE" , deltaX = 0 , deltaY = 0 , deltaZ = 40 , deltaRx = 0 , deltaRy = 0 , deltaRz = 0):
        """
        relative_mvt calculate relative mvt .

        :param id: id of the component where vacuum should be set or reset  
        :param pose_ini : Positon of which relative movement should be executed (only in DR_BASE)
        :param ref : DR_TOOL or DR_BASE 
        
        :return: DR_BASE: posx  , DR_TOOL : moves directly
        """ 

        if ref == "DR_TOOL" :
            Prel = posx(deltaX,deltaY,-1*deltaZ,0,0,0)
            movel(Prel, ref=DR_TOOL, mod=DR_MV_MOD_REL)
        elif ref == "DR_BASE" :
            if pose_ini == 0 :
                
                tp_popup("[relative_mvt] Unsupported position: {0} ".format(pose_ini), DR_PM_ALARM)
            else:
                delta = [ deltaX , deltaY , deltaZ , 0 , 0 , 0 ]
                pos = add_pose(pose_ini , delta)
                return pos
        else :
            tp_popup("[relative_mvt] Unsupported reference: {0} ".format(ref), DR_PM_ALARM)

#####################################    

class ap() :

    global System_Start_Program 
    global System_End_Program 
    global System_Cur_Pos
    global System_i_AP
    global System_SM_Side
    global System_i_Step
    global Global_t_lever
    
 
    def __init__(self ) :
        self.c_functions = functions()
        self.c_calc = calc()
        self.c_vacuum = vacuum()
        self.c_error = error()
        self.c_modbus = modbus(
                D1 , 
                pneumatic , 
                DI_Signals , 
                handpress_clam , 
                rotary_gripper_turn , 
                rotary_gripper , 
                rotary_gripper_grip_and_turn ,
                stroke_horizontal_cylinder , 
                stroke_verticale_cylinder , 
                transfer_cylinder , 
                taster_cylinder , 
                test_head ,
                inlet_sensor_left , 
                inlet_sensor_right ,
                venturi_vacuum_1 , 
                venturi_vacuum_2 , 
                venturi_vacuum_3 , 
                venturi_vacuum_4 ) 
        self.no_blendRadius = 0 
        self.small_blendRadius = 10
        self.big_blendRadius = 50
        self.vel_veryslow = 10
        self.vel_ap = 50
        self.Simulation = 0
        self.t_lever = 1.5 
        self.timeout_restart = 2
        self.override = 75
        self.id_greifer_h = "greifer_horizontal"
        self.id_greifer_v = "greifer_vertikal"
        self.id_kugelschnaepper = "Kugelschnaepper"
        
    def ap_10(self):
        """
        ap_10 : Picks from the Station Magazin.

        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global Global_Disturbance
        global System_End_Program
        global System_i_AP
        global thread
        ### Ende ###

        System_Start_Program = 10
        mwait(0)
        set_tcp(self.id_greifer_v)
        
        if self.Simulation == 0:
            self.c_modbus.set_digital_output_wait_input(6 , "go_bp")
            #self.c_vacuum.vacuum_control(id_S1S , False)

        System_SM_Side = self.c_functions.fifo()
        
        movej(Global_10_SM , r = self.big_blendRadius)
        System_Cur_Pos = 10

        if System_SM_Side == 0 :
            
            movel((System_11_S1M) , r = self.small_blendRadius)
            System_Cur_Pos = 11
            #tp_popup("in ap 10 muss noch vervollständigt werden ob stop signal richtig definiert " , DR_PM_ALARM) 
            amovel(Global_15_S1M , v = self.vel_veryslow)
            set_digital_output(6)
            self.c_modbus.stop_at_signal(self.c_modbus.id_venturi_vacuum_1 , "wp")
            System_Cur_Pos = 15

        elif System_SM_Side == 1 :
            
            movel(System_21_S2M , r = self.small_blendRadius)
            System_Cur_Pos = 21 
            set_digital_output(6)
            amovel(System_25_S2M , v = self.vel_veryslow)
            self.c_modbus.stop_at_signal(self.c_modbus.id_venturi_vacuum_1 , "wp")
            System_Cur_Pos = 25
            
        elif System_SM_Side == -1 :
            Global_Disturbance = 1
            self.c_error.disturbance_message(4)
            exit()

        if self.Simulation == 0:
            self.c_modbus.set_digital_output_wait_input(6 , "go_wp")
        else :
            set_digital_output(-6)

        System_End_Program = 10
        System_i_AP = 30
        
    def ap_20(self):
        pass

    def ap_30(self):
        """
        ap_30 : Places in the first station 
        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_i_AP
        global thread
        ### Ende ###

        #thread_stop(thread)
        System_Start_Program = 30
        
        #thread = thread_run(self.Thread_Handpress_Clam_Wp , loop = False)
        self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_wp")
        

        movej( Global_30_S1S , r = self.big_blendRadius )
        System_Cur_Pos = 30
        #mwait(0)
        #set_tcp(self.id_greifer_v)

        movel( ( System_31_S1S ) , r = self.small_blendRadius)
        System_Cur_Pos = 31

        movel( ( System_32_S1S ) , r = self.no_blendRadius , v = self.vel_ap)
        System_Cur_Pos = 32

        movel( Global_35_S1S , r = self.no_blendRadius , v = self.vel_ap)
        System_Cur_Pos = 35 
        
        if self.Simulation == 0 : 
                   
            self.c_modbus.set_digital_output_wait_input( 6 , "go_bp" )
            set_digital_output( 7 , ON , 0.2 , OFF)

        
        System_End_Program = 30
        System_i_AP = 40
        #thread_stop(thread)
        
    def ap_40( self ) :
        """
        ap_40 : Use lever of SS1 
        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_i_AP
        global thread
        
        ### Ende ###

        #thread_stop(thread)
        System_Start_Program = 40
        mwait(0)
        set_tcp(self.id_kugelschnaepper)

        self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_bp")
        #self.c_modbus.set_digital_output_wait_input( 10 , "go_wp" )

        movej( Global_49_S1S , r = self.big_blendRadius )
        System_Cur_Pos = 49

        movel( System_41_S1S , r = self.small_blendRadius , ref = DR_WORLD )
        System_Cur_Pos = 41 
        movel( Global_40_S1S , r = self.no_blendRadius , ref = DR_WORLD)
        System_Cur_Pos = 40 
        movec( Global_46_S1S , Global_47_S1S , time = self.t_lever )
        System_Cur_Pos = 47

        if self.Simulation == 0 :
            self.c_modbus.set_digital_output_wait_input( 10 , "go_bp" )
            

        movec( Global_48_S1S , Global_45_S1S , time = self.t_lever , ref = DR_WORLD)
        System_Cur_Pos = 45 
        if System_i_Step == 3 :
            System_i_AP = 50 
        elif System_i_Step == 8 :
            System_i_AP = 90 

        #tp_popup("stop")
        movec( Global_44_S1S , Global_43_S1S , time = self.t_lever , ref = DR_WORLD)
        movec( Global_42_S1S , Global_40_S1S , time = self.t_lever , ref = DR_WORLD)
        System_Cur_Pos = 40 
        movel( System_41_S1S , r = self.small_blendRadius , ref = DR_WORLD  , v = self.vel_ap)
        System_Cur_Pos = 41 

        
        System_End_Program = 40

    def ap_50( self ) :
        """
        ap_50 : First pick out of SS1
        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_i_AP
        global thread
        ### Ende ###

        #thread_stop(thread)
        System_Start_Program = 50
        mwait(0)
        set_tcp(self.id_greifer_h)

        movej( Global_30_S1S  , r = self.big_blendRadius )
        System_Cur_Pos = 30

        movel( ( System_56_S1S ) , r = self.small_blendRadius )
        System_Cur_Pos = 56 

        movel( Global_55_S1S , r = self.no_blendRadius  , v = self.vel_ap/4)
        System_Cur_Pos = 55 

        if self.Simulation == 0 :
            self.c_modbus.set_digital_output_wait_input( 8 , "go_wp" )
            
        self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_wp")
        #thread = thread_run(self.Thread_Turn_Bp_Open , loop = False)
        
        self.c_modbus.get_set_output(self.c_modbus.id_rotary_gripper_grip_and_turn , "turn_bp_open")

        System_End_Program = 50
        System_i_AP = 60

    def ap_60( self ) :
        """
        ap_60 : Place on SR
        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_i_AP
        global thread
        ### Ende ###

        System_Start_Program = 60
        #mwait(0)
        #set_tcp(self.id_greifer_h)
        #thread_stop(thread)

        #tp_popup("IN ap_60 muss noch vervollständigt werden." , DR_PM_ALARM)
        self.c_modbus.get_set_output(self.c_modbus.id_rotary_gripper_grip_and_turn , "turn_bp_open")
        #self.c_vacuum.vacuum_control( id_RD , True )
        movej( Global_60_SR , r = self.big_blendRadius )
        System_Cur_Pos = 60
        movel(  System_61_SR , r = self.small_blendRadius )
        System_Cur_Pos = 61 
        movel(  System_62_SR , r = self.small_blendRadius )
        System_Cur_Pos = 62
        movel(  System_63_SR , r = self.no_blendRadius  , v = self.vel_ap)
        System_Cur_Pos = 63
        movel( Global_65_SR , r = self.no_blendRadius  , v = self.vel_ap)
        System_Cur_Pos = 65 
        #self.c_vacuum.vacuum_control( id_RD , True )
        self.c_modbus.get_set_output(self.c_modbus.id_rotary_gripper_grip_and_turn , "turn_bp_closed")

        if self.Simulation == 0 : 
            self.c_modbus.set_digital_output_wait_input( 8 , "go_bp" )

        System_End_Program = 60
        System_i_AP = 70

    def ap_70( self ) :
        """
        ap_70 : Pick from SR
        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_i_AP
        global thread
        ### Ende ###

        System_Start_Program = 70
        
        mwait(0)
        set_tcp(self.id_greifer_v)
        #thread_stop(thread)

        thread = thread_run(self.Thread_Turn_Wp_Closed , loop = False) 
           
        #self.c_modbus.get_set_output(self.c_modbus.id_rotary_gripper_grip_and_turn , "turn_wp_closed")
        movej( Global_70_SR , r = self.big_blendRadius )
        System_Cur_Pos = 70

        movel( ( System_71_SR ) , r = self.small_blendRadius )
        System_Cur_Pos = 71

        thread_stop(thread)

        set_digital_output(6)
        amovel( Global_75_SR , vel = self.vel_veryslow )
        self.c_modbus.stop_at_signal(self.c_modbus.id_venturi_vacuum_1 , "wp")
        System_Cur_Pos = 75 
        

        if self.Simulation == 0 :
            #self.c_modbus.set_digital_output_wait_input( 6 , "go_wp" )
            pass

        self.c_modbus.get_set_output(self.c_modbus.id_rotary_gripper_grip_and_turn , "turn_wp_open")
        #thread = thread_run(self.Thread_Handpress_Clam_Wp , loop = False)
        
        self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_wp")

        System_End_Program = 70
        System_i_AP = 80

    def ap_80( self ) :
        """
        ap_80 : Second place on SS1
        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_i_AP
        global thread 
        ### Ende ###

        System_Start_Program = 80
        #mwait(0)
        #set_tcp(self.id_greifer_v)
        #thread_stop(thread)

        thread = thread_run(self.Thread_Handpress_Clam_Wp , loop = False)
        
        #self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_wp")
        
        movej( Global_30_S1S , r = self.big_blendRadius )
        System_Cur_Pos = 30

        movel( ( System_81_S1S ) , r = self.small_blendRadius)
        System_Cur_Pos = 81

        movel( ( System_82_S1S ) , r = self.no_blendRadius , v = self.vel_ap / 3)
        System_Cur_Pos = 82
        #tp_popup("S")

        movel( Global_85_S1S , r = self.no_blendRadius , v = self.vel_ap / 4)
        System_Cur_Pos = 85 
        thread_stop(thread)
        

        if self.Simulation == 0 : 
            
            self.c_modbus.set_digital_output_wait_input( 6 , "go_bp" )
            set_digital_output( 7 , ON , 0.2 , OFF)
            #self.c_vacuum.vacuum( 10 , True)
            #self.c_vacuum.vacuum( id_RD , False)

        System_End_Program = 80
        System_i_AP = 40

    def ap_90( self ) :
        """
        ap_90 : Second Pick from SS1
        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_i_AP
        global thread
        ### Ende ###

        #thread_stop(thread)
        System_Start_Program = 90
        mwait(0)
        set_tcp(self.id_greifer_h)
        thread = thread_run(self.Thread_Handpress_Clam_Wp , loop = False)
        #self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_wp")
        

        movej( Global_30_S1S , r = self.big_blendRadius )
        System_Cur_Pos = 30
        movel( ( System_91_S1S ) , r = self.small_blendRadius )
        System_Cur_Pos = 91 
        movel( Global_95_S1S , r = self.no_blendRadius  , v = self.vel_ap)
        System_Cur_Pos = 95 
        thread_stop(thread)

        if self.Simulation == 0 :
            self.c_modbus.set_digital_output_wait_input( 8 , "go_wp" )

        System_End_Program = 90
        System_i_AP = 100

    def ap_100( self ) :
        """
        ap_100 : Place on ST
        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_i_AP
        global thread
        ### Ende ###

        System_Start_Program = 100
        #mwait(0)
        #set_tcp(self.id_greifer_h)
        #thread_stop(thread)

        #tp_popup("IN ap_100 muss noch vervollständigt werden." , DR_PM_ALARM)
        #set ST_Pos_SP = True  # Wahrscheinlich ist das ein Pulse 
        #set SP_H_GS = True # Wahrscheinlich ist das ein Pulse 

        movej( Global_100_ST , r = self.big_blendRadius )
        System_Cur_Pos = 100
        movel( ( System_101_ST ) , r = self.small_blendRadius )
        System_Cur_Pos = 101      
        movel( Global_105_ST , r = self.no_blendRadius  , v = self.vel_ap / 3)
        System_Cur_Pos = 105 

        if self.Simulation == 0 :
            self.c_modbus.set_digital_output_wait_input( 8 , "go_bp" )
            set_digital_output( 9 , ON , 0.2 , OFF)
            

        System_End_Program = 100
        System_i_AP = 110

    def ap_110( self ) :
        """
        ap_110 : Use lever of SS2
        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_i_AP
        global thread
        ### Ende ###

        System_Start_Program = 110
        mwait(0)
        set_tcp(self.id_kugelschnaepper)

        movej( Global_110_S2S , r = self.big_blendRadius )
        System_Cur_Pos = 110
        movel( ( System_111_S2S ) , r = self.small_blendRadius )
        System_Cur_Pos = 111 

        t = 0
        while True:
            wp , bp = self.c_modbus.get_status_signal(self.c_modbus.id_transfer_cylinder) 
            if wp == True :
                break
            elif t > self.timeout_restart:
                tp_popup("ap_110: Timeout, Transfert Train not in position" , DR_PM_ALARM)
                exit()
            else:
                wait(0.1)
                t += 0.1
        thread_stop(thread)
        movel( Global_115_S2S , r = self.no_blendRadius )
        System_Cur_Pos = 115 
        movec( Global_116_S2S , Global_117_S2S , time = self.t_lever )
        System_Cur_Pos = 117
        movec( Global_118_S2S , Global_119a_S2S , time = self.t_lever )
        System_Cur_Pos = 119
        
        movel( Global_119b_S2S , r = self.no_blendRadius)
        

        movec( Global_114_S2S , Global_113_S2S , time = self.t_lever )
        System_Cur_Pos = 113

        thread = thread_run(self.Thread_Packaging , loop = False)

        movec( Global_112_S2S , Global_115_S2S , time = self.t_lever )
        System_Cur_Pos = 115
        movel( ( System_111_S2S ) , r = self.small_blendRadius )
        System_Cur_Pos = 111 

        System_End_Program = 110
        System_i_AP = 10

    def moveout_ap_00(self):
        """
        moveout_ap_00 : Moves out of endposition of each ap 

        """

        ### Variabeln Deklarieren ###
        global System_Start_Program
        global System_Cur_Pos
        global System_End_Program
        global System_merker_pos
        global thread
        ### Ende ###

        #System_Start_Program = 0
        #self.c_functions.position_locator()
        
        if System_merker_pos == 1 :

            movej(Global_Home , r = self.no_blendRadius)
            System_Cur_Pos = 0
            System_merker_pos = 0

        if System_Cur_Pos == 0 :
            pass


        elif System_Cur_Pos == 10 :
            pass
        
        elif System_Cur_Pos == 11 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movej(Global_10_SM , r = self.small_blendRadius)
            System_Cur_Pos = 10

        elif System_Cur_Pos == 15 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movel(System_11_S1M , r = self.no_blendRadius , v = self.vel_ap )
            System_Cur_Pos = 11
            movej(Global_10_SM , r = self.small_blendRadius)
            System_Cur_Pos = 10
            

        elif System_Cur_Pos == 21 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movej(Global_10_SM , r = self.big_blendRadius)
            System_Cur_Pos = 10

        elif System_Cur_Pos == 25 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movel((System_21_S2M) , r = self.no_blendRadius , v = self.vel_ap )
            System_Cur_Pos = 21
            movej(Global_10_SM , r = self.small_blendRadius)
            System_Cur_Pos = 10


        elif System_Cur_Pos == 30 : 
            pass

        elif System_Cur_Pos == 31 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movej(Global_30_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 30

        elif System_Cur_Pos == 32 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movel(System_31_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 31
            movej(Global_30_S1S , r = self.big_blendRadius)
            System_Cur_Pos = 30

        elif System_Cur_Pos == 35 :
            mwait(0)
            set_tcp(self.id_greifer_v)
            movel(System_32_S1S , r = self.no_blendRadius , v = self.vel_ap)
            System_Cur_Pos = 32 

            if System_End_Program == 30 :

                self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_bp")
                if self.Simulation == 0 :
                    wait(0.5)
                    #thread = thread_run(self.Thread_Set_Output_S1S , loop = False)
                    
                    self.c_modbus.set_digital_output_wait_input( 10 , "go_wp" )

            movel(System_31_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 31
            movej(Global_30_S1S , r = self.big_blendRadius)
            System_Cur_Pos = 30
            #thread_stop(thread)


        elif System_Cur_Pos == 40 : 
            mwait(0)
            set_tcp(self.id_kugelschnaepper)
            movel(System_41_S1S , r = self.no_blendRadius)
            System_Cur_Pos = 41
            movej( Global_49_S1S , r = self.big_blendRadius )
            System_Cur_Pos = 49
        
        elif System_Cur_Pos == 41:
            movej( Global_49_S1S , r = self.big_blendRadius )
            System_Cur_Pos = 49
            
        elif System_Cur_Pos == 45 : 
            mwait(0)
            set_tcp(self.id_kugelschnaepper)
            movec( Global_47_S1S , Global_40_S1S , time = self.t_lever , ref = DR_WORLD)
            System_Cur_Pos = 40 
            movel( System_41_S1S , r = self.small_blendRadius , ref = DR_WORLD )
            System_Cur_Pos = 41 
            movej( Global_49_S1S , r = self.big_blendRadius )
            System_Cur_Pos = 49

        elif System_Cur_Pos == 47 : 
            mwait(0)
            set_tcp(self.id_kugelschnaepper)
            movec( Global_46_S1S , Global_40_S1S , time = self.t_lever )
            System_Cur_Pos = 40 
            movel( System_41_S1S , r = self.small_blendRadius , ref = DR_WORLD )
            System_Cur_Pos = 41 
            movej( Global_49_S1S , r = self.big_blendRadius )
            System_Cur_Pos = 49

        elif System_Cur_Pos == 49 :
            pass


        elif System_Cur_Pos == 51 : 
            mwait(0)
            set_tcp(self.id_greifer_h)
            movel( System_52_S1S , r = self.small_blendRadius , ref = DR_WORLD )
            System_Cur_Pos = 52
            movej(Global_30_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 30

        elif System_Cur_Pos == 52 : 
            mwait(0)
            set_tcp(self.id_greifer_h)
            movej(Global_30_S1S , r = self.big_blendRadius)
            System_Cur_Pos = 30

        elif System_Cur_Pos == 55 : 
            mwait(0)
            set_tcp(self.id_greifer_h)
            movel((System_51_S1S) , r = self.no_blendRadius , v = self.vel_ap)
            System_Cur_Pos = 51
            movel( System_52_S1S , r = self.no_blendRadius , ref = DR_WORLD  , v = self.vel_ap)
            System_Cur_Pos = 52
            movej(Global_30_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 30

        elif System_Cur_Pos == 56 : 
            mwait(0)
            set_tcp(self.id_greifer_h)
            movej(Global_30_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 30


        elif System_Cur_Pos == 60 : 
            pass

        elif System_Cur_Pos == 61 :
            mwait(0)
            set_tcp(self.id_greifer_h) 
            movej(Global_60_SR , r = self.small_blendRadius)
            System_Cur_Pos = 60

        elif System_Cur_Pos == 62:
            mwait(0)
            set_tcp(self.id_greifer_h)
            movel(  System_61_SR , r = self.small_blendRadius )
            System_Cur_Pos = 61
            movej(Global_60_SR , r = self.small_blendRadius)
            System_Cur_Pos = 60 

        elif System_Cur_Pos == 63:
            mwait(0)
            set_tcp(self.id_greifer_h)
            movel(  System_62_SR , r = self.small_blendRadius )
            System_Cur_Pos = 62
            movel(  System_61_SR , r = self.small_blendRadius )
            System_Cur_Pos = 61
            movej(Global_60_SR , r = self.small_blendRadius)
            System_Cur_Pos = 60           

        elif System_Cur_Pos == 65 : 
            mwait(0)
            set_tcp(self.id_greifer_h)
            movel((System_66_SR) , r = self.no_blendRadius , v = self.vel_ap)
            System_Cur_Pos = 66
            movej(Global_60_SR , r = self.small_blendRadius)
            System_Cur_Pos = 60
            #thread = thread_run(self.Thread_Turn_Wp_Closed , loop = False)
            self.c_modbus.get_set_output(self.c_modbus.id_rotary_gripper_grip_and_turn , "turn_wp_closed")
                 
        elif System_Cur_Pos == 66:
            mwait(0)
            set_tcp(self.id_greifer_h) 
            movej(Global_60_SR , r = self.small_blendRadius)
            System_Cur_Pos = 60


        elif System_Cur_Pos == 70 : 
            pass

        elif System_Cur_Pos == 71 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movej(Global_70_SR , r = self.small_blendRadius)
            System_Cur_Pos = 70

        elif System_Cur_Pos == 75 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movel((System_76_SR) , r = self.no_blendRadius , v = self.vel_ap)
            System_Cur_Pos = 76
            thread = thread_run(self.Thread_Turn_Bp_Open , loop = False)
            movel((System_77_SR) , r = self.small_blendRadius)
            System_Cur_Pos = 77
            movej(Global_70_SR , r = self.small_blendRadius)
            System_Cur_Pos = 70
            thread_stop(thread)

        elif System_Cur_Pos == 76 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movel((System_77_SR) , r = self.no_blendRadius)
            System_Cur_Pos = 77
            movej(Global_70_SR , r = self.small_blendRadius)
            System_Cur_Pos = 70

        elif System_Cur_Pos == 77 :
            mwait(0)
            set_tcp(self.id_greifer_v)
            movej(Global_70_SR , r = self.small_blendRadius)
            System_Cur_Pos = 70


        elif System_Cur_Pos == 81 :
            mwait(0)
            set_tcp(self.id_greifer_v)
            movej(Global_30_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 30

        elif System_Cur_Pos == 82 :
            mwait(0)
            set_tcp(self.id_greifer_v)
            movel(System_81_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 81
            movej(Global_30_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 30

        elif System_Cur_Pos == 85 : 
            mwait(0)
            set_tcp(self.id_greifer_v)
            movel(System_82_S1S , r = self.no_blendRadius , v = self.vel_ap)
            System_Cur_Pos = 82  

            #if System_End_Program == 80 :
            #    self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_bp")
            #    if self.Simulation == 0 :
            #        wait(0.2)
            #        self.c_modbus.set_digital_output_wait_input( 10 , "go_wp" )  
            
            self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_bp")
            
            if self.Simulation == 0 :
                wait(0.5)
                thread = thread_run(self.Thread_Set_Output_S1S , loop = False)
                #self.c_modbus.set_digital_output_wait_input( 10 , "go_wp" )

            movel(System_86_S1S , r = self.no_blendRadius)
            System_Cur_Pos = 86 

            movel(System_81_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 81
            movej(Global_30_S1S , r = self.big_blendRadius)
            System_Cur_Pos = 30
            thread_stop(thread)

        elif System_Cur_Pos == 86 :
            movel(System_81_S1S , r = self.small_blendRadius)
            System_Cur_Pos = 81
            movej(Global_30_S1S , r = self.big_blendRadius)
            System_Cur_Pos = 30


        elif System_Cur_Pos == 91 : 
            movej(Global_30_S1S , r = self.big_blendRadius)
            System_Cur_Pos = 30

        elif System_Cur_Pos == 96 : 
            movej(Global_30_S1S , r = self.big_blendRadius)
            System_Cur_Pos = 30

        elif System_Cur_Pos == 95 :
            mwait(0)
            set_tcp(self.id_greifer_h) 
            movel((System_96_S1S) , r = self.no_blendRadius , v = self.vel_ap)
            System_Cur_Pos = 96
            movej(Global_30_S1S , r = self.big_blendRadius)
            System_Cur_Pos = 30


        elif System_Cur_Pos == 100 : 
            pass

        elif System_Cur_Pos == 101 :
            movej(Global_100_ST , r = self.big_blendRadius)
            System_Cur_Pos = 100

        elif System_Cur_Pos == 105 : 
            mwait(0)
            set_tcp(self.id_greifer_h)
            movel((System_101_ST) , r = self.no_blendRadius , v = self.vel_ap)
            System_Cur_Pos = 101

            if System_End_Program == 100:
                thread = thread_run(self.Thread_Train_to_Wp , loop = False)
            mwait(0)
            set_tcp(self.id_greifer_h)  
            movej(Global_100_ST , r = self.big_blendRadius)
            System_Cur_Pos = 100
            #thread_stop(thread)


        elif System_Cur_Pos == 110 : 
            pass

        elif System_Cur_Pos == 111 : 
            movej(Global_110_S2S , r = self.big_blendRadius)
            System_Cur_Pos = 110
            pass

        elif System_Cur_Pos == 115 : 
            #movel(relative_mvt(Global_115_S2S))
            #System_Cur_Pos = 111
            #movej(Global_110_S2S , r = self.big_blendRadius)
            #System_Cur_Pos = 110
            pass

        elif System_Cur_Pos == 117 : 
            #movec( Global_116_S2S , Global_115_S2S , time = constants.Global_t_lever )
            #System_Cur_Pos = 115 
            #movel( relative_mvt( Global_115_S2S ) )
            #System_Cur_Pos = 111 
            #movej( Global_110_S2S , r = self.big_blendRadius)
            #System_Cur_Pos = 110
            pass 

        else :
            System_merker_pos = 1
            tp_popup("I lost my position, please put me in a position so i can Home", DR_PM_ALARM)
            exit()

    def restart(self):
        
        global System_i_AP
        global System_i_Step
        global thread
        global System_Start_Program
        global System_End_Program
        global System_Drive_Free
        global user_input

        control_voltage = False
        air_ok = False
        control_air_ok = False
        sick_laser_error = True 
        t = 0 
        self.c_calc.calc_positions()
        set_digital_output(5) # Main Air
        set_digital_output(-2) # Sick Config ffür Stanze

        while True : 


            if not get_digital_input(1):
                control_voltage = True 
            else:
                self.c_error.disturbance_message(8 , "controle_voltage")
                pass

            if get_digital_input(2):
                air_ok = True 
            else:
                wait_air = wait_digital_input( 2 , ON , 5)
                if wait_air == 0 :
                    air_ok = True 
                else:
                    self.c_error.disturbance_message(8 , "Air")
                    

            if not get_digital_input(3):
                control_air_ok = True 
            else:
                self.c_error.disturbance_message(8 , "control_air")    
                pass

            if not get_digital_input(6):
                sick_laser_error = False 
            else:
                set_digital_output( 1 , ON , 0.5 , OFF)
                if get_digital_input(6):
                    self.c_error.disturbance_message(9 , "sick_laser_error") 
                    pass

            if control_voltage ==  True and air_ok == True and control_air_ok == True and sick_laser_error == False:
                thread_Stoerung = thread_run(self.Thread_Stoerungsmanagment , loop = True)
                break
            else:
                wait(0.1)
                t = t + 0.1

            if t > self.timeout_restart:
                self.c_error.disturbance_message(10 , "restart")

        #Controle if the right tool is mounted
        force_ext = get_tool_force(DR_WORLD)
        force_ext_abs = sqrt( pow(force_ext[0],2) + pow(force_ext[1],2) + pow(force_ext[2],2))

        if force_ext_abs > 15 :

            #user_input = tp_get_user_input( "Is the right tool mounted on the robot ?" , input_type =DR_VAR_BOOL)
            right_tool()

            if user_input :
                tp_popup("The smaller tool needs to be mounted !!!" , DR_PM_ALARM)
            else : 
                set_digital_output(-5)
                exit()

        if System_i_Step != 0 and System_i_AP != 10:
            
            restart_variables()
            #user_input = tp_get_user_input( "Restart all variables ?" , input_type = DR_VAR_BOOL)
        else :
            user_input = 1
        
        if user_input :
            
            self.c_modbus.move_all("bp")
            self.c_modbus.set_digital_output_wait_input(6 , "go_bp")
            self.c_modbus.set_digital_output_wait_input( 8 , "go_bp" )
            self.c_modbus.set_digital_output_wait_input( 10 , "go_bp" )
            self.c_modbus.set_digital_output_wait_input( 13 , "go_bp" )
            set_digital_output( 7 , OFF)
            set_digital_output( 9 , OFF)
            set_digital_output( 11 , OFF)
            set_digital_output( 14 , OFF)

            System_Start_Program = 110
            System_End_Program = 110
            System_i_AP = 10
            System_i_Step = 0

        else :
            #thread = thread_run(self.Thread_Nothing , loop = False)
            #self.c_modbus.move_all("restart")
            pass

        #Check if robot is at a known position
        

        if System_Drive_Free == 0:
            self.c_functions.position_locator()
            if System_Cur_Pos ==  47 or System_Cur_Pos == 45 or System_Cur_Pos == 117 or System_Cur_Pos == 119 or System_Cur_Pos == 113 :
                tp_popup("Please take me out of the lever and place me close to Home " , DR_PM_ALARM)
                System_Drive_Free = 1
                exit()
            elif System_Cur_Pos == 40 or System_Cur_Pos == 115 :
                user_input = tp_get_user_input( "Am I in endposition and Can I drive Home ? " , input_type =DR_VAR_BOOL)
                if not user_input :
                    tp_popup("Please take me out of the lever and place me close to Home " , DR_PM_ALARM)
                    System_Drive_Free = 1
                    exit()
                    
            elif System_Cur_Pos == "unkown":
                #tp_popup("Place me close to Home " , DR_PM_ALARM)
                System_Drive_Free = 1

        elif System_Drive_Free == 1:
            change_operation_speed(15)
            movej(Global_Home , r= self.no_blendRadius)
            change_operation_speed(self.override)
            System_Drive_Free = 0

    def Thread_Stoerungsmanagment( self ):
        global Global_Disturbance
        global Global_No_Parts

        SM_Sensor_Left , bp = self.c_modbus.get_status_signal(self.c_modbus.id_inlet_sensor_left)
        SM_Sensor_Right , bp = self.c_modbus.get_status_signal(self.c_modbus.id_inlet_sensor_right)

        if not SM_Sensor_Left and not SM_Sensor_Right and System_End_Program == 110:
          Global_Disturbance = 1 
          Global_No_Parts = 1
        elif get_digital_input(1) :    
            Global_Disturbance = 1 
            self.c_error.disturbance_message(8 , "controle_voltage")
        elif not get_digital_input(2) :
            Global_Disturbance = 1 
            self.c_error.disturbance_message(8 , "Air")
        elif get_digital_input(3):
            Global_Disturbance = 1 
            self.c_error.disturbance_message(8 , "control_air")    
        elif not get_digital_input(4):
            Global_Disturbance = 1 
            self.c_error.disturbance_message(8 , "24 V")  
        elif get_digital_input(6):
            Global_Disturbance = 1 
            self.c_error.disturbance_message(9 , "sick_laser_error")
        else:
            Global_Disturbance = 0 
            Global_No_Parts = 0
   
    def Thread_Packaging (self):

        if System_Start_Program == 110:

            self.c_modbus.get_set_output(self.c_modbus.id_stroke_horizontal_cylinder,"go_bp")
            self.c_modbus.get_set_output(self.c_modbus.id_stroke_verticale_cylinder,"go_wp")
            self.c_modbus.get_set_output(self.c_modbus.id_transfer_cylinder,"go_bp")

            self.c_modbus.get_set_output(self.c_modbus.id_stroke_horizontal_cylinder,"go_wp")
            self.c_modbus.get_set_output(self.c_modbus.id_stroke_verticale_cylinder,"go_bp")
            if self.Simulation == 0:
                self.c_modbus.set_digital_output_wait_input( 13 , "go_wp" )

            
            self.c_modbus.get_set_output(self.c_modbus.id_stroke_verticale_cylinder,"go_wp")
            self.c_modbus.get_set_output(self.c_modbus.id_stroke_horizontal_cylinder,"go_bp")
            self.c_modbus.get_set_output(self.c_modbus.id_stroke_verticale_cylinder,"go_bp")

            if self.Simulation == 0:
                self.c_modbus.set_digital_output_wait_input( 13 , "go_bp" )
                set_digital_output( 14 , ON , 0.2 , OFF)

        elif System_End_Program == 100:

            self.c_modbus.get_set_output(self.c_modbus.id_transfer_cylinder,"go_wp")

        elif System_Start_Program == 30 : 
            self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_wp")

    def Thread_Modbus(self):
        pass
    def Thread_Train_to_Wp(self):
        self.c_modbus.get_set_output(self.c_modbus.id_transfer_cylinder,"go_wp")

    def Thread_Turn_Wp_Closed(self):
        self.c_modbus.get_set_output(self.c_modbus.id_rotary_gripper_grip_and_turn , "turn_wp_closed")

    def Thread_Turn_Bp_Open(self):
        self.c_modbus.get_set_output(self.c_modbus.id_rotary_gripper_grip_and_turn , "turn_bp_open")

    def Thread_Handpress_Clam_Wp(self):
        self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_wp")

    def Thread_Handpress_Clam_Bp(self):
        self.c_modbus.get_set_output(self.c_modbus.id_handpress_clam,"go_bp")

    def Thread_Set_Output_S1S(self):
        self.c_modbus.set_digital_output_wait_input( 10 , "go_wp" )
 
    def Thread_Nothing(self):
        pass

#####################################

class runtime():

    global System_i_Step
    global Global_Disturbance
    global System_Cur_Pos

    def __init__(self) -> None:

        self.timeout = 2
        self.c_vacuum = vacuum()
        self.c_functions = functions()
        self.c_error = error()
        self.c_AP = ap()
        self.c_modbus = modbus(
                D1 , 
                pneumatic , 
                DI_Signals , 
                handpress_clam , 
                rotary_gripper_turn , 
                rotary_gripper , 
                rotary_gripper_grip_and_turn ,
                stroke_horizontal_cylinder , 
                stroke_verticale_cylinder , 
                transfer_cylinder , 
                taster_cylinder , 
                test_head ,
                inlet_sensor_left , 
                inlet_sensor_right ,
                venturi_vacuum_1 , 
                venturi_vacuum_2 , 
                venturi_vacuum_3 , 
                venturi_vacuum_4 ) 
        pass

    def flow_logic(self):
        """
        #The flow contains eleven steps.
        #After a restart we are at step 0
        # Step 0  : Restart 
        # Step 1  : Pick Part SM
        # Step 2  : Place Part S1S
        # Step 3  : Push Lever 1
        # Step 4  : Pick Part S1S
        # Step 5  : Place Part Gripper
        # Step 6  : Pick Part Gripper
        # Step 7  : Place Part S1S
        # Step 8  : Push Lever 1
        # Step 9  : Pick Part
        # Step 10 : Place Part Train
        # Step 11 : Push Lever 2
        """

        ### Variabeln Deklarieren ###
        global System_i_Step
        ### Ende ###
        t = 0
        while True :

            if System_i_Step == 0 or System_i_Step == 11:
                #Conditions to enter in Step 1:
                #Robot is empty 
                #Station_SM has parts
                
                if System_i_AP == 10 :  

                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_1 ) #True when Robot is empty
                    if wp == True :
                        tp_popup("Robot has already a part FL_1",DR_PM_ALARM)
                        exit()
                    if self.c_functions.fifo() != -1 : #-1=No Part present 
                        System_i_Step = 1 #ap10
                        break
                    else:
                        #NCV
                        raise DR_Error(DR_ERROR_TYPE, "Problem at flow_logic Step 1")                
                else : 
                    System_i_Step = 10

            elif System_i_Step == 1:
                #Conditions to enter in Step 2:
                #Robot has part
                #Station_S1S is empty  

                if System_i_AP == 30 :

                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_1 ) #True when Robot is empty
                    if bp == True :
                        tp_popup("Robot has no part FL_2",DR_PM_ALARM)
                        exit()
                    #self.c_vacuum.vacuum_control( id_S1S , False ) #True when S1S has no part
                    wp , bp = self.c_modbus.get_status_signal(self.c_modbus.id_venturi_vacuum_3)
                    if wp == True :
                        tp_popup("Problem at flow_logic : Step 2" , DR_PM_ALARM)
                        exit()
                    System_i_Step = 2 #ap30
                    break
                else:
                    System_i_Step = 11

            elif System_i_Step == 2:
                #Conditions to enter in Step 3:
                #Robot has no part
                #Station_S1S has part

                if System_i_AP == 40 :
                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_1 ) #True when Robot is empty
                    if wp == True :
                        tp_popup("Robot has  a part FL_3",DR_PM_ALARM)
                        exit()

                    wp , bp = self.c_modbus.get_status_signal(self.c_modbus.id_venturi_vacuum_3)
                    if bp == True :
                        tp_popup("Problem at flow_logic : Step 3" , DR_PM_ALARM)
                        exit()
                    System_i_Step = 3
                    break
                else:
                    System_i_Step = 1

            elif System_i_Step == 3:
                #Conditions to enter in Step 4:
                #Robot has no part
                
                if System_i_AP == 50 :
                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_1 ) #True when Robot is empty
                    if wp == True :
                        tp_popup("Robot has already a part FL_4",DR_PM_ALARM)
                        exit() 
                    
                    System_i_Step = 4 #ap50
                    break
                else:
                    System_i_Step = 2

            elif System_i_Step == 4:
                #Conditions to enter in Step 5:
                #Schunk Gripper is open
                #Schunk Gripper is turned to 0 Degrees
                #Robot has a part 

                if System_i_AP == 60 :
                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_2 ) #True when Robot is empty
                    if bp == True :
                        tp_popup("Robot has no part: Step 5",DR_PM_ALARM)
                        exit()

                    while True :
                        status_rotary_gripper = self.c_modbus.get_status_rotary_gripper()
                        if status_rotary_gripper == "bp_open":
                            break
                        elif t > self.timeout:
                            tp_popup("Problem at flow_logic : Step 5" , DR_PM_ALARM)
                            exit()
                        else:
                            wait(0.1)
                            t = t + 0.1
                    
                    System_i_Step = 5
                    break
                else :
                    System_i_Step = 3

            elif System_i_Step == 5:
                #Conditions to enter in Step 6:
                #Schunk Gripper is closed
                #Schunk Gripper is turned to 180 Degrees
                #Robot has no part 

                if System_i_AP == 70 :
                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_1  ) #True when Robot is empty
                    if wp == True :
                        tp_popup("Robot has  a part FL_6",DR_PM_ALARM)
                        exit()
                    t = 0
                    while True: 
                        status_rotary_gripper = self.c_modbus.get_status_rotary_gripper()
                        if status_rotary_gripper == "wp_closed":
                            break
                        elif t > self.timeout :
                            tp_popup("Problem at flow_logic : Step 6" , DR_PM_ALARM)
                            exit()
                        else:
                            wait(0.1)
                            t = t + 0.1
                    
                    System_i_Step = 6
                    break
                else:
                    System_i_Step = 4

            elif System_i_Step == 6:
                #Conditions to enter in Step 7:
                #Robot has part
                #Station_S1S is empty 

                if System_i_AP == 80 :
                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_1 ) #True when Robot is empty
                    if bp == True :
                        tp_popup("Robot has no part: Step 7",DR_PM_ALARM)
                        exit() 

                    wp , bp = self.c_modbus.get_status_signal(self.c_modbus.id_venturi_vacuum_3)
                    if wp == True :
                        tp_popup("Problem at flow_logic : Step 7" , DR_PM_ALARM)
                        exit()
                    System_i_Step = 7
                    break
                else:
                    System_i_Step = 5

            elif System_i_Step == 7:
                #Conditions to enter in Step 8:
                #Robot has no part
                
                if System_i_AP == 40 :
                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_2 ) #True when Robot is empty
                    if wp == True :
                        tp_popup("Robot has  a part FL_8",DR_PM_ALARM)
                        exit()

                    wp , bp = self.c_modbus.get_status_signal(self.c_modbus.id_venturi_vacuum_3)
                    if wp == False :
                        tp_popup("Problem at flow_logic : Step 8" , DR_PM_ALARM)
                        exit()
                    System_i_Step = 8 #ap40
                    break
                else:
                    System_i_Step = 6

            elif System_i_Step == 8:
                #Conditions to enter in Step 9:
                #Robot has no part

                if System_i_AP == 90 :
                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_2 ) #True when Robot is empty
                    if bp == False :
                        tp_popup("Robot has  a part FL_9",DR_PM_ALARM)
                        exit()
                    System_i_Step = 9
                    break
                else:
                    System_i_Step = 7

            elif System_i_Step == 9:
                #Conditions to enter in Step 10:
                #Station Train in Position: ST_Pos_SP
                #Station Packaging in GS ( Avoid colision while placing part on train )
                #Robot has part
                #NCV

                if System_i_AP == 100 :
                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_2 ) #True when Robot is empty
                    if wp == False :
                        tp_popup("Robot has no part : Step 10",DR_PM_ALARM)
                        exit() 

                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_stroke_horizontal_cylinder ) #True when Robot is empty
                    if bp == False :
                        tp_popup("stroke_horizontal_cylinder not in Position: Step 10",DR_PM_ALARM)
                        exit() 

                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_stroke_verticale_cylinder ) #True when Robot is empty
                    if bp == False :
                        tp_popup("stroke_verti_cylinder not in Position: Step 10",DR_PM_ALARM)
                        exit() 

                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_transfer_cylinder ) #True when Robot is empty
                    if bp == False :
                        tp_popup("transfer cylinder not in Position: Step 10",DR_PM_ALARM)
                        exit() 
                    
                    System_i_Step = 10
                    break
                else:
                    System_i_Step = 8
                
            elif System_i_Step == 10:
                #Conditions to enter in Step 11:
                #Robot has no part
                #Station Train in Position: ST_Pos_S2S 
                #NCV
                #tp_popup("Flow_Logic step 10 needs to be completed!" , DR_PM_ALARM)

                if System_i_AP == 110 :
                    wp , bp = self.c_modbus.get_status_signal( self.c_modbus.id_venturi_vacuum_1 ) #True when Robot is empty
                    if wp == True :
                        tp_popup("Robot has  a part",DR_PM_ALARM)
                        exit() 
                    
                    """
                    t = 0
                    while True:
                        wp , bp = self.c_modbus.get_status_signal(self.c_modbus.id_transfer_cylinder) 
                        if wp == True :
                            break
                        elif t > self.timeout:
                            tp_popup("Problem at flow_logic : Step 11" , DR_PM_ALARM)
                            exit()
                        else:
                            wait(0.1)
                            t += 0.1
                    """
                    System_i_Step = 11
                    break
                else:
                    System_i_Step = 9
            if t > self.timeout :
                tp_popup("Please restart Variables",DR_PM_ALARM)
                exit()
            else:
                wait(0.1)
                t += 0.1    

    def flow_management(self):
        """
        """
        ### Variabeln Deklarieren ###
        global Global_Disturbance 
        ### Ende ###

        if System_i_Step == 1:

            if System_i_AP > 0 :
                self.c_AP.ap_10()
                #ap_010_SM_Pick()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 2 : 

            if System_i_AP == 30 :
                self.c_AP.ap_30()
                #ap_030_SS1_Place()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 3 : 

            if System_i_AP == 40 :
                self.c_AP.ap_40()
                #ap_040_SS1_Lever()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 4 : 

            if System_i_AP == 50 :
                self.c_AP.ap_50()
                #ap_050_SS1_Pick1()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 5 : 

            if System_i_AP == 60 :
                self.c_AP.ap_60()
                #ap_060_SR_Place()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 6 : 

            if System_i_AP == 70 :
                self.c_AP.ap_70()
                #ap_070_SR_Pick()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 7 :

            if System_i_AP == 80 :
                self.c_AP.ap_80()
                #ap_080_SS1_Place_2()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 8 : 

            if System_i_AP == 40 :
                self.c_AP.ap_40()
                #ap_040_SS1_Lever()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 9 : 

            if System_i_AP == 90 :
                self.c_AP.ap_90()
                #ap_090_SS1_Pick2()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 10 : 

            if System_i_AP == 100 :
                self.c_AP.ap_100()
                #ap_100_ST_Place()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)

        elif System_i_Step == 11 : 
            if System_i_AP == 110 :
                self.c_AP.ap_110()
                #ap_110_SS2_Lever()
            else :
                Global_Disturbance = 1
                self.c_error.disturbance_message(5)
        else : 
            Global_Disturbance = 1 
            raise DR_Error(DR_ERROR_TYPE, "Problem at flow_managment")

    def automatic_mode(self):
        self.c_AP.restart()
        self.c_AP.moveout_ap_00()
        while True :
            if Global_Disturbance == 0:
                self.flow_logic()
                self.flow_management()
                self.c_AP.moveout_ap_00()
            else:
                if Global_No_Parts == 1 :
                  movej(Global_Home)
                  System_Cur_Pos == 0

#####################################

class functions() : 

    def __init__(self , plausibility_check_X_Min = 0 , plausibility_check_X_Max = 0 , plausibility_check_Y_Min = 0 , plausibility_check_Y_Max = 0 , plausibility_check_Z_Min = 0 , plausibility_check_Z_Max = 0 ) :
        self.plausibility_check_X_Min = plausibility_check_X_Min
        self.plausibility_check_X_Max = plausibility_check_X_Max
        self.plausibility_check_Y_Min = plausibility_check_Y_Min
        self.plausibility_check_Y_Max = plausibility_check_Y_Max
        self.plausibility_check_Z_Min = plausibility_check_Z_Min
        self.plausibility_check_Z_Max = plausibility_check_Z_Max
        self.c_drive = drive()
        self.c_error = error()
        self.c_modbus = modbus(
                    D1 , 
                    pneumatic , 
                    DI_Signals , 
                    handpress_clam , 
                    rotary_gripper_turn , 
                    rotary_gripper , 
                    rotary_gripper_grip_and_turn ,
                    stroke_horizontal_cylinder , 
                    stroke_verticale_cylinder , 
                    transfer_cylinder , 
                    taster_cylinder , 
                    test_head ,
                    inlet_sensor_left , 
                    inlet_sensor_right ,
                    venturi_vacuum_1 , 
                    venturi_vacuum_2 , 
                    venturi_vacuum_3 , 
                    venturi_vacuum_4 ) 

    def plausibility_check(self , check_pos):
        """
        plausibility_check checks of passed position is valid .

        :param check_pos [posx]: position which should be checked

        :return: True/False
        """ 
        if (check_pos[0] < self.plausibility_check_X_Min):
            return False
        elif (check_pos[0] > self.plausibility_check_X_Max):
            return False
        elif (check_pos[1] < self.plausibility_check_Y_Min):
            return False
        elif (check_pos[1] > self.plausibility_check_Y_Max):
            return False
        elif (check_pos[2] < self.plausibility_check_Z_Min):
            return False
        elif (check_pos[2] > self.plausibility_check_Z_Max):
            return False
        else:
            return True

    def fifo(self):
        """
        fifo =  First In First Out.

        :return: Pick side
        """ 
        ### Variabeln Deklarieren ###
        global System_SM_Side
        global Global_Disturbance
        global Global_No_Parts 
        #NC
        #tp_popup("[fifo] Hier muss noch was vervollstandiegt werden ")
        SM_Sensor_Left , bp = self.c_modbus.get_status_signal(self.c_modbus.id_inlet_sensor_left)
        #tp_popup("SM_Sensor_Left = {0}".format(SM_Sensor_Left),DR_PM_ALARM)
        SM_Sensor_Right , bp = self.c_modbus.get_status_signal(self.c_modbus.id_inlet_sensor_right)
        #tp_popup("SM_Sensor_Right = {0}".format(SM_Sensor_Right),DR_PM_ALARM)

        ### Ende ###
        Global_No_Parts = 0

        if System_SM_Side == 1 :

            if SM_Sensor_Left == 1 :
                System_SM_Side = 1
            elif SM_Sensor_Right == 1 : 
                System_SM_Side = 0
            else : 
                System_SM_Side = -1
                Global_Disturbance = 1
                Global_No_Parts = 1
                self.c_error.disturbance_message(4)

        elif System_SM_Side == 0 : 

            if SM_Sensor_Left == 1 :
                System_SM_Side = 1
            elif SM_Sensor_Right == 1 : 
                System_SM_Side = 0
            else : 
                System_SM_Side = -1 
                Global_Disturbance = 1
                Global_No_Parts = 1
                self.c_error.disturbance_message(4)

        elif System_SM_Side == -1 :

            if SM_Sensor_Left == 1 :
                System_SM_Side = 1
            elif SM_Sensor_Right == 1 : 
                System_SM_Side = 0
            else : 
                System_SM_Side = -1 
                Global_Disturbance = 1
                Global_No_Parts = 1
                self.c_error.disturbance_message(4)
                
        return System_SM_Side

    def check_position( self , cur_pos , comparison_pos , radius = 30 ):
        
        """
        check_position checks if cur_pos is within a sphere with radius around the position comparison_pos  .

        :param cur_pos [posx]: position which should be checked
        :param comparison_pos [posx]: position to wchich cur_pos should be checked 
        :param radius [mm]: Sphere raduis 

        :return: True/False
        """ 
        x = comparison_pos[0]
        y = comparison_pos[1]
        z = comparison_pos[2]
        x_c = cur_pos[0]
        y_c = cur_pos[1]
        z_c = cur_pos[2]

        test = pow((x - x_c),2) + pow((y - y_c),2) + pow((z - z_c),2)
        r = pow(radius , 2)
        if test < r :
            return True 
        else :
            return False 

    def position_locator(self , l_checkPosRadius = 25 ):
        """
        posoition locator : this methods checks if the robot is
        currently on a place whick he knows.

        return: System_Cur_Pos  
        """

        ### Variabeln Deklarieren ###
        global System_Cur_Pos 

        ### Ende ###

        cur_pos,sol = get_current_posx(ref=DR_WORLD)

        merker = 0

        if self.check_position( cur_pos , System_11_S1M , l_checkPosRadius ) :

            System_Cur_Pos = 11
            merker = 1 

        elif self.check_position( cur_pos , System_21_S2M , l_checkPosRadius ) :
            System_Cur_Pos = 21 
            merker = 1 
        
        elif self.check_position( cur_pos , System_25_S2M  , l_checkPosRadius ):
            System_Cur_Pos = 25
            merker = 1
        
        elif self.check_position( cur_pos , System_31_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 31
            merker = 1

        elif self.check_position( cur_pos , System_32_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 32
            merker = 1

        elif self.check_position( cur_pos , System_41_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 41
            merker = 1

        elif self.check_position( cur_pos , System_51_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 51
            merker = 1

        elif self.check_position( cur_pos , System_52_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 52
            merker = 1

        elif self.check_position( cur_pos , System_56_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 56
            merker = 1

        elif self.check_position( cur_pos , System_61_SR , 2 ) :
            System_Cur_Pos = 61
            merker = 1 

        elif self.check_position( cur_pos , System_62_SR , 2 ) :
            System_Cur_Pos = 62
            merker = 1 

        elif self.check_position( cur_pos , System_63_SR , 2 ) :
            System_Cur_Pos = 63
            merker = 1 
        
        elif self.check_position( cur_pos , System_66_SR , 2 ) :
            System_Cur_Pos = 66
            merker = 1 

        elif self.check_position( cur_pos , System_71_SR , 2 ) :
            System_Cur_Pos = 71
            merker = 1 

        elif self.check_position( cur_pos , System_76_SR , 2 ) :
            System_Cur_Pos = 76
            merker = 1 

        elif self.check_position( cur_pos , System_77_SR , 2 ) :
            System_Cur_Pos = 77
            merker = 1 

        elif self.check_position( cur_pos , System_81_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 81
            merker = 1

        elif self.check_position( cur_pos , System_82_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 82
            merker = 1

        elif self.check_position( cur_pos , System_86_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 86
            merker = 1

        elif self.check_position( cur_pos , System_91_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 91
            merker = 1 

        elif self.check_position( cur_pos , System_96_S1S , l_checkPosRadius ) :
            System_Cur_Pos = 96
            merker = 1

        elif self.check_position( cur_pos , System_101_ST , l_checkPosRadius ) :
            System_Cur_Pos = 101
            merker = 1

        elif self.check_position( cur_pos , System_111_S2S , l_checkPosRadius ) :
            System_Cur_Pos = 111
            merker = 1


        elif self.check_position( cur_pos , (Global_15_S1M)  , l_checkPosRadius ):
            System_Cur_Pos = 15
            merker = 1

        elif self.check_position( cur_pos , (Global_35_S1S)  , l_checkPosRadius ):
            System_Cur_Pos = 35
            merker = 1

        elif self.check_position( cur_pos , (Global_40_S1S)  , l_checkPosRadius ):
            System_Cur_Pos = 40
            merker = 1

        elif self.check_position( cur_pos , (Global_45_S1S)  , l_checkPosRadius ):
            System_Cur_Pos = 45
            merker = 1

        elif self.check_position( cur_pos , (Global_47_S1S)  , l_checkPosRadius ):
            System_Cur_Pos = 47
            merker = 1

        elif self.check_position( cur_pos , (Global_55_S1S)  , l_checkPosRadius ):
            System_Cur_Pos = 55
            merker = 1

        elif self.check_position( cur_pos , (Global_65_SR)  , 2 ):
            System_Cur_Pos = 65
            merker = 1

        elif self.check_position( cur_pos , (Global_75_SR)  , 2 ):
            System_Cur_Pos = 75
            merker = 1

        elif self.check_position( cur_pos , (Global_85_S1S)  , l_checkPosRadius ):
            System_Cur_Pos = 85
            merker = 1

        elif self.check_position( cur_pos , (Global_95_S1S)  , l_checkPosRadius ):
            System_Cur_Pos = 95
            merker = 1

        elif self.check_position( cur_pos , (Global_105_ST)  , l_checkPosRadius ):
            System_Cur_Pos = 105
            merker = 1

        elif self.check_position( cur_pos , (Global_115_S2S)  , l_checkPosRadius ):
            System_Cur_Pos = 115
            merker = 1
        
        elif self.check_position( cur_pos , (Global_113_S2S) , l_checkPosRadius ):
            System_Cur_Pos = 113
            merker= 1

        elif self.check_position( cur_pos , (Global_117_S2S) , l_checkPosRadius ):
            System_Cur_Pos = 117 
            merker= 1

        elif self.check_position( cur_pos , (Global_119a_S2S) , l_checkPosRadius ):
            System_Cur_Pos = 119 
            merker= 1

        elif self.check_position( cur_pos , (Global_119b_S2S) , l_checkPosRadius ):
            System_Cur_Pos = 119 
            merker= 1


        elif self.check_position( cur_pos , fkin(Global_Home , DR_WORLD)    , l_checkPosRadius ):
            System_Cur_Pos = 0
            merker = 1

        elif self.check_position( cur_pos , fkin(Global_10_SM , DR_WORLD)   , l_checkPosRadius ):
            System_Cur_Pos = 10
            merker = 1

        elif self.check_position( cur_pos , fkin(Global_30_S1S , DR_WORLD)  , l_checkPosRadius ):
            System_Cur_Pos = 30
            merker = 1

        elif self.check_position( cur_pos , fkin(Global_49_S1S , DR_WORLD)  , l_checkPosRadius ):
            System_Cur_Pos = 49
            merker = 1

        elif self.check_position( cur_pos , fkin(Global_60_SR , DR_WORLD)  , 2 ):
            System_Cur_Pos = 60
            merker = 1

        elif self.check_position( cur_pos , fkin(Global_70_SR , DR_WORLD)  , 2 ):
            System_Cur_Pos = 70
            merker = 1

        elif self.check_position( cur_pos , fkin(Global_100_ST , DR_WORLD)  , l_checkPosRadius ):
            System_Cur_Pos = 100
            merker = 1

        elif self.check_position( cur_pos , fkin(Global_110_S2S , DR_WORLD)  , l_checkPosRadius ):
            System_Cur_Pos = 110
            merker = 1

        else:
            System_Cur_Pos = "unkown"

#####################################

class error():

    def __init__(self) -> None:
        pass
        
    def disturbance_message(self , id , origin = "???"):
        """
        disturbance_message generates a disturbance popup .

        :param id: id of the disturbance
        :param origin: origin of the disturbance

        :return: popup
        """ 
        global Global_Disturbance
        
        if( id == 1 ):
            
            tp_popup("No Parts in Station Magazine", DR_PM_MESSAGE) 
            #tp_popup("Neustart erforderlich!! ", DR_PM_ALARM)
            
        elif( id == 2 ):
            tp_popup("Vacuum Fail at {0}".format(origin), DR_PM_ALARM) 
            #tp_popup("Neustart erforderlich!! ", DR_PM_ALARM)
            exit()

        elif( id == 3 ):
            tp_popup("Part Present at {0}".format(origin), DR_PM_ALARM) 
            #tp_popup("Neustart erforderlich!! ", DR_PM_ALARM)
            exit()

        elif( id == 4 ):
            tp_popup("No Parts in SM ! Please refill and restart !", DR_PM_MESSAGE) 
            #tp_popup("Neustart erforderlich!! ", DR_PM_ALARM)
            
        elif( id == 5 ):
            tp_popup("Previous Job was not finished", DR_PM_MESSAGE) 
            exit()

        elif( id == 6 ):
            tp_popup("OOPS, There went something wrong in the Flow managment", DR_PM_ALARM) 
            exit()

        elif( id == 7):
            tp_popup("timeout at {0}".format(origin) , DR_PM_ALARM) 
            exit()

        elif( id == 8):
            tp_popup("{0} NOT ok".format(origin) , DR_PM_ALARM)  
            #stop(DR_SSTOP)
            #raise DR_Error(DR_ERROR_TYPE, "Problem at flow_logic Step 1")

        elif( id == 9):
            tp_popup(" Sick Laser Error " , DR_PM_ALARM)   

        elif( id == 10):
            tp_popup("Can t initiate all components at {0}".format(origin) , DR_PM_ALARM) 

        elif( id == 8):
            pass 
        elif( id == 8):
            pass 
        elif( id == 8):
            pass 
        elif( id == 8):
            pass 
        elif( id == 8):
            pass 
        elif( id == 8):
            pass 
        elif( id == 8):
            pass 
        elif( id == 8):
            pass 
        elif( id == 8):
            pass 
        elif( id == 8):
            pass 

        else:
            tp_popup("Ungueltige Fehlerindex", DR_PM_MESSAGE) 
            tp_popup("Neustart erforderlich!! ", DR_PM_ALARM)
            exit()

#####################################

auto = runtime()
auto.automatic_mode()

