
def vacuum_control( id , state):
    """
    vacuum_control checks wheter or not vacuum was reached .

    :param id: id of the component which should be checked for vacuum 
    :param state: Check for vacuum or no vacuum 

    :return: TRUE FALSE or Error  
    """ 

    Global_Vak_Ok = 0
    timeout_vak_check = 1 
    if id == "S1S":
        id_output = 0
    elif id == "SP":
        id_output = 0
    elif id == "RD" :
        id_output = 0

    if state == True :
        res = wait_digital_input( id_output , ON , timeout_vak_check)
        if res == 0 : # 0 = Success , -1 = Failed
            Global_Vak_Ok = 1
            return Global_Vak_Ok
        else :
            Global_Vak_Ok = 0
            Global_Disturbance = 1
            disturbance_message(2 , id)
            return Global_Vak_Ok  
    elif state == False : 
        res = wait_digital_input( id_output , OFF , timeout_vak_check)
        if res == 0 : # 0 = Success , -1 = Failed
            Global_Vak_Ok = 0
            return Global_Vak_Ok
        else :
            Global_Vak_ok = 1
            Global_Disturbance = 1
            disturbance_message(3 , id)
            return Global_Vak_Ok              
