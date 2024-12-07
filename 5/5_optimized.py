import os
from typing import List, Tuple

def parse_input(filename: str = 'input') -> Tuple[List[Tuple[str, str]], List[List[str]]]:
    with open(filename, 'r') as file:
        rules_text, sequences = file.read().split('\n\n')
    
    # Parse rules while preserving order
    rules = [tuple(rule.split('|')) for rule in rules_text.split('\n')]
    
    # Parse sequences into lists
    sequences_list = [seq.split(',') for seq in sequences.split('\n')]
    
    return rules, sequences_list

def check_sequence_validity(sequence: List[str], rules: List[Tuple[str, str]]) -> bool:
    # Create index lookup for O(1) access
    index_lookup = {val: idx for idx, val in enumerate(sequence)}
    
    # Check each rule
    for before, after in rules:
        if before in index_lookup and after in index_lookup:
            if index_lookup[before] > index_lookup[after]:
                return False
    return True

def get_middle_value(sequence: List[str]) -> int:
    return int(sequence[len(sequence) // 2])

def fix_sequence(sequence: List[str], rules: List[Tuple[str, str]]) -> List[str]:
    sequence = list(sequence)  # Create a copy
    
    # Run exactly 4 iterations
    for _ in range(4):
        # Process all rules in each iteration
        for before, after in rules:
            if before not in sequence or after not in sequence:
                continue
            
            before_idx = sequence.index(before)
            after_idx = sequence.index(after)
            
            if before_idx > after_idx:
                # Swap elements
                sequence[before_idx], sequence[after_idx] = sequence[after_idx], sequence[before_idx]
    
    return sequence

def main():
    # Parse input
    rules, sequences = parse_input()
    
    # Part 1: Process valid sequences
    part1_sum = 0
    invalid_sequences = []
    
    for sequence in sequences:
        if check_sequence_validity(sequence, rules):
            part1_sum += get_middle_value(sequence)
        else:
            invalid_sequences.append(sequence)
    
    # Part 2: Fix and process invalid sequences
    part2_sum = sum(get_middle_value(fix_sequence(seq, rules)) 
                   for seq in invalid_sequences)
    
    print(part1_sum)
    print(part2_sum)

if __name__ == '__main__':
    main()
