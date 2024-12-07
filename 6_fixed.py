def read_grid(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return x, y
    return None

def main():
    # Read the grid
    grid = read_grid('input')
    
    # Find starting position
    start = find_start(grid)
    if not start:
        print("No starting position (^) found!")
        return
    
    x, y = start
    visited = {(x, y)}  # Track unique positions using a set
    
    # Define directions: right, down, left, up
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    current_dir = 3  # Start moving up (index 3)
    
    while True:
        # Try to move in current direction
        new_x = x + directions[current_dir][0]
        new_y = y + directions[current_dir][1]
        
        # Check if we can move (within bounds and not hitting a wall)
        if (0 <= new_y < len(grid) and 
            0 <= new_x < len(grid[new_y]) and 
            grid[new_y][new_x] != '#'):
            # Move to new position
            x, y = new_x, new_y
            visited.add((x, y))
        else:
            # Turn right (clockwise)
            current_dir = (current_dir - 1) % 4
            
            # Check if we're stuck (tried all directions)
            stuck = True
            for _ in range(4):
                test_x = x + directions[current_dir][0]
                test_y = y + directions[current_dir][1]
                if (0 <= test_y < len(grid) and 
                    0 <= test_x < len(grid[test_y]) and 
                    grid[test_y][test_x] != '#'):
                    stuck = False
                    break
                current_dir = (current_dir - 1) % 4
            
            if stuck:
                break
    
    print(f"Number of unique positions visited: {len(visited)}")

if __name__ == "__main__":
    main()
