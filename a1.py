def intercept(roads, stations, start, friendStart):
    '''
    TODO: 
    Function description:
    Approach description (if main function):
    :Input:
    argv1:
    argv2:
    :Output, return or postcondition:
    :Time complexity:
    :Time complexity analysis:
    :Space complexity:
    :Space complexity analysis:

    '''
    # Check if input empty
    if not roads:
        return None
    else:
        # index of highest location (end of list of roads)
        maxLoc = -1

    for road in roads:
        maxLoc = max(maxLoc, road[0], road[1])

    # Adj list for locations [locations are the index of the list]
    locAdj = [[] for i in range(maxLoc + 1)]

    for source, dest, cost, time in roads:
        locAdj[source].append((dest, cost , time))
        
    print(locAdj)

    # Index each station
    stationIndex = [None] * (maxLoc + 1)
    
    for i, (station, _) in enumerate(stations):
        stationIndex[station] = i
    print(stationIndex)

    # Get index of friendStart
    friendStartIndex = stationIndex[friendStart]

    # Total time for one train loop (NOTE: i think it's needed)
    trainLoopTime = 0
    for i, time in stations:
        trainLoopTime += time
    print(trainLoopTime)
    

roads = [(6,0,3,1), (6,7,4,3), (6,5,6,2), (5,7,10,5), (4,8,8,5), (5,4,8,2),
(8,9,1,2), (7,8,1,3), (8,3,2,3), (1,10,5,4), (0,1,10,3), (10,2,7,2),
(3,2,15,2), (9,3,2,2), (2,4,10,5)]
stations = [(0,1), (5,1), (4,1), (3,1), (2,1), (1,1)]
start = 6
friendStart = 0

(intercept(roads, stations, start, friendStart))
#(7, 9, [6,7,8,3])