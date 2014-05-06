Subtitle Corrector
==================

You know how annoying it is when your subtitles do not sync with the video you are watching.
Subtitle Corrector is a tool to make subtitles sync with your video.

### Requirements
* Python3.x

### Installation
Clone the repo
`git clone https://github.com/sunilkumarc/subtitle-corrector.git`

Then run installation script
`./install.sh`

### How to use
Now you can use the tool to correct the subtitles file(.srt)
Example : 
If you have a subtitle file example.srt and you want all the subtitles 
to come 1 seconds earlier in the video then you can run the command

`corrector example.srt -1`

If you want the subtitles to come 2 second later, then run the command

`corrector example.srt 2`

After you run the command, the tool will update your subtitles file.

To uninstall the tool, run the command

`corrector-uninstall`


