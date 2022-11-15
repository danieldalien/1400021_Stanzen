def check_pos(cur_pos , pos , radius):
    x = pos[0]
    y = pos[1]
    z = pos[2]
    x_c = cur_pos[0]
    y_c = cur_pos[1]
    z_c = cur_pos[2]

    test = pow((x - x_c),2) + pow((y - y_c),2) + pow((z - z_c),2)
    r = pow(radius , 2)
    if test < r :
        return True 
    else :
        return False 


merker = 0
radius = 25 
cur_pos,sol = get_current_posx(ref=DR_BASE)

if check_pos( cur_pos , relative_bewegung(Global_15_MC) , radius ) :
    System_cur_pos = 11
    merker = 1
elif check_pos( cur_pos , relative_bewegung(Global_25_SS) , radius ) :
    System_cur_pos = 21
    merker = 1
elif check_pos( cur_pos , relative_bewegung(Global_35_MC) , radius ) :
    System_cur_pos = 31
    merker = 1
elif check_pos( cur_pos , relative_bewegung(Global_45_SS) , radius ) :
    System_cur_pos = 41
    merker = 1
elif check_pos( cur_pos , relative_bewegung(Global_65_FS) , radius ) :
    System_cur_pos = 61
    merker = 1
elif check_pos( cur_pos , (Global_15_MC) , radius ) :
    System_cur_pos = 15
    merker = 1
elif check_pos( cur_pos , (Global_25_SS) , radius ) :
    System_cur_pos = 25
    merker = 1
elif check_pos( cur_pos , (Global_35_MC) , radius ) :
    System_cur_pos = 35
    merker = 1
elif check_pos( cur_pos , (Global_45_SS) , radius ) :
    System_cur_pos = 45
    merker = 1
elif check_pos( cur_pos , (Global_65_FS) , radius ) :
    System_cur_pos = 65
    merker = 1
elif check_pos( cur_pos , fkin(Global_1_MC) , radius ) :
    System_cur_pos = 1
    merker = 1
elif check_pos( cur_pos , fkin(Global_2_SS) , radius ) :
    System_cur_pos = 2
    merker = 1
elif check_pos( cur_pos , fkin(Global_6_FS) , radius ) :
    System_cur_pos = 6
    merker = 1
elif check_pos( cur_pos , fkin(Global_10_MC) , radius ) :
    System_cur_pos = 10
    merker = 1
elif check_pos( cur_pos , fkin(Global_20_SS) , radius ) :
    System_cur_pos = 20
    merker = 1
elif check_pos( cur_pos , fkin(Global_60_FS) , radius ) :
    System_cur_pos = 60
    merker = 1

tp_popup("merker= {0} , cur_pos = {1}".format(merker,System_cur_pos), DR_PM_ALARM)

if merker == 0 :
    tp_popup("Please place Robot in a free position", DR_PM_ALARM)
    wait_manual_guide()
    tp_popup("Please pay attention to robot and push the emergency stop if needed", DR_PM_ALARM)
    movej(Global_1_MC)
