# Adventures in 3d-printing

First foray into 3D Printing - document is a work in progress


I figured it was time to give 3D printing a go. I wanted to post my experiences and track it as a project. Of course YMMV and I take no responsibility for anything that happens.


## Part 1. From box to build

### Printer Criteria:

I knew I wanted a printer (ever since I saw the first RepRaps && Makerbots) but figured they were too expensive. I love the idea of an Ultimaker, not so much the $2500+ price tag. After researching a bunch of 3D printers (through 2017) I landed on the Anet A8 (which is a Prusa i3 clone). Many may not agree as they've been known to start fires, however, it ticked off a bunch of marks on my printer criteria.
 

- [x] Required assembly
- [x] Entry level price (<500$ - picked up this one for 275$ CAD)
- [x] Decent build plate size (in this case - 220x220x240mm)
- [x] Open source/community/hackable (big finger to proprietary)
- [x] Compatible with models from Thingiverse
- [x] Supports multiple different filament types
- [x] Ethernet/Wifi connectivity (*NEW*)
- [x] Non-fire causing* (precautions taken) (*NEW*)
- [ ] Enclosed 
- [ ] Metal Frame 
- [ ] Dual Extruder (can be used to make dissolvable support structures)

The beauty of the A8 is the modability. Many of the deficiencies can be overcome with some creativity and the open source community. The Ethernet/Wifi connectivity was solved with a raspberry pi and [Octoprint](https://octoprint.com). Non-fire causing and other safety concerns addressed via hardware (part/wiring/mosfet upgrades) and software (Marlin firmware). Enclosures can be built to surround the printer. Dual extruders are something I havent looked into, but would likely be a bit more challenging.

A note about toxicity. It's important to understand the risks with 3D printing. At the moment my interest is with PLA which seems to be fairly harmless (emissions/non-toxic) vs. ABS which emits formaldehyde and other particulates. I'd recommend watching a series of studies done by [diy3dtech](http://diy3dtech.com/3d-printing-and-air-quality-risks/)


### Resources

[3DPrint.Wiki](https://3dprint.wiki/reprap/anet/a8) - Yuge list of resources for the A8

[Official, Anet, A8R 3D printer Support Group](https://www.facebook.com/groups/1068531466501015) - I'm not a facebook guy but this is a great group to lurk on


###### Post build
[Best Upgrades for Anet A8 3D Printer](https://pevly.com/anet-a8-upgrades/) - Good write up on steps for after build

[25 Must have upgrades for the Anet A8](https://all3dp.com/1/anet-a8-upgrades-mods/) - Another decent write up, this time as a top 25

[Simplify3d Quality Troublshooting Guide](https://www.simplify3d.com/support/print-quality-troubleshooting/) - Help with common print issues


###### Few sites for models:

[Thingiverse](https://www.thingiverse.com/) - word of caution - ensure it has some build counts and a pic

[MyMiniFactory](https://www.myminifactory.com) - currated list of builds


 ------

# Building

### Some assembly required

Overall, I have to say, this was an awesome experience.

The instructions that came with the printer are in Chinese, which made it difficult to build from the manual - so onto youtube. I found a couple good vids on the process but continued to reference the official manual to ensure I was using the right screw for the right part. That added some serious time but it never hurts to double check.

The molded x-axis motor mount had a slight crack in it but didnt look like it would affect operation. On that note though, the x-axis rods were an insanely tight fit. I would recommend test assembling that before you have it all put together (I had to back step a bit here). I used some fine sandpaper to open the holes up a bit so the rods would fit flush.

Altogether it probably took me a solid 8-10h to build. That was broken up over a 3 days. I left the brown sticker on the acrylic because I think it ends up looking cooler - and saved me a ton of peeling time. That did mean everything fit a bit more snug but it will probably add some strength to the overall chassis in the end.

As a final note, wrapping the cabling was a bit more challenging than I thought. Ive done a lot of computer builds in my day and feel I am pretty adept at cable management. I will admit this took me a few times to get wired the way I wanted. Adding in the auto-leveller later forced me to re-wrap the extruder bundle. I also managed to cut through one of the ground cables to when snipping the cable wrap - rookie move - fixed it with a quick solder. Maybe that just adds character?

# Eye-candy

### Few shots of the build process

![kit as it came](https://github.com/andruschak/3d-printing/blob/master/images/kit-small.png)
Kit as it came in the box 

![basic frame taking shape](https://github.com/andruschak/3d-printing/blob/master/images/basic-frame-small.png)
Basic frame starting to look like a printer

![mid build, pre electronics](https://github.com/andruschak/3d-printing/blob/master/images/physical-complete-small.png)
Physical is complete, onto electronics 

![finished printer](https://github.com/andruschak/3d-printing/blob/master/images/finished-small.png)
The finished printer
 

### Garbled LCD

The LCD ribbon isnt sheilded and initially I encountered issues with garbled characters. Moving the bed and extruder cabling away from the ribbon solved the issue. *UPDATE* this issue cropped up again with the switch to the Marlin Firmware, see below.
 

### Initial Configuration and Leveling

I wanted to use the default firmware for the first few prints to make sure it would work as expected. This took a bit of experimenting. My kit came with an auto-leveling sensor which I didn't install until after my first couple prints. At first, I did not realize that the auto-level actually replaces the need for the physical z-axis switch. Again, youtube to the rescue.

The default firmware had an auto-level menu selection. This would move the nozzle to the lf, rf, rb, lb allowing you to tweak the paper drag under each test point. It seemed to work fine.

Also, I found when using a piece of A4 paper to calibrate, I got best results when it was a light drag on the paper vs a heavy press.

I left the 4 corners of the bed about 1/2 way tightened. Many said to tighten all the way down to start, but I found I had to drop the bed in order to get the right height, so it took a couple retries. Make sure to tighten the wingnuts snug before printing - I had 1/2 a side come loose after a print and throw my calibration out of whack.

Updated below: Initial Configuration and Leveling of the Firmware update section

------

# Software

There are a ton of packages out there you can use. For quick results I wanted to be able to browse Thingiverse and convert the stl to gcode - cura came highly recommended. It was quite easy to pick up and learn. The printer cannot handle .stl files directly, so cura is needed to generate a gcode file (more on these later).

### Slicers

[Ultimaker cura:](https://ultimaker.com/en/products/ultimaker-cura-software) quick and easy out of the box. Running in Win10.

I must say after spending a couple hours using Cura I am pretty happy with its balance of features vs usability. It took a little while to get used to the interface (it looks to have gone through GUI change recently making many old posts obsolete). 

Setup was easy. Install and run. It prompted for a default printer (I picked Pruse i3 clone) but still had to go into the device and modify the bed size parameters.  

Loading models was easy as well. Open the .stl file and it will import into the application. It also auto detected the SDcard and prompted to save and eject (its the little things!)

Pay particular attention to the settings on the right hand side. You can see mine attached. Note there is a section for "generating support". This instructs the printer to build disposable support structures. 

A cool feature is enabling the layers view, selecting a specific layer and watching it simulate the print. 

It also has usb support for hooking directly to your printer but I havent tried that.

![Cura screenshot with settings](https://github.com/andruschak/3d-printing/blob/master/images/360-cooler.png)


### 3d Model Creation

I hope to start creating my own models shortly, the in mean time, here are a few links.

[Sketchup:](https://www.sketchup.com/) Formally Google Sketchup. Ive used this in other projects. Pretty good and free.

[Fusion 360:](https://www.autodesk.com/products/fusion-360/students-teachers-educators) havent read much into it yet. Suppose to be complete and free - with learning curve


------
 
# Printing

### Anet A8 settings

This is close to the defaults that came with Cura under draft quality. For simple prints it has been excellent. The temps were what the machine was set to by default (200F/60F).

I am currently trying a more complex build to see how to holds up. Watch the "support" check. It will auto generate supports for overhangs. Printing my first support in aforementioned complex build. You can view the layers by selecting the object and the layers button.

Name   | Setting
------------ | -------------
Layer Height | 0.2
Wall Thickness | 0.8
Infill | 20
Print Temp | 200
Build Plate Temp | 60
Diameter | 1.75mm
Flow | 100
Speed | 60
Travel | 120
Cooling | Y
Support | Y
Adhesion | Brim
Width | 8

### Adhesion

Admittedly still new to this. The hotbed came pre-tapped from the factory and I mistakenly peeled it off to free my first build. Quick lesson... masking tape doesnt work as a substitute. Snagged some blue extra-wide painters tape and it works beautifully.

The first prints confused me a bit as it was creating a dummy layer around the base. Turns out this is totally normal, in fact, it is called a "brim", and is designed to break off the final print. If you have issues with the brim layer it is likely your bed leveling or z-offset is out of whack (important lessons learned!). You can also select raft or skirt as possible preprint selections. I've never tried raft, but use skirt regularly. My printer seems to have a slight delay in extruding so it gets the filament flowing. I usually end up with only 3/4 of the skirt though.

I did end up getting a glass plate with binder clips to try. But I am not sure how well the inductive sensor will work having a glass buffer before the bed (may require a sensor swap). Honestly though, the taping setup is cheap and is working fine. Adhesion is good and removal fairly painless. The worst case is a munged up tape job. The only downside to the tape so far is that it results in a less than perfect print face because of the tape lines on the bed. 

### Notes on filament

I knew it wouldn't take long until I ran out of the small roll of white PLA (25m ?) that came with the printer. However, it produced a 360 cooling blower, 2 T brackets, a pen holder and a heart shaped trinket for the Mrs. Overall, I must say, I am pleasantly surprised at the ratio of print to raw material put in.

For starters I am mainly interested in PLA. Truth by told, I havent done a ton of research on the different types of printable material out there. According to the wiki, this printer supports a pretty wide range - ABS/PLA/TPU/Wood/Nylon/PVA/PP/Luminescent.

PLA doesn't have much of a smell which is nice.

For replacement, I picked up a couple 1kg rolls of AMZ3D PLA in orange and black. They get decent reviews online and have come recommended by a few friends so I thought I would give it a try. Came to about 25$ with shipping for each roll.

Changing the filament was pretty simple. There are a few different methods. I enabled PLA preheat to get it up to the melting point, cut the old filament flush with the entrance to the extruder, cut a point on the end of the new spool, and started to push a bit. Once it bit I used the menu stepper control to feed it though, voila, the white turned black and it was good to go. I didn't end up taking off the front mount fan. I have heard it can be a pain in the ass but the previous method seemed to work for me.

Just to note, there are many different ways advocated on the net. Some take off the fan, just push it through, some pull it out (though it can get cool and stuck forcing you to take things apart).

### Support or no support?

This really depends on what you're printing. I've found if I can get away without supports it is better. This is especially true when you want parts to slot together.

If the area is super tight it can be very hard to pull out the small breakaway parts. 

I've found it is possible to print 45 degree angles without support. Benchy's are designed to be printed without support and really highlight whats possible. I'd say by default I woud try to avoid.

## Upgrade Prints

[Anet A8 T corner](https://www.thingiverse.com/thing:1672959)

[Anet A8 Prusa i3 Simple filament guide (Horizontal)](https://www.thingiverse.com/thing:1764285)

[Hesine M-505, Anet A8 - Center Nozzle Fan](https://www.thingiverse.com/thing:1620630)

[Remixed Y axis belt tightener for A8, A6](https://www.thingiverse.com/thing:1755471)

[Heatbed Cable Holder for Anet A8](https://www.thingiverse.com/thing:1875869)

[AMZ3D PLA spool hub](https://www.thingiverse.com/thing:1955324)

## Example prints

I will upload more as I go.

![printing air cooler mod](https://github.com/andruschak/3d-printing/blob/master/images/printing-360-aircooler-small.png)

360 cooling to replace stock fan extruder blower. As seen in Cura screenshot above.

![pen holder for 2D plotting](https://github.com/andruschak/3d-printing/blob/master/images/finished-pen-holder-small.png)

Little more complex - pen holder to convert the printer to a 2D plotter. Quality has improved since first couple prints, tweaking software settings

![T bracket mod](https://github.com/andruschak/3d-printing/blob/master/images/finished-t-small.png)

Allows for a more rigid frame. Definate improvement in quality. Seems the A8 likes multiples of 4 in certain settings

##### Timelapse Video
[![Youtube Timelapse](https://img.youtube.com/vi/Xh2m-gPxqYk/0.jpg)](https://www.youtube.com/watch?v=Xh2m-gPxqYk)

Timelapse video of T bracket build


##### Print evolution

Same part, many tweaks. Show the 2nd print and the 8th print. Maybe the alien prints?


------

## Part 2: The build continues

After 25h or so of printing, I have gotten to know the basics fairly well. What better time to start over with a new firmware and updated settings? This process was pretty straight forward though there are many possible pitfalls. 

### Safety

There is a lot of buzz on the Internet regarding this machine and it's potential hazards. It is highly recommended by the online community to perform some upgrades. I will cover, securing cabling for the hotbed and extruder, installing a mosfet and flashing the firmware.

##### Hardware

Secure moving cables to prevent movement fatigue on the connectors to the bed and extruder. 

Picture of the bed

Picture of the extruder

Isolate Heatbed via MOSFET


##### Software

Upgrade firmware - Marlin 1.1.8 (at time of writing)

There are some reasons for upgrading:

- to enable thermal runaway protection 
- (better) auto-leveling support - my original a8 firmware had some sensor support (4 point)
- control of features and menu items
- review the code yourself
- you want a garbled LCD display (seems to be a bug)


There are good resources on how to do the install. Apparently you can use a native framwork (platform.io?) to configure and upload. I went the arduino path as I have a lot of experience in that space. Pay special attention to the settings in configuration.h - there were many tweaks I had to make here in order to accomodate for placement of the z-axis sensor and bed cable bracket. There are tons of experiemental componants commented out - like printing chocolate or driving LED lights!

Here are the highlevel steps I followed:

- Download arduino software
- Download Skynet 3D drivers (for arduino hardware plugin)
- Download Marlin 1.1.8
- Unzip em all
- install arduino
- Copy Skynet "hardware" folder into your arduino user dir
- Copy Marlin example for anet a8 configuration.h and configuration_adv.h to root Marlin folder and overwrite the existing files
- Fire up the Marlin.ino file and edit on of the files you just copied in the arduino IDE
- Edit Configuration.h - see below
- Connect the printer to the computer via usb
- Select the Anet 1.0 board
- Select the proper comm port
- Click the "->" to compile and upload to the printer
- The printer will reboot and you're good to go!

There are a few differences in this firmware compared to stock. The button selections have changed, center is menu and ok for example.

##### Configuration.h file

*** Make sure you go through this file and understand what it is doing or you can end up doing nasty things! ***

```
// increased the jerk rate by 10 (original 10)
define DEFAULT_XJERK                 20.0
define DEFAULT_YJERK                 20.0
define DEFAULT_ZJERK                  0.3
define DEFAULT_EJERK                  5.0

// replaces the default Z-Axis (expects same pin)
define Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN

// enable fixed probe – mine is inductive
define FIX_MOUNTED_PROBE

// set the location of the probe in relation to the Nozzle (off the back of the extruder module – from wiki)
define X_PROBE_OFFSET_FROM_EXTRUDER 15   // X offset: -left  +right  [of the nozzle]
define Y_PROBE_OFFSET_FROM_EXTRUDER 55   // Y offset: -front +behind [the nozzle]
define Z_PROBE_OFFSET_FROM_EXTRUDER 1   // Z offset: -below +above  [the nozzle]

// bed leveling algorithm – 9-point touch
define AUTO_BED_LEVELING_BILINEAR

// modified the 9 point touch to not hit the printed bed cable holder
define LEFT_PROBE_BED_POSITION 15
define RIGHT_PROBE_BED_POSITION 190
define FRONT_PROBE_BED_POSITION 45
define BACK_PROBE_BED_POSITION 160

// in case you’re off the bed and there is no metal for the sensor to sense
define Z_SAFE_HOMING
```

------

##### LCD garbling - revenge!

Deja Vu - a garbled LCD - didn't we talk about this earlier?

Well, it appears to be an issue with the A8 LCD and the Marlin software. Some comments seem to indicate a problem with the arduino refresh rates and the A8 setup. Others talk about interference. It seems hit or miss in my experience, however, it happens during more prints. It is possible to click right-right-menu-menu to have it reset without impact to the print process. I am going to try and sheild the cable to see if that helps.

In the meantime, I hope it is something fixed in software.

![Garbled LED](https://github.com/andruschak/3d-printing/blob/master/images/garbled-display.jpg)

### gcode

gcode is a machine instruction language. Through a series of "codes", instructions are sent to machines to perform certain tasks. In the case of 3D printing it tells the printer how to create each layer. The gcode file is plain-text and is generated by Cura (or other software) after slicing.

Additional gcode commands link

Here is a sample cura file with comments:

```
;FLAVOR:Marlin
;TIME:9769
;Filament used: 11.6661m
;Layer height: 0.2
;Generated with Cura_SteamEngine 3.2.1
M190 S60
M104 S200
M109 S200
M82 ;absolute extrusion mode
G21 ;metric values
G90 ;absolute positioning
M82 ;set extruder to absolute mode
M107 ;start with the fan off
G28 X0 Y0 ;move X/Y to min endstops
G28 Z0 ;move Z to min endstops
G1 Z15.0 F9000 ;move the platform down 15mm
G92 E0 ;zero the extruded length
G1 F200 E3 ;extrude 3mm of feed stock
G92 E0 ;zero the extruded length again
G1 F9000
;Put printing message on LCD screen
M117 Printing...
;LAYER_COUNT:199
;LAYER:0
M107
G0 F3000 X62.137 Y58.904 Z0.3
;TYPE:SKIRT
G1 F1800 X62.574 Y58.466 E0.03087
G1 X64.341 Y57.007 E0.14519
G1 X64.673 Y56.767 E0.16563
G1 X65.478 Y56.26 E0.21309
```

##### Pre/Post gcode

Sample post - move bed out instead of in. 

------

### Octoprint

Octoprint is a web interface for your printer. It allows you to control and monitor every aspect of your 3D printer and your printing jobs right from within your browser. One thing to note is the webcam is viewable without logging in.

It offers a ton of great features:

- Open source (fits our conditions above)
- RPI image
- Full print control via web interface
- Video Streaming/Timelapse (keep an eye on the printer when out of the room!)
- Slicing on box
- Plug-ins (stats, history, push notifications, etc..)
- Custom UI scripts (turn on/off, control LEDs, others?)
- Custom touch screen support

Here is the highlevel steps I used (took 15mins):

- Download octopi (0.14 at time of writing)
- Flash using Etcher
- Edit the octopi-network.txt file, uncomment and add your wifi information
- Boot up rpi with camera
- Log into web interface
- Follow wizard (assigning proper values)
- Connect the usb and test
- Print!

So far I am very impressed with the Octoprint and would recommend giving it a try. It adds a whole new dimension to the experience. Being able to watch the feed from anywhere is nice. 

Previously I was slicing on the PC and using the SD card (which worked well). I am still using the PC for slicing but drag/dropping to the web interface.

Screenshot

Screenshot

Screenshot

##### Octoprint API

I've been looking to pull some stats out of octoprint to display on a micro-phat. I was able to pull basic info with curl. 

```
curl -i -k -H "Content-Type: application/json" -H "x-api-key:XXXXXXXXXXXXXXXXXXXXXXXXXX" -X GET https://octoprint.local/api/version

HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 40
Cache-Control: max-age=0
X-Clacks-Overhead: GNU Terry Pratchett
Set-Cookie: session_P443=.eJyrVopPK0otzlCyKikqTdVRis9MUbKqVlJIUrJSisryy_B38cr2zY009qtKNvTNda3yD4-sjMrKyYhyCS2Pcg_L8DVyNfAP8bVVqtVRykxJzSvJLKnUSywtyYgvqSxIVbLKK83JQZJBMj3CyK0  8MdAWrLO0OLUoHqtcLQDapDRp.DdO2eA.C7_ZDuNHEctv78qnk8vYHpv3KcY; Path=/; HttpOnly
X-Robots-Tag: noindex, nofollow, noimageindex

{
  "api": "0.1",
  "server": "1.3.8"
}
```


------

## Next steps

- [-] Safety upgrades
- [ ] Highlevel gcode information
- [ ] Write up on 2D plotting
- [ ] Glass plate (ordered, but pretty happy with the painters tape)
- [ ] Flash firmware to Marlin (Skynet 3D is obsolete)
- [-] Build octoprint box from rpi


## Prints

![Articulating butterfly](https://github.com/andruschak/3d-printing/blob/master/images/butterfly.jpg)

![Batman Headphone Stand](https://github.com/andruschak/3d-printing/blob/master/images/bm-headphone-stand.jpg)

![Google Home Mini Wall Hanger](https://github.com/andruschak/3d-printing/blob/master/images/gh-holder.jpg)

