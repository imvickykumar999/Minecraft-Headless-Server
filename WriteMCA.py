from CallMe import MAZE3D_generator as mzg
from CallMe import MAZE3D_solver as mzs
import anvil
import os

# Path to the world region folder
world_region_path = os.path.join("world", "region", "r.0.0.mca")

# ✅ Load existing region (if exists) instead of wiping it
if os.path.exists(world_region_path):
    region = anvil.Region.from_file(world_region_path)
else:
    region = anvil.EmptyRegion(0, 0)

chunk = 2
tall = 250
side = 16 * chunk - 1

gold_block = anvil.Block('minecraft', 'gold_block')
glowstone = anvil.Block('minecraft', 'glowstone')
diamond_block = anvil.Block('minecraft', 'diamond_block')
blue_stained_glass = anvil.Block('minecraft', 'blue_stained_glass')

for y in range(-63, tall, 10):  # floor
    us_maze = mzg.returnMaze(side, side)
    s_maze = mzs.solve_maze(us_maze)

    for x in range(side):
        for z in range(side):
            if s_maze[x][z] == 'w':
                region.set_block(diamond_block, x, y+1, z)
                region.set_block(diamond_block, x, y+2, z)

            if y == -63 or not (x == 1 and z == 1):
                region.set_block(gold_block, x, y, z)

            if s_maze[x][z] == 'p':
                region.set_block(glowstone, x, y, z)

for x in range(side):  # walls
    for y in range(-63, tall - 1):
        for z in range(side):
            if x == 0 or x == side - 1 or z == 0 or z == side - 1:
                region.set_block(blue_stained_glass, x, y, z)

# ✅ Save back to the correct region file in the world folder
region.save(world_region_path)
print('\nBuild Complete.')
