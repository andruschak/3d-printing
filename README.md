# Adventures in 3d-printing

First foray into 3D Printing


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
- [ ] Non-fire causing*
- [ ] Enclosed
- [ ] Metal Frame
- [ ] Dual Extruder

 

### Resources

Yuge list of resources for the A8:
wiki: https://3dprint.wiki/reprap/anet/a8


I'm not a facebook guy but this is a great group to lurk on:
fb group: https://www.facebook.com/groups/1068531466501015

 

 

# Building

### Some assembly required

Overall, I have to say, this was an awesome experience.

The instructions that came with the printer are in Chinese, which made it difficult to build from the manual - so onto youtube. I found a couple good vids on the process but continued to reference the official manual to ensure I was using the right screw for the right part. That added some serious time but it never hurts to double check.

The molded x-axis motor mount had a slight crack in it but didnt look like it would affect operation. On that note though, the x-axis rods were an insanely tight fit. I would recommend test assembling that before you have it all put together (I had to back step a bit here). I used some fine sandpaper to open the holes up a bit so the rods would fit flush.

Altogether it probably took me a solid 8-10h to build. That was broken up over a 3 days. I left the brown sticker on the acrylic because I think it ends up looking cooler - and saved me a ton of peeling time. That did mean everything fit a bit more snug but it will probably add some strength to the overall chassis in the end.

As a final note, wrapping the cabling was a bit more challenging than I thought. Ive done a lot of computer builds in my day and feel I am pretty adept at cable management. I will admit, this took me a few times to get wired the way I wanted. Adding in the auto-leveller later forced me to re-wrap the extruder bundle.

# Eye-candy

![kit as it came](https://github.com/andruschak/3d-printing/blob/master/images/kit-small.png)
Kit as it came in the box 

![basic frame taking shape](https://github.com/andruschak/3d-printing/blob/master/images/basic-frame-small.png)
Basic frame starting to look like a printer

![mid build, pre electronics](https://github.com/andruschak/3d-printing/blob/master/images/physical-complete-small.png)
Physical is complete, onto electronics 

![finished printer](https://github.com/andruschak/3d-printing/blob/master/images/finished-small.png)
The finished printer
 

 

### Initial Configuration and Leveling

This took a bit of experimenting. My kit came with an auto-leveling sensor, which I didnt install until after my first couple prints. I didnt realize that the auto-level actually replaces the need for the physical z-axis switch. Again, youtube to the rescue.

Also, I found when using a piece of A4 paper to calibrate, I got best results when it was a light drag on the paper vs a heavy press.

I left the 4 corners of the bed about 1/2 way tightened. Many said to tighten all the way down to start, but I found I had to drop the bed in order to get the right height, so it took a couple retries. Make sure to tighten the wingnuts snug before printing - I had 1/2 a side come loose after a print and throw my calibration out of whack.

### Adhesion

Admittedly still new to this. The hotbed came pre-tapped from the factory and I mistakenly peeled it off to free my first build. Quick lesson... masking tape doesnt work as a substitute. Snagged some blue extra-wide painters tape and it works beautifully.


The first prints confused me a bit as it was creating a dummy layer around the base. Turns out this is totally normal, in fact, it is called a "brim".

 
# Printing

#### First print

- pictures of prints

#### Second print

- pictures of prints

 
# Software

There are a ton of packages out there you an use. For quick results I wanted to be able to browse Thingiverse and convert the stl to gcode - cure came highly recommended. Although I wouldnt mind trying a few others.

Ultimaker cura: https://ultimaker.com/en/products/ultimaker-cura-software


Anet A8 settings

- Table of tried settings and pics of prints with those settings?

 


Next steps

- [ ] Support structure mods
- [ ] Glass plate (ordered, but pretty happy with the painters tape)
- [ ] Flash firmware to Marlin (Skynet 3D)
- [ ] Build octoprint box from rpi