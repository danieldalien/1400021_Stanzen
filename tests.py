


x1 = posx( -614 , -49 , 199 , 0 , 135 , 0 )
delta = posx( 100 , 100 , 100 , 0 , 0 , 0 )
x2 = trans(x1, delta, ref = DR_WORLD, ref_out = DR_TOOL)

tp_popup("test =  {0}".format(x2), DR_PM_ALARM)

x1 = posx( -861.16 , -186.72 , 152.61 , 0 , 135 , 0 )
x2 = posx( -861.16 , -107.8  , 152.61 , 0 , 135 , 0 )
X3 = posx( -935.01 , -107.8  , 178.74 , 0 , 135 , 0 )

        #Check if robot is at a known position
        self.c_functions.position_locator()

        if System_Cur_Pos ==  47 or System_Cur_Pos == 45 or System_Cur_Pos == 117 or System_Cur_Pos == 119 or System_Cur_Pos == 113 :
            pass
        elif System_Cur_Pos == 40 or System_Cur_Pos == 115:
            pass
        elif System_Cur_Pos == "unkown":
