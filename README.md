# Photos Organizer
That's my first python program. The idea is compare images of a folder and separate them if they are the same.

The project rises while I was organizing my photos in my cellphone and realized that tons of them was replicated.<br>
So I used Pillow in Python 3 to make it.

## How to use
Here I'm running the program directly in the folder I want to organize.

### Python
You can download the only .py file this project has or clone it.

Things you can change
<ul>
  <li>I let the percentage displaying as the program is running, you can delete that at <b>fotos</b> function</li>
  <li>What you want to...</li>
</ul>

After that, you need to make the .exe file from it. I'm using Pyinstaller.
Use pip to install and then run: <b>pyinstaller [name of your file].py</b>

In the project folder it's going to create the folder <b>dist/main</b>

### .exe
Now we already have our file. The next step is create a folder in <b>Program Files</b> folder and paste all files from <b>dist/main</b> there.
We're done for here.

### Adding to the Windows menu
To use the program in any folder you want we're going to add it to Windows menu <i>(left click)</i>.

From the folder that you put the .reg file run it on terminal.<br>
<i>(edit it if the name of your files and folders are differents)</i>

Now add the path to your .exe file on the Environment Variables.

#### THE END

<a href='https://instagram.com/cristian_ucf'>Instagram</a>
