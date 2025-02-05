#!/bin/bash

canJump() {
    local nums=("$@")  # Capture all arguments as an array
    local n=${#nums[@]}  # Get the length of the array
    local goal=$((n - 1))

    for (( i = n - 2; i >= 0; i-- )); do
        if (( i + nums[i] >= goal )); then
            goal=$i
        fi
    done

    if (( goal == 0 )); then
        echo "True"
    else
        echo "False"
    fi
}

# Example: calling the function with a list
canJump 2 3 1 1 4
