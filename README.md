# libgamestart
We provide cleaner syntax for Python programming in Minecraft. Supported platforms are minecraft-pi for Raspbian, [CanaryRaspberryJuice](http://www.stuffaboutcode.com/2014/10/minecraft-raspberryjuice-and-canarymod.html) for Windows, and Play Minecraft on Kano.

    from libgamestart import *    #this line is required at the top of all your scripts! :D
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    cube(0, 20, 0, TNT, 6)
    teleport(0, 30, 0)
    setblock(player.x, player.y, player.z, DIAMOND_BLOCK)
    
In order for the required import statement to be meaningful, we must place the library in Python's path. The easiest way to do this is to copy libgamestart to the [PYTHONHOME](https://docs.python.org/2/using/cmdline.html#envvar-PYTHONHOME) folder.

    sudo cp libgamestart.py /usr/lib/python2.7    # Raspbian and Kano
    sudo cp -r mcpi /usr/lib/python2.7            # Kano only. They renamed the mcpi directory to "minecraft" so we want our own copy with the conventional name "mcpi"

For CanaryRaspberryJuice on Windows, just copy libgamestart.py and the mcpi folder into the PYTHONHOME folder; usually c:\Python27\Lib
