#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 09:12:31 2020

@author: podolnik
"""

import re

data = []

with open('input.txt', mode='r') as f:
    pattern = '([A-Z]{1})([0-9]*)'
    text = f.read()
    matches = re.findall(pattern, text)
    data = [(m[0], int(m[1])) for m in matches]

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dir_names = ['E', 'S', 'W', 'N']
rotations = {'L': -1, 'R': 1}

# part 1

def go(current_pos, current_dir, handle, value):
    if handle in dir_names:
        next_dir = directions[dir_names.index(handle)]
        next_pos = (current_pos[0] + next_dir[0] * value, current_pos[1] + next_dir[1] * value)
        return next_pos, current_dir
    if handle in rotations:
        i = directions.index(current_dir)
        n = int(value / 90)
        next_dir = directions[(i + rotations[handle] * n) % len(directions)]
        return current_pos, next_dir
    elif handle == 'F':
        next_pos = (current_pos[0] + current_dir[0] * value, current_pos[1] + current_dir[1] * value)
        return next_pos, current_dir

position = (0, 0)
direction = (0, 1)        

for inst in data:
    position, direction = go(position, direction, inst[0], inst[1])

print(abs(position[0]) + abs(position[1]))    

# part 2

rot_mat = {'L': [[0, 1], [-1, 0]], 'R': [[0, -1], [1, 0]]}

def rotate(mat, vec):
    v_0 = vec[0] * mat[0][0] + vec[1] * mat[0][1]
    v_1 = vec[0] * mat[1][0] + vec[1] * mat[1][1]
    return (v_0, v_1)

def go_w(waypoint_pos, current_pos, handle, value):
    if handle in dir_names:
        next_dir = directions[dir_names.index(handle)]
        waypoint_pos = (waypoint_pos[0] + next_dir[0] * value, waypoint_pos[1] + next_dir[1] * value)
        return waypoint_pos, current_pos
    if handle in rot_mat:
        mat = rot_mat[handle]
        n = int(value / 90)
        waypoint_pos = rotate(mat, waypoint_pos)
        for i in range(n - 1):
            waypoint_pos = rotate(mat, waypoint_pos)
        return waypoint_pos, current_pos
    elif handle == 'F':
        n_0 = waypoint_pos[0]
        n_1 = waypoint_pos[1]
        next_pos = (current_pos[0] + value * n_0, current_pos[1] + value * n_1)
        return waypoint_pos, next_pos

position = (0, 0)
waypoint = (1, 10)

for inst in data:
    waypoint, position = go_w(waypoint, position, inst[0], inst[1])

print(abs(position[0]) + abs(position[1]))    

vec = (0, 10)
mat = rot_mat
    