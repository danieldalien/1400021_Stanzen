z = 50 
def relative_mvt( pos_ini , deltaX  = 0 , deltaY = 0 , deltaZ = z  ):
   
    delta = [ deltaX , deltaY , deltaZ , 0 , 0 , 0 ]
    pos = add_pose(pos_ini , delta)

    return pos    