class KnapSack:
    def __init__(self, weights, profit, capacity):
        self.weights = weights
        self.profit = profit
        self.capacity = capacity
        self.n = len(weights)
        self.ratio = [round(profit[i] / weights[i], 2) for i in range(self.n)]
        self.returned_indices = []

    def find_max_idx(self):
        max_val = float("-inf")
        max_index = -1
        for i in range(self.n):
            if i not in self.returned_indices:
                if self.ratio[i] > max_val or (
                    self.ratio[i] == max_val
                    and self.weights[i] > self.weights[max_index]
                ):
                    max_val = self.ratio[i]
                    max_index = i
        if max_index != -1:
            self.returned_indices.append(max_index)
        return max_index

    def find_max_profit(self):
        initial_capacity = 0
        max_profit = 0
        items = []
        while initial_capacity < self.capacity:
            idx = self.find_max_idx()
            if idx == -1:
                break

            items.append(idx + 1)

            if self.weights[idx] + initial_capacity <= self.capacity:
                initial_capacity += self.weights[idx]
                max_profit += self.profit[idx]
            else:
                max_profit += (self.capacity - initial_capacity) * self.ratio[idx]
                break

        return items, max_profit


if __name__ == "__main__":
    weights = [3, 2, 4, 1, 5, 4, 6, 3, 2, 2]
    profit = [80, 30, 20, 40, 120, 60, 100, 60, 30, 50]
    capacity = 16
    knapsack = KnapSack(weights, profit, capacity)
    items, profit = knapsack.find_max_profit()
    print(items)
    print(profit)
