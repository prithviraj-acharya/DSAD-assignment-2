class KnapSack:
    def __init__(self, acres, profit, capacity):

        if len(acres) != len(profit):
            raise ValueError("acres and profit lists must have the same length.")
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative number.")
        if not acres or not profit:
            raise ValueError("acres and profit lists must not be empty.")

        self.acres = acres
        self.profit = profit
        self.capacity = capacity
        self.n = len(acres)
        self.ratio = [round(profit[i] / acres[i], 2) for i in range(self.n)]
        self.returned_indices = set()

    def find_max_idx(self):
        max_val = float("-inf")
        max_index = -1
        for i in range(self.n):
            if i not in self.returned_indices:
                if self.ratio[i] > max_val or (
                    self.ratio[i] == max_val
                    and self.acres[i] > self.acres[max_index]
                ):
                    max_val = self.ratio[i]
                    max_index = i
        if max_index != -1:
            self.returned_indices.add(max_index)
        return max_index

    def find_max_profit(self):
        initial_capacity = 0
        max_profit = 0
        items = []
        while initial_capacity < self.capacity:
            idx = self.find_max_idx()
            if idx == -1:
                break

            items.append(f"R{idx + 1}")

            if self.acres[idx] + initial_capacity <= self.capacity:
                initial_capacity += self.acres[idx]
                max_profit += self.profit[idx]
            else:
                max_profit += (self.capacity - initial_capacity) * self.ratio[idx]
                break

        return items, round(max_profit, 2)

def read_input_file(INPUT_FILE):
        acres_of_land = []
        profit = []
        with open(INPUT_FILE, 'r') as file:
            lines = file.readlines()
        x_line = lines[1].strip()
        max_acres = int(x_line.split(':')[1].strip())
        for line in lines[2:]:
            parts = line.strip().split('/')
            if len(parts) == 3:
                acres = int(parts[1].strip())
                value = int(parts[2].strip())
                acres_of_land.append(acres)
                profit.append(value)
        return acres_of_land, profit, max_acres

def write_output_file(OUTPUT_FILE, items, max_profit):
    with open(OUTPUT_FILE, 'w') as file:
        file.write("The regions that to are be selected is: ")
        for item in items:
            file.write(f"{item}, ")
        file.write(f"\nTotal profit value: {max_profit}")

if __name__ == "__main__":
    INPUT_FILE = 'inputPS05.txt'
    OUTPUT_FILE = "outputPS05.txt"
    acres, profit, capacity = read_input_file(INPUT_FILE)
    knapsack = KnapSack(acres, profit, capacity)
    items, profit = knapsack.find_max_profit()
    write_output_file(OUTPUT_FILE, items, profit)
