def vifo():

    if System_SM_Side == 1 :

        if SM_Sensor_Left == 1 :
            System_SM_Side = 1
        elif SM_Sensor_Right == 1 : 
            System_SM_Side = 0
        else : 
            System_SM_Side = -1
            Global_Disturbance = 1
            disturbance_message(4)

    elif System_SM_Side == 0 : 

        if SM_Sensor_Left == 1 :
            System_SM_Side = 1
        elif SM_Sensor_Right == 1 : 
            System_SM_Side = 0
        else : 
            System_SM_Side = -1 
            Global_Disturbance = 1
            disturbance_message(4)

    elif System_SM_Side == -1 :

        if SM_Sensor_Left == 1 :
            System_SM_Side = 1
        elif SM_Sensor_Right == 1 : 
            System_SM_Side = 0
        else : 
            System_SM_Side = -1 
            Global_Disturbance = 1
            disturbance_message(4)
            
    return System_SM_Side