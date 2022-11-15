
global Global_Disturbance

def disturbance_message(id , origin = "???"):
    """
    disturbance_message generates a disturbance popup .

    :param id: id of the disturbance
    :param origin: origin of the disturbance

    :return: popup
    """ 
	
    if( Global_Disturbance == 1 ):
        if( id == 1 ):
            tp_popup("No Parts in Station Magazine", DR_PM_MESSAGE) 
            #tp_popup("Neustart erforderlich!! ", DR_PM_ALARM)
            exit()
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
            exit()
        elif( id == 5 ):
            tp_popup("Previous Job was not finished", DR_PM_MESSAGE) 
            exit()
        elif( id == 6 ):
            tp_popup("OOPS, There went something wrong in the Flow managment", DR_PM_ALARM) 
            exit()
        elif( id == 7):
            pass 
        else:
            tp_popup("Ungueltige Fehlerindex", DR_PM_MESSAGE) 
            tp_popup("Neustart erforderlich!! ", DR_PM_ALARM)
            exit()
	
    else:
        tp_popup( "No Disturbance", DR_PM_MESSAGE)



