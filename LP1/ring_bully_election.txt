def ring(nodes,initiator,alive):
    msg=[]
    index=nodes.index(initiator)
    if initiator not in alive:
        print("INITIATOR DEAD")
        return

    while True:
        if nodes[index] in alive:
            msg.append(nodes[index])
        
        index=(index+1)%len(nodes)

        if nodes[index]==initiator:
            break
    print(msg)
    print(f"LEADER: {max(msg)}")

def bully(nodes,initiator,alive):
    print(f"{initiator} starts election")

    if initiator not in alive:
        print("INITIATOR DEAD")
        return
    
    higher=[p for p in nodes if p>initiator and p in alive]

    if not higher:
        print(f"LEADER: {initiator}")

    for q in higher:
        print(f"{initiator} -> {q} who starts election")
        return bully(nodes,q,alive)

nodes=[2,3,1,4,5]
alive=[1,2,3,4,5]
initiator=1

ring(nodes,initiator,alive)
bully(nodes,initiator,alive)


'''def bully(nodes, initiator, alive, visited=None):
    if visited is None:
        visited = set()

    if initiator not in alive:
        print(f"Initiator {initiator} is not alive, cannot start election")
        return None

    if initiator in visited:
        return None  # Already handled
    visited.add(initiator)

    higher = [p for p in nodes if p > initiator and p in alive]
    if not higher:
        print(f"No higher nodes than {initiator}. Node {initiator} becomes leader")
        return initiator

    candidates = []
    for q in higher:
        print(f"{initiator} sends election message to {q}")
        print(f"{q} receives message and starts its own election")
        leader = bully(nodes, q, alive, visited)
        if leader:
            candidates.append(leader)

    return max(candidates) if candidates else initiator

nodes=[1,2,3,4,5]
initiator=2
alive=[1,2,3,5]

print("LEADER IS", bully(nodes,initiator,alive))'''
