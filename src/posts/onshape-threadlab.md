---
title: "3D modeling threads in OnShape"
publishDate: 2026-04-18
published: true
---

OnShape[^1] offers two types of tools for drawing threads: hole and external thread. They are great when you draw parts because the tool links the information in the CAD model to the drawing with the right information. The only downside is when you start to design parts for a 3D printer, OnShape[^1] defines the surface as an internal or external thread but it doesn't represent it in the 3D model. In some cases, the thread will be 3D printed so it needs to be represented as a 3D object in the model.

Here comes a great tool called [ThreadLab](https://forum.onshape.com/discussion/19009/threadlab-internal-external-modeled-cosmetic-threads-with-external-thread-callouts/), developed by [antlu56](https://forum.onshape.com/profile/activity/antlu65).

## Installation

1. In the toolbar, click on the button `Add custom features`
   ![Add custom feature](/img/onshape-threadlab/addCustomFeature.png)
2. Past the FeatureScript link in the URL area: https://cad.onshape.com/documents/5c0528b62c1fbb13a2a0e739/w/9f9185ce078357d93c7d0853/e/7cbb452d4d5e963a034ce616
3. Click on the module name in the list
   ![Select the module](/img/onshape-threadlab/selectCustomFeature.png)

## Usage

1. Draw a hole for an internal thread or a cylinder for an external one
2. Select the desired hole or cylinder
   ![Internal cylinder selected](/img/onshape-threadlab/externalCylinderSelected.png)
3. Open the ThreadLab tool
4. Configure the thread as needed. For 3D printing, don't forget to select the tab `Modeled` to have the thread modeled on the part.
   ![External thread](/img/onshape-threadlab/externalThread.png)

[^1]: [OnShape](https://onshape.com) is a CAD software developed by PTC
