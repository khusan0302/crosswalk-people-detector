def get_traffic_light_status(current_time, red_duration, green_duration):
    cycle = red_duration + green_duration
    if current_time % cycle < red_duration:
        return "RED"
    return "GREEN"