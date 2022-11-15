def vacuum( id , state ):

    if id == "S1S":
        id_output = 0
    elif id == "SP":
        id_output = 0
    elif id == "RD" :
        id_output = 0
    else : 
        tp_popup("Vacuum : Unkown ID", DR_PM_ALARM)

    if state == True :
        set_digital_output( id_output , ON )
    elif state == False : 
        set_digital_output( id_output , OFF )
    else : 
        tp_popup("Vacuum : Unkown state, Use True to start vacuum  and False to stop", DR_PM_ALARM)