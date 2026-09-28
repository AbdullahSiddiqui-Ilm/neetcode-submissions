class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleets = []

        for p, s in zip(position, speed):
            cars.append([p, s])
        cars.sort(key=lambda x: x[0], reverse=True)

        p, s = cars[0]
        time = (target - p) / s
        fleets.append(time)

        for p, s in cars[1:]:
            time = (target - p) / s
            if time > fleets[-1]:
                fleets.append(time)
        return len(fleets)       

# hint; time = (target - p) / s
"""
Pattern: 

We use a stack to check how many fleets we have. If the time to get to destination is greater than car in front, it means it doesnt catch up and forms a new fleet, so add to stack

algorithm:
 - store positions and speeds of each car in a list
 - reverse the list so we check from the closest to destination
 - calculate time for last car, and append to fleets as we know we have at least one.
 - append through the cars list, and check whether time is greater than one in front. 
 If true, append the fleets as it didnt catch up to the car in front.
"""