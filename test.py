def second_pass(commands, num_frames):
    knob = []
    for command in commands:
        cmd = command[0]
        args = command[1:]
        varname = args[0]
        if cmd == 'vary':
            start_frame = args[1]
            end_frame = args[2]
            start_val = args[3]
            end_val = args[4]

            frames = end_frame - start_frame

            d = 1
            if frames < 0:
                d=-1

          
                
            knob=[{varname:x/num_frames} for x in range(start_frame, end_frame+1,d)]
        
