#-- Start To Do --#
# NACH NCV ( = Noch zu vervollstaendigen) SUCHEN 
#
#
#-- Ende To Do --#
#--Positions--##
Global_10_SM  = 11
Global_11_S1M = 11
Global_15_S1M = 11
Global_21_S2M = 11
Global_25_S2M = 11

Global_30_S1S = 11
Global_31_S1S = 11 
Global_35_S1S = 11

#Global_40_S1S = 1 
Global_41_S1S = 11 
#Global_42_S1S = 0 
#Global_43_S1S = 0 
Global_45_S1S = 11 
Global_46_S1S = 0 # Zwischenposition movec 
Global_47_S1S = 11

Global_51_S1S = 11
Global_55_S1S = 11

Global_60_SR = 11
Global_61_SR = 11
Global_65_SR = 11

Global_71_SR = 11
Global_75_SR = 11

Global_81_S1S = 11
Global_85_S1S = 11

Global_91_S1S = 11
Global_95_S1S = 11

Global_100_ST = 11
Global_101_ST = 11
Global_105_ST = 11

Global_110_S2S = 11
Global_111_S2S = 11
#Global_112_S2S = 0
#Global_113_S2S = 0
Global_115_S2S = 11
Global_116_S2S = 0 #Zwischenposition fuer moveC
Global_117_S2S = 11
#--Ende Positions--#

#--Start Constants--#
class Constants :

    Global_t_lever = 15 #Time the Robot will need to push the spamp  
    Global_l_blendRadius = 5 #Blending Radius for smoother mvt
    Global_l_checkPosRadius = 25 #Sphere Radius fpr Positionlocating 

constants = Constants
#--Ende Constants--#



#--Start Marker--#
System_SM_Side = 0 
System_Cur_Pos = 0
System_i_AP = 0 
System_i_Step = 0
Global_Disturbance = 0

#--Ende Marker--#

def vacuum_control(id,state ):
    pass
def vifo():
    pass
def disturbance_message(id ):
    pass
def vacuum(id , state):
    pass
def relative_mvt(pos_ini , deltaX  = 0 , deltaY = 0 , deltaZ = z):
    pass
def check_pos(cur_pos , pos , radius):
    pass
#--Start 010_SM_Pick--#
#
def ap_010_SM_Pick(): 

    vacuum_control( "RD" , False )
    vacuum_control( "S1S" , False ) 
    vifo()
    if System_SM_Side == 0 :
        movej(Global_10_SM , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 10
        movel(relative_mvt(Global_15_S1M) , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 11 
        movel(Global_15_S1M , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 15 
    elif System_SM_Side == 1 :
        movej(Global_10_SM)
        System_Cur_Pos = 10
        movel(relative_mvt(Global_25_S2M) , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 21 
        movel(Global_25_S2M)
        System_Cur_Pos = 25
    elif System_SM_Side == -1 :
        Global_Disturbance = 1
        disturbance_message(4)
        exit()
    vacuum("RD", True)
    vacuum_control("RD" , True )
    System_i_AP = 30 


#--Ende 010_SM_Pick--#

#--Start 030_SS1_Place--#

def ap_030_SS1_Place():

    vacuum_control( "RD" , True ) 
    vacuum_control( "S1S" , False ) 
    movej( Global_30_S1S , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 30
    movel( relative_mvt( Global_35_S1S ) , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 31 
    movel( Global_35_S1S )
    System_Cur_Pos = 35 
    vacuum_control( "RD" , True )
    vacuum( "S1S" , True)
    vacuum_control( "S1S" , True )
    vacuum( "RD" , False)
    System_i_AP = 40 

#--Ende 030_SS1_Place--#

#--Start 040_SS1_Lever--#

def ap_040_SS1_Lever() :

    movej( Global_30_S1S , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 30
    movel( relative_mvt( Global_45_S1S ) , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 41 
    movel( Global_45_S1S )
    System_Cur_Pos = 45 
    movec( Global_46_S1S , Global_47_S1S , time = constants.Global_t_lever )
    System_Cur_Pos = 47
    wait( 1 )
    movec( Global_46_S1S , Global_45_S1S , time = constants.Global_t_lever )
    System_Cur_Pos = 45 

    if System_i_Step == 3 :
        System_i_AP = 50 
    elif System_i_Step == 8 :
        System_i_AP = 90 
#--Ende  040_SS1_Lever--#

#--Start 050_SS1_Pick1--#

def ap_050_SS1_Pick1():

    vacuum_control( "RD" , False ) 
    vacuum_control( "S1S" , True )
    movej( Global_30_S1S , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 30
    movel( relative_mvt( Global_55_S1S ) , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 51 
    movel( Global_55_S1S )
    System_Cur_Pos = 55 
    vacuum( "RD" , True)
    vacuum_control( "RD" , True )
    vacuum( "S1S" , False)
    System_i_AP = 60 

#--Ende  050_SS1_Pick1--#

#--Start 060_SR_Place--#

def ap_060_SR_Place():
    #NCV
    set SR_Gripper_open = True  # Wahrscheinlich ist das ein Pulse 
    set SR_Gripper_0_Degree = True # Wahrscheinlich ist das ein Pulse 

    vacuum_control( "RD" , True )
    movej( Global_60_SR , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 60
    movel( relative_mvt( Global_65_SR ) , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 61 
    movel( Global_65_SR )
    System_Cur_Pos = 65 
    vacuum_control( "RD" , True )
    #NCV
    set SR_Gripper_close = True  # Wahrscheinlich ist das ein Pulse 
    vacuum("RD" , False)
    System_i_AP = 70 

#--Ende 060_SR_Place--#

#--Start 070_SR_Pick--#

def ap_070_SR_Pick():

    set SR_Gripper_180_Degree = True # Wahrscheinlich ist das ein Pulse 

    vacuum_control( "RD" , False )
    movej( Global_60_SR , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 60
    movel( relative_mvt( Global_75_SR ) , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 71 
    movel( Global_75_SR )
    System_Cur_Pos = 75 
    vacuum("RD" , True)
    vacuum_control( "RD" , True )
    #NCV
    set SR_Gripper_open = True  # Wahrscheinlich ist das ein Pulse 

    System_i_AP = 80 

#--Ende 070_SR_Pick--#

#--Start 080_SS1_Place2--#
def ap_080_SS1_Place_2():

    vacuum_control( "RD" , True ) 
    vacuum_control( "S1S" , False ) 
    movej( Global_30_S1S , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 30
    movel( relative_mvt( Global_85_S1S ) , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 81 
    movel( Global_85_S1S )
    System_Cur_Pos = 85 

    vacuum_control( "RD" , True )
    vacuum( "S1S" , True)
    vacuum_control( "S1S" , True )
    vacuum( "RD" , False)
    System_i_AP = 40

#--Ende 080_SS1_Place2--#

#--Start 090_SS1_Pick2--#

def ap_090_SS1_Pick2():

    vacuum_control( "RD" , False ) 
    vacuum_control( "S1S" , True ) 
    movej( Global_30_S1S , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 30
    movel( relative_mvt( Global_95_S1S ) , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 91 
    movel( Global_95_S1S )
    System_Cur_Pos = 95 

    vacuum_control( "RD" , False )
    vacuum_control( "S1S" , True )
    vacuum( "RD" , True)
    vacuum_control( "RD" , True )
    vacuum( "S1S" , False)
    System_i_AP = 100 

#--Ende 090_SS1_Pick2--#

#--Start 100_ST_Place--#

def ap_100_ST_Place():
    #NCV
    set ST_Pos_SP = True  # Wahrscheinlich ist das ein Pulse 
    set SP_H_GS = True # Wahrscheinlich ist das ein Pulse 

    vacuum_control( "RD" , True )
    movej( Global_100_ST , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 100
    movel( relative_mvt( Global_105_ST ) , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 101 
    movel( Global_105_ST )
    System_Cur_Pos = 105 
    vacuum_control( "RD" , True )
    vacuum("RD" , False)

    System_i_AP = 110 

#--Ende 100_ST_Place--#

#--Start 110_SS2_Lever--#

def ap_110_SS2_Lever() :

    set ST_Pos_S2S = True  # Wahrscheinlich ist das ein Pulse 

    movej( Global_110_S2S , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 110
    movel( relative_mvt( Global_115_S2S ) , r = constants.Global_l_blendRadius )
    System_Cur_Pos = 111 
    movel( Global_115_S2S )
    System_Cur_Pos = 115 
    movec( Global_116_S2S , Global_117_S2S , time = constants.Global_t_lever )
    System_Cur_Pos = 117
    wait( 1 )
    movec( Global_116_S2S , Global_115_S2S , time = constants.Global_t_lever )
    System_Cur_Pos = 115 

    System_i_AP = 10 

#--Ende  110_SS2_Lever--#

def flow_logic():
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
    if System_i_Step == 0 or System_i_Step == 11 :
        #Conditions to enter in Step 1:
        #Robot is empty 
        #Station_SM has parts 
        vacuum_control( "RD" , False ) #True when Robot is empty
        
        if vifo() != -1 : #-1=No Part present 
            System_i_Step = 1
        else:
            #NCV
            tp_popup("Problem at flow_logic Step 1",DR_PM_ALARM)

    elif System_i_Step == 1:
        #Conditions to enter in Step 2:
        #Robot has part
        #Station_S1S is empty  
        vacuum_control( "RD" , True ) #True when Robot has part
        vacuum_control( "S1S" , False ) #True when S1S has no part
        System_i_Step = 2

    elif System_i_Step == 2:
        #Conditions to enter in Step 3:
        #Robot has no part
        #Station_S1S has part
        vacuum_control( "RD" , False ) 
        vacuum_control( "S1S" , True ) 
        System_i_Step = 3

    elif System_i_Step == 3:
        #Conditions to enter in Step 4:
        #Robot has no part
        #Station_S1S has part
        vacuum_control( "RD" , False ) 
        vacuum_control( "S1S" , True ) 
        System_i_Step = 4

    elif System_i_Step == 4:
        #Conditions to enter in Step 5:
        #Schunk Gripper is open
        #Schunk Gripper is turned to 0 Degrees
        #Robot has a part 
        'Check Gripper open'
        'Check Gripper 0 degree' 
        vacuum_control( "RD" , True ) 
        System_i_Step = 5

    elif System_i_Step == 5:
        #Conditions to enter in Step 6:
        #Schunk Gripper is closed
        #Schunk Gripper is turned to 180 Degrees
        #Robot has no part 
        'Check Gripper closed'
        'Check Gripper 180 degree' 
        vacuum_control( "RD" , False ) 
        System_i_Step = 6

    elif System_i_Step == 6:
        #Conditions to enter in Step 7:
        #Robot has part
        #Station_S1S is empty 
        vacuum_control( "RD" , True ) #True when Robot has part
        vacuum_control( "S1S" , False ) #True when S1S has no part
        System_i_Step = 7

    elif System_i_Step == 7:
        #Conditions to enter in Step 8:
        #Robot has no part
        #Station_S1S has a part
        vacuum_control( "RD" , False ) #True when Robot has no part
        vacuum_control( "S1S" , True ) #True when S1S has part
        System_i_Step = 8

    elif System_i_Step == 8:
        #Conditions to enter in Step 9:
        #Robot has no part
        #Station_S1S has part
        vacuum_control( "RD" , False ) #True when Robot has no part
        vacuum_control( "S1S" , True ) #True when S1S has part
        System_i_Step = 9

    elif System_i_Step == 9:
        #Conditions to enter in Step 10:
        #Station Train in Position: ST_Pos_SP
        #Station Packaging in GS ( Avoid colision while placing part on train )
        #Robot has part
        #NCV
        'Check ST_Pos_SP'
        'Check SP_Cylinder_Horizontal_GS' 
        vacuum_control( "RD" , True ) 
        System_i_Step = 10
        
    elif System_i_Step == 10:
        #Conditions to enter in Step 11:
        #Robot has no part
        #Station Train in Position: ST_Pos_S2S 
        #NCV
        'Check ST_Pos_S2S' 
        vacuum_control( "RD" , False ) 
        System_i_Step = 11

def flow_management():

    if System_i_Step == 1:

        if System_i_AP == 10 :
            ap_010_SM_Pick()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 2 : 

        if System_i_AP == 30 :
            ap_030_SS1_Place()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 3 : 

        if System_i_AP == 40 :
            ap_040_SS1_Lever()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 4 : 

        if System_i_AP == 50 :
            ap_050_SS1_Pick1()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 5 : 

        if System_i_AP == 60 :
            ap_060_SR_Place()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 6 : 

        if System_i_AP == 70 :
            ap_070_SR_Pick()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 7 :

        if System_i_AP == 80 :
            ap_080_SS1_Place_2()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 8 : 

        if System_i_AP == 40 :
            ap_040_SS1_Lever()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 9 : 

        if System_i_AP == 90 :
            ap_090_SS1_Pick2()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 10 : 

        if System_i_AP == 100 :
            ap_100_ST_Place()
        else :
            Global_Disturbance = 1
            disturbance_message(5)

    elif System_i_Step == 11 : 
        if System_i_AP == 110 :
            ap_110_SS2_Lever()
        else :
            Global_Disturbance = 1
            disturbance_message(5)
    else : 
        Global_Disturbance = 1 
        disturbance_message()
        
def position_locator():

    # TO DO

    #ENDE
    merker = 0 
    radius = 25 
    cur_pos,sol = get_current_posx(ref=DR_BASE)
    
    if check_pos( cur_pos , relative_mvt(Global_15_S1M) , constants.Global_l_checkPosRadius ) :

        System_Cur_Pos = 11
        merker = 1 

    elif check_pos( cur_pos , relative_mvt(Global_25_S2M) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 21 
        merker = 1 

    elif check_pos( cur_pos , relative_mvt(Global_35_S1S) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 31
        merker = 1

    elif check_pos( cur_pos , relative_mvt(Global_45_S1S) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 41
        merker = 1

    elif check_pos( cur_pos , relative_mvt(Global_55_S1S) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 51
        merker = 1

    elif check_pos( cur_pos , relative_mvt(Global_65_SR) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 61
        merker = 1 

    elif check_pos( cur_pos , relative_mvt(Global_75_SR) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 71
        merker = 1 

    elif check_pos( cur_pos , relative_mvt(Global_85_S1S) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 81
        merker = 1

    elif check_pos( cur_pos , relative_mvt(Global_95_S1S) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 91
        merker = 1 

    elif check_pos( cur_pos , relative_mvt(Global_105_ST) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 101
        merker = 1

    elif check_pos( cur_pos , relative_mvt(Global_115_S2S) , constants.Global_l_checkPosRadius ) :
        System_Cur_Pos = 111
        merker = 1

    elif check_pos( cur_pos , (Global_15_S1M)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 15
        merker = 1

    elif check_pos( cur_pos , (Global_25_S2M)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 25
        merker = 1

    elif check_pos( cur_pos , (Global_35_S1S)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 35
        merker = 1

    elif check_pos( cur_pos , (Global_45_S1S)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 45
        merker = 1

    elif check_pos( cur_pos , (Global_55_S1S)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 55
        merker = 1

    elif check_pos( cur_pos , (Global_65_SR)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 65
        merker = 1

    elif check_pos( cur_pos , (Global_75_SR)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 75
        merker = 1

    elif check_pos( cur_pos , (Global_85_S1S)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 85
        merker = 1

    elif check_pos( cur_pos , (Global_95_S1S)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 95
        merker = 1

    elif check_pos( cur_pos , (Global_105_ST)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 105
        merker = 1

    elif check_pos( cur_pos , (Global_115_S2S)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 115
        merker = 1

    elif check_pos( cur_pos , fkin(Global_10_SM)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 10
        merker = 1

    elif check_pos( cur_pos , fkin(Global_30_S1S)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 30
        merker = 1

    elif check_pos( cur_pos , fkin(Global_60_SR)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 60
        merker = 1

    elif check_pos( cur_pos , fkin(Global_100_ST)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 100
        merker = 1

    elif check_pos( cur_pos , fkin(Global_110_S2S)  , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 110
        merker = 1

    elif check_pos( cur_pos , (Global_47_S1S) , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 47 
        merker = 1 

    elif check_pos( cur_pos , (Global_117_S2S) , constants.Global_l_checkPosRadius ):
        System_Cur_Pos = 117 
        merker= 1

    if merker == 0 :

        tp_popup("Please place Robot in a free position", DR_PM_ALARM)
        wait_manual_guide()
        tp_popup("Please pay attention to robot and push the emergency stop if needed", DR_PM_ALARM)
        change_operation_speed( 10 )
        #NCV
        movej(' Hier muss noch eine Position definiert werden ')
        change_operation_speed( 100 )
    
def move_out_ap():
    
    if System_Cur_Pos == 10 :
        pass
    elif System_Cur_Pos == 11 : 
        movej(Global_10_SM , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 10

    elif System_Cur_Pos == 15 : 
        movel(relative_mvt(Global_15_S1M))
        System_Cur_Pos = 11
        movej(Global_10_SM , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 10
        
    elif System_Cur_Pos == 21 : 
        movej(Global_10_SM , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 10

    elif System_Cur_Pos == 25 : 
        movel(relative_mvt(Global_25_S2M))
        System_Cur_Pos = 21
        movej(Global_10_SM , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 10

    elif System_Cur_Pos == 30 : 
        pass

    elif System_Cur_Pos == 31 : 
        movej(Global_30_S1S , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 35 : 
        movel(relative_mvt(Global_35_S1S))
        System_Cur_Pos = 31
        movej(Global_30_S1S , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 41 : 
        movej(Global_30_S1S , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 45 : 
        #NCV : Kraftkontrolle einbauen, falls moveC schon angefangen hat aber Cur pos 
        # noch nicht umgeschrieben wurde weil somit ware ein gerade rausfahren auf 
        # 41 nicht moeglich un koennte damit abgefangen werden. 
        movel(relative_mvt(Global_45_S1S))
        System_Cur_Pos = 41
        movej(Global_30_S1S , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 47 : 
        #NCV : Kraftkontrolle 
        movec( Global_46_S1S , Global_45_S1S , time = constants.Global_t_lever )
        System_Cur_Pos = 45 
        movel(relative_mvt(Global_45_S1S))
        System_Cur_Pos = 41
        movej(Global_30_S1S , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 51 : 
        movej(Global_30_S1S , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 55 : 
        movel(relative_mvt(Global_55_S1S))
        System_Cur_Pos = 51
        movej(Global_30_S1S , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 60 : 
        pass

    elif System_Cur_Pos == 61 : 
        movej(Global_60_SR)
        System_Cur_Pos = 60

    elif System_Cur_Pos == 65 : 
        movel(relative_mvt(Global_65_SR))
        System_Cur_Pos = 61
        movej(Global_60_SR , r = constants.Global_l_blendRadius)
        System_Cur_Pos = 60

    elif System_Cur_Pos == 71 : 
        movej(Global_60_SR)
        System_Cur_Pos = 60

    elif System_Cur_Pos == 75 : 
        movel(relative_mvt(Global_75_SR))
        System_Cur_Pos = 71
        movej(Global_60_SR)
        System_Cur_Pos = 60

    elif System_Cur_Pos == 81 : 
        movej(Global_30_S1S)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 85 : 
        movel(relative_mvt(Global_85_S1S))
        System_Cur_Pos = 81
        movej(Global_30_S1S)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 91 : 
        movej(Global_30_S1S)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 95 : 
        movel(relative_mvt(Global_95_S1S))
        System_Cur_Pos = 91
        movej(Global_30_S1S)
        System_Cur_Pos = 30

    elif System_Cur_Pos == 100 : 
        pass

    elif System_Cur_Pos == 101 : 
        movej(Global_100_ST)
        System_Cur_Pos = 100

    elif System_Cur_Pos == 105 : 
        movel(relative_mvt(Global_105_ST))
        System_Cur_Pos = 101
        movej(Global_100_ST)
        System_Cur_Pos = 100

    elif System_Cur_Pos == 110 : 
        pass

    elif System_Cur_Pos == 111 : 
        movej(Global_110_S2S)
        System_Cur_Pos = 110

    elif System_Cur_Pos == 115 : 
        movel(relative_mvt(Global_115_S2S))
        System_Cur_Pos = 111
        movej(Global_110_S2S)
        System_Cur_Pos = 110

    elif System_Cur_Pos == 117 : 
        movec( Global_116_S2S , Global_115_S2S , time = constants.Global_t_lever )
        System_Cur_Pos = 115 
        movel( relative_mvt( Global_115_S2S ) )
        System_Cur_Pos = 111 
        movej( Global_110_S2S )
        System_Cur_Pos = 110

