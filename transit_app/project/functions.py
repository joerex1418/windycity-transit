import cta
import metra

def get_cta_tracking_data(presets,lat,lon):
    tracking_dict = {}
    if presets["bus_route"]["tracking"] is True:
        tracking_dict["bus_route"] = []
        rt_list = presets["bus_route"]["items"]
        for rt in rt_list:
            obj = cta.BusRoute(rt[0],rt[1])
            try:stops_dict = obj.stops_by_distance(lat,lon,limit=3).astype("str").to_dict("records")
            except:stops_dict = obj.stops().astype("str").to_dict("records")
            tracking_dict['bus_route'].append({
                "info":{"route":obj.route(),"direction":obj.direction()},
                "locations":obj.locations().astype("str").to_dict("records"),
                "stops":stops_dict
                })
    return tracking_dict

def draw_vehicle_locations(tracking_data:dict,service:str):
    pass

def bus_route_html(df_records):
    pass