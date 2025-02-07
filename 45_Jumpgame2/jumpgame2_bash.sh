#!/bin/bash

function jump {
    nums=("$@")  # All arguments passed to the function
    n=${#nums[@]}  # Length of the array
    jumps=0
    farthest=0
    current_jump_end=0

    # Loop through the array up to the second to last element
    for ((i=0; i<n-1; i++)); do
        # Update the farthest position we can reach
        farthest=$((farthest > i + nums[i] ? farthest : i + nums[i]))

        # When we reach the end of the current jump, increment the jump count
        if [[ $i == $current_jump_end ]]; then
            ((jumps++))
            current_jump_end=$farthest

            # If we can reach or go beyond the last index, break out of the loop
            if [[ $current_jump_end -ge $((n-1)) ]]; then
                break
            fi
        fi
    done

    echo $jumps
}

# Example Usage:
nums=(2 3 1 1 4)
jump "${nums[@]}"
