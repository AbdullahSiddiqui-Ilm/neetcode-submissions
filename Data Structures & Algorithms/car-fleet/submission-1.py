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
            if time <= fleets[-1]:
                continue
            else:
                fleets.append(time)
        return len(fleets)