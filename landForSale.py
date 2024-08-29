class KnapSack:
    def __init__(self, input_file):
        self.acres, self.profit, self.capacity = self.read_input_file(input_file)
        self.validate_inputs()
        self.n = len(self.acres)
        self.ratio = [round(self.profit[i] / self.acres[i], 2) for i in range(self.n)]
        self.returned_indices = set()

    def validate_inputs(self):
        """Validate the input data."""
        if len(self.acres) != len(self.profit):
            raise ValueError("acres and profit lists must have the same length.")
        if self.capacity < 0:
            raise ValueError("Capacity must be a non-negative number.")
        if not self.acres or not self.profit:
            raise ValueError("acres and profit lists must not be empty.")
        if any(acres < 0 for acres in self.acres):
            raise ValueError("acres values must be non-negative.")

    def find_max_idx(self):
        """Find the index of the item with the maximum profit-to-acre ratio."""
        max_val = float("-inf")
        max_index = -1
        for i in range(self.n):
            if i not in self.returned_indices:
                if self.ratio[i] > max_val or (
                    self.ratio[i] == max_val and self.acres[i] > self.acres[max_index]
                ):
                    max_val = self.ratio[i]
                    max_index = i
        if max_index != -1:
            self.returned_indices.add(max_index)
        return max_index

    def find_max_profit(self):
        """Calculate the maximum profit and the selected items."""
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

    def read_input_file(self, input_file):
        """Read input data from a file."""
        acres_of_land = []
        profit = []
        try:
            with open(input_file, "r") as file:
                lines = file.readlines()
            n = int(lines[0].strip().split(":")[1].strip())
            max_acres = int(lines[1].strip().split(":")[1].strip())
            for line in lines[2 : 2 + n]:
                parts = line.strip().split("/")
                if len(parts) == 3:
                    acres = int(parts[1].strip())
                    value = int(parts[2].strip())
                    acres_of_land.append(acres)
                    profit.append(value)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {input_file}")
        except ValueError as e:
            raise ValueError(f"Value error: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
        return acres_of_land, profit, max_acres

    def write_output_file(self, output_file, items, max_profit):
        """Write the output data to a file."""
        try:
            with open(output_file, "w") as file:
                file.write("The regions that to be selected is: ")
                file.write(", ".join(items))
                file.write(f"\nTotal profit value: {max_profit}")
        except IOError as e:
            raise IOError(f"IO error: {e}")


if __name__ == "__main__":
    INPUT_FILE = "inputPS05.txt"
    OUTPUT_FILE = "outputPS05.txt"
    try:
        knapsack = KnapSack(INPUT_FILE)
        items, profit = knapsack.find_max_profit()
        knapsack.write_output_file(OUTPUT_FILE, items, profit)
    except Exception as e:
        print(f"An error occurred during processing: {e}")
