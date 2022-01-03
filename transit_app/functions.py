import cta
import metra


def getStops(search_by,**params):
    if search_by == "route":
        rt = str(params["route_id"])
        direction = params["direction"]
        df = cta.bus_route_stops(rt,direction)
        return df.to_dict("records")
    elif search_by == "query":
        query = params["query"]