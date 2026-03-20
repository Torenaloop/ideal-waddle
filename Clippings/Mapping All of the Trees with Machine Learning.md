---
title: "Mapping All of the Trees with Machine Learning"
source: "https://medium.com/descarteslabs-team/descartes-labs-urban-trees-tree-canopy-mapping-3b6c85c5c9cc"
author:
  - "[[Tim Wallace]]"
published: 2018-12-20
created: 2025-10-29
description: "Mapping All of the Trees with Machine Learning Note: This post was updated on January 3, 2019 to clarify that lidar was used as ground truth data to train the model only. Lidar is not needed to run …"
tags:
  - "clippings"
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)## [descarteslabs-meditations](https://medium.com/descarteslabs-team?source=post_page---publication_nav-96a6e5a6d5da-3b6c85c5c9cc---------------------------------------)

[![descarteslabs-meditations](https://miro.medium.com/v2/resize:fill:38:38/1*m8uizSm_fCH5_v4K4zQqLg.png)](https://medium.com/descarteslabs-team?source=post_page---post_publication_sidebar-96a6e5a6d5da-3b6c85c5c9cc---------------------------------------)

Explore posts from the Descartes Labs team

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*wZUjJ2qk9KSxE0_RUyoNOg.jpeg)

Descartes Labs built a machine learning model to identify tree canopy globally using a combination of lidar, aerial imagery and satellite imagery. Above are trees nestled around Baltimore highway interchanges.

> Note: This post was updated on January 3, 2019 to clarify that lidar was used as ground truth data to train the model only. Lidar is not needed to run the model; it requires only ~1m resolution four-band imagery (near infrared, red, green and blue) as inputs.

Much fuss has been made over city trees in recent years. Urban trees [reduce crime](https://www.sciencedirect.com/science/article/pii/S016920461630127X) and help [stormwater management](https://www.sciencedirect.com/science/article/pii/S0169204617300464) (yay!). [Cities and towns across the U.S. are losing 36 million trees a year](https://www.sciencedaily.com/releases/2018/04/180418141323.htm) (boo!). But, hold up— [climate change is accelerating the growth of urban trees in metropolises worldwide](https://www.nature.com/articles/s41598-017-14831-w) (boo/yay?). Urban trees are under such scrutiny right now that the U.N. even had a [World Forum on Urban Forests](http://www.fao.org/forestry/urbanforestry/en/) a few weeks ago to discuss the planning, design and management of urban forests and green infrastructure.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*6_sVAz9VWznbQ6ZFp7ElAg.jpeg)

The Descartes Labs tree canopy layer around the Baltimore Beltway. Treeless main roads radiate from the dense pavement of the city to leafy suburbs.

All this fuss is not without good reason. Trees are great! They make oxygen for breathing, suck up CO₂, provide shade, reduce noise pollution, and just look at them — they’re beautiful!

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*y9JIW79NniV0skiVa-4AwQ.jpeg)

8th Street in Park Slope, Brooklyn last May. Look at those beautiful trees!

The thing is, though, that trees are pretty hard to map. The 124,795 trees in the San Francisco Urban Forest Map shown below, for example, were cataloged over a year of survey work by a team of certified arborists. The database they created is thorough, with information on tree species and size as well as environmental factors like the presence of power lines or broken pavement.

But surveys like this are expensive to conduct, difficult to maintain, and provide an [incomplete picture](https://twitter.com/wallacetim/status/1073021053645930496) of the entire extent of the urban tree canopy. Both the San Francisco inventory below and the [New York City TreesCount](https://www.nycgovparks.org/trees/treescount)! do an impeccable job mapping the location, size and health of *street trees*, but exclude large chunks within the cities, like parks.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*RqsTOuZbqbfH_yZCPCtcGQ.gif)

San Francisco’s wonderful Open Forest Map tree inventory (point data) alternating with the Descartes Labs tree canopy layer (image data)

This data gap is neither accidental nor purposeful. As described in this tweet from SF Urban Forest, the trees they mapped were a product of bureaucratic choices and limitations—such as the case of mapping private property — and moving beyond those choices and limitations may take some time, if it happens at all.

![](https://x.com/i/status/1075175646190399488)

So, what’s the solution if we want to map tree canopies in places with such complex geographies? How do we fill in the gaps between official street tree census and trees in parks and on private property?

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*UIVFMDoL7IDplVYcjLNp9A.png)

New York City TreesCount! (circles) and the Descartes Labs tree canopy layer along Prospect Park West in Brooklyn. Note the city census does not include park trees or trees in private gardens.

Some savvy folks might reply, *C’mon, can’t we just fake it with a vegetation map?**Everyone’s all over* [*NDVI*](https://earthobservatory.nasa.gov/features/MeasuringVegetation) *these days, right?* Well… it’s not exactly that easy. Take a look at Boston below. Trees are only part of what’s green across the region.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*bZwTGQEI5rIteS4rC7TuSg.gif)

Boston vegetation (NDVI from an August 28, 2018 Sentinel 2 scene ) alternating with the Descartes Labs tree canopy layer — looks like quite a lot of that vegetation might not be trees! Those who know Boston may notice Fenway Park popping in and out because it doesn’t have trees (just grass and a Green Monster).

So Descartes Labs summer intern, [Aidan Swope](https://www.linkedin.com/in/aidan-swope-2600a614a), built a machine learning model to identify tree canopy from satellite imagery. To train the model, he identified known locations of tree canopy using lidar data and NAIP imagery over California. Using that as ground truth, the model was trained to classify which pixels contain trees in the corresponding satellite images. The result is a machine-learning model that has learned to identify trees just using four-band high-resolution (~1 meter) satellite or aerial imagery—no lidar required! This model can now be run anywhere in the world with high-resolution satellite imagery.

Here’s the area surrounding the Boston Common, for example. We clearly see that the Public Garden, Common and Commonwealth Avenue all have lots of trees. But we also see some other fun artifacts. The trees [in front of the CVS](https://binged.it/2rI5CDm) in Downtown Crossing, for instance, might seem inconsequential to a passer-by, but they’re one of the biggest concentrations of trees in the neighborhood.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*0ZSEBM2pgXDaM95rE8Iehw.jpeg)

Some of Boston’s tree canopy mapped by Descartes Labs

The classifier can be run over any location in the world where we have approximately 1-meter resolution imagery. When using [NAIP](https://www.fsa.usda.gov/programs-and-services/aerial-photography/imagery-programs/naip-imagery/) imagery, for instance, the resolution of the tree canopy map is as high as 60cm. Drone imagery would obviously yield an even higher resolution.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*wIsDPFDS_B2wD1JeXB0k4A.gif)

Washington, D.C. tree canopy created with NAIP source imagery shown at different scales—all the way down to individual “TREES!” on The Ellipse.

The ability to map tree canopy at a such a high resolution in areas that can’t be easily reached on foot would be helpful for utility companies to pinpoint encroachment issues—or for municipalities to find possible trouble spots beyond their official tree census (if they even have one). But by zooming out to a city level, patterns in the tree canopy show off urban greenspace quirks. For example, unexpected tree deserts can be identified and neighborhoods that would most benefit from a surge of saplings revealed.

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*MZcIQRCAJX5fbn0Zw6cPlA.jpeg)

New York City’s tree canopy by Descartes Labs. Tree prominence is concentrated in obvious places like parks and cemeteries, but also around certain neighborhoods (like leafy Ditmas Park in Brooklyn and New Brighton on Staten Island). Tree deserts are apparent in Midtown (except Bryant Park!) and the industrial parks of Queens, as well as scattered throughout the city (e.g., Rikers Island Prison Complex).

Below is a **parting shot**.Scroll through this New York City tree image and notice how the landscape of trees ebbs and flows throughout. Trees blanket parks, cemeteries, housing development courtyards, the streets of affluent residential neighborhoods like the West Village and The Upper East Side, and the edges of rail lines (that’s a freight rail line that cuts across Brooklyn east to west!). But trees have been pushed out of highly-trafficked areas like Times Square and Downtown Brooklyn.

The pattern of trees in any city reveals something about its urban planning history and legacy of greenspace. Just looking at these, don’t you want to know what your city’s treescape looks like?

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*VKE7KlJHIdAgPWY6H3chqw.png)

**Also, Miami!**

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*-tCyw8oqzAgeEumRE5zKQg.jpeg)

**Oh, and why not Minneapolis too?**

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*ptVHlCZYHD1cqPRjWiIDzA.jpeg)

## Responses (13)

Write a response[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdescarteslabs-team%2Fdescartes-labs-urban-trees-tree-canopy-mapping-3b6c85c5c9cc&source=---post_responses--3b6c85c5c9cc---------------------respond_sidebar------------------)

```c
How can I access this data to compute things like tree canopy % by city?
```

2

```c
Hi Tim, this is amazing- could I ask if we could discuss this methodology further? I’m working on urban forestry at the University of Sheffield and would be really interested in seeing if we could combine this with other datasets to describe urban environmental niches
```

1

```c
This is great stuff. BTW, like San Francisco and NYC, Baltimore also completed a tree inventory which indicates that the canopy grew by 1% from 2007–2015: http://baltimore.maps.arcgis.com/apps/webappviewer/index.html?id=b4d5f007c0974e2aa575295654919545
```

1

## More from Tim Wallace and descarteslabs-meditations

## Recommended from Medium

[

See more recommendations

](https://medium.com/?source=post_page---read_next_recirc--3b6c85c5c9cc---------------------------------------)