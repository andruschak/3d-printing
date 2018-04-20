# Adventures in 3d-printing

First foray into 3D Printing - document is a work in progress


I figured it was time to give 3D printing a go. I wanted to post my experiences and track it as a project.





### Printer Criteria:

I knew I wanted a printer (ever since I saw the first RepRaps && Makerbots) but figured they were too expensive. I love the idea of an Ultimaker, not so much the $2500+ price tag. After researching a bunch of 3D printers (through 2017) I landed on the Anet A8 (which is a Prusa i3 clone). Many may not agree as they've been known to start fires, however, it ticked off a bunch of marks on my printer criteria.
 

- [x] Required assembly
- [x] Entry level price (<500$ - picked up this one for 275$ CAD)
- [x] Decent build plate size (in this case - 220x220x240mm)
- [x] Open source/community/hackable (big finger to proprietary)
- [x] Compatible with models from Thingiverse
- [x] Supports multiple different filament types
- [ ] Ethernet/Wifi connectivity
- [ ] Non-fire causing
- [ ] Enclosed 
- [ ] Metal Frame 
- [ ] Dual Extruder (can be used to make dissolvable support structures)

The beauty of the A8 is the modability. Many of the deficiencies can be overcome with some creativity and the open source community. The Ethernet/Wifi connectivity can be solved with a raspberry pi and [Octoprint](https://octoprint.com). Non-fire causing and other safety concerns addressed via hardware (part/wiring/mosfet upgrades) and software (skynet 3D firmware). Enclosures can be built to surround the printer. Dual extruders are something I havent looked into, but would likely be a bit more challenging.


### Resources

Yuge list of resources for the A8:

[3DPrint.Wiki](https://3dprint.wiki/reprap/anet/a8)

I'm not a facebook guy but this is a great group to lurk on:

[Official, Anet, A8R 3D printer Support Group (Inc RepRap Prusa i3 clones)](https://www.facebook.com/groups/1068531466501015)

Good write up on steps for after build:

[Best Upgrades for Anet A8 3D Printer](https://pevly.com/anet-a8-upgrades/)


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
 

 

### Initial Configuration and Leveling

This took a bit of experimenting. My kit came with an auto-leveling sensor which I didn't install until after my first couple prints. At first, I did not realize that the auto-level actually replaces the need for the physical z-axis switch. Again, youtube to the rescue.

Also, I found when using a piece of A4 paper to calibrate, I got best results when it was a light drag on the paper vs a heavy press.

I left the 4 corners of the bed about 1/2 way tightened. Many said to tighten all the way down to start, but I found I had to drop the bed in order to get the right height, so it took a couple retries. Make sure to tighten the wingnuts snug before printing - I had 1/2 a side come loose after a print and throw my calibration out of whack.


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

The first prints confused me a bit as it was creating a dummy layer around the base. Turns out this is totally normal, in fact, it is called a "brim".

I did end up getting a glass plate with binder clips to try. Honestly though, the taping setup (its cheap and not too much of a pain) is working fine. Adhesion is good and removal fairly painless (worst case it mungs up the tape job).



## Upgrade Prints

[Anet A8 Prusa i3 Simple filament guide (Horizontal)](https://www.thingiverse.com/thing:1764285)

[Hesine M-505, Anet A8 - Center Nozzle Fan](https://www.thingiverse.com/thing:1620630)

[Remixed Y axis belt tightener for A8, A6](https://www.thingiverse.com/thing:1755471)

[Anet A8 T corner](https://www.thingiverse.com/thing:1672959)

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

### The build continues

I think by now, i've probably got around 20h of print time under my belt. Now that I have gotten to know the system fairly well. 

There is a lot of buzz on the Internet regarding this machine. 

### Safety


Upgrade firmware 
- to enable thermal runover protection

Secure moving cables 
- to prevent movement fatigue

Isolate Heatbed via MOSFET


Replace the PSU



------

Next steps

- [ ] Safety upgrades
- [ ] Highlevel gcode information
- [ ] Write up on 2D plotting
- [ ] Glass plate (ordered, but pretty happy with the painters tape)
- [ ] Flash firmware to Marlin (Skynet 3D)
- [ ] Build octoprint box from rpi