from connect import getConnection
from math import cos, asin, radians, degrees

def getPoints(lat, lon, radius):
    mydb = getConnection()

    cursor = mydb.cursor()

    R = 6371; # earth's mean radius, km

    max_lat = lat + degrees(radius/R);
    min_lat = lat - degrees(radius/R);
    max_lon = lon + degrees(asin(radius/R) / cos(radians(lat)));
    min_lon = lon - degrees(asin(radius/R) / cos(radians(lat)));


    sql =f'''Select name, lat, lon, 
        acos(sin({radians(lat)})*sin(radians(lat)) + cos({radians(lat)})*cos(radians(lat))*cos(radians(lon)-{radians(lon)})) * {R} As distance
                From (
                    Select name ,lat, lon
                    From seller
                    Where lat Between {min_lat} And {max_lat}
                    And lon Between {min_lon} And {max_lon}
                ) As Box
                Where (acos(sin({radians(lat)})*sin(radians(lat)) + cos({radians(lat)})*cos(radians(lat))*cos(radians(lon)-{radians(lon)})) * {R}) < {radius}
                Order by distance'''


    cursor.execute(sql)

    myresult = cursor.fetchall()

    result = []
    names = []
    for x in myresult:
        result.append(tuple(map(float, (x[1], x[2]))))
        names.append(x[0])
        print(x)

    return (result, names)

if __name__ == "__main__":
    lat = 11.307213686206195 #float(input("Latitude: "))
    lon = 75.76359255756473  #float(input("Longitude: "))
    radius = 1 #float(input("Radius in KM: "))
    points, names = getPoints(lat, lon, radius)
    print(points)
