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

    # Adj list for roads
    roads_adj = [[] for i in range(maxLoc + 1)]

    for source, dest, cost, time in roads:
        roads_adj[source].append((dest, cost , time))
        
    print(roads_adj)
    # Get index of friendStart
    friendStartIndex = -1
    '''
    for i in range(len(stations)):
        if stations[0] == friendStart
    '''
    

roads = [(0,1,35,3), (1,2,5,2), (2,0,35,4), (0,4,10,1), (4,1,22,2),
(1,5,65,1), (5,2,70,1), (2,3,10,1), (3,0,20,3)]
stations = [(4,3), (5,2), (3,4)]
start = 0
friendStart = 4

(intercept(roads, stations, start, friendStart))