# Descriptor Animations for MM3E - Notion Reference

**Source:** https://www.notion.so/Descriptor-Animations-for-MM3E-166b3a3d89ed809fbdf5d7d368748ad8

## Overview

The `mm3e-animations` module allows you to execute sequencer and automated animations that are looked up based on the descriptor and power effect of the item being clicked on.

## Why Would Anyone Want This?

Building a complete list of animations for an effects-based system like Mutants and Masterminds is basically impossible. Effects-based systems allow players to define the exact power they want by purchasing a game effect for their character (like damage for instance), applying one or more modifiers (like range and area effect), and then finally a descriptor (like fire, or maybe a thrown hammer).

This module aims to make it possible to create animations based on the descriptor/effect/modifier combination of a power item, with the goal of defining reusable components that can be mixed and matched in order to support an infinite combination of unique powers!

### Example: Fire Powers Animation

To animate all combinations of fire powers that could be created in the mm3e system, you define:

1. **A common fire range cast effect** - Animation that plays when casting a ranged fire power
2. **A common fire melee cast effect** - Animation that plays when casting a melee fire power  
3. **A common fire project effect** - Animation that projects from caster to target for ranged fire powers
4. **A common fire affect sequence** for every power effect that could reasonably be used by the fire descriptor:
   - Damage
   - Affliction
   - Transform
   - etc.

### How It Works

An interpreter activates whenever a player clicks on a power. This interpreter determines what effect components are required to animate that power by looking at:

1. **The descriptor** on the power item (e.g., Fire)
2. **The range type** (range, melee, or personal)
3. **An area shape** (for instance Burst or Line)
4. **The actual power effect** of the item (for instance Damage or Affliction)

## What This Module Provides

1. **Mechanism to invoke animation** based on the descriptor, range type, optional area shape, and power-effects of an item being clicked

2. **Support for automated animations entries and sequencer macros** that are named using the `<descriptor>-<range type>-<area shape>-<power effect>` convention, including a sample Autorec file with a set of pre-labelled entries for various descriptor-range-area-effect combinations out of the box.

3. **Collection of bespoke sequencer scripts** that have been componentized into various descriptor-range-area-power effect scripts that can be mixed and matched. These exist for Earth, Air, Fire, and Radiation with many more on the way!

4. **Custom UI** that enables quick mixing and matching of the above sequencer scripts into customized macros

## Module Dependencies

- **Sequencer** - For all bespoke descriptor animations (MUST HAVE)
- **JB2A Patreon** - Many animations rely on JB2A assets (highly recommended)
- **NOTE FOR NEW SYSTEM**: Automated Animations (autorec) integration is NOT needed - we will focus solely on Sequencer-based animations
- **Jacks Cartoon Spell Effects** - Many animations use this (highly recommended)
- **Jinkers Animation** - A few animations use this
- **FXMaster** - Occasionally relied upon
- **Token Magic FX** - Small reliance

## Animation Content Providers

Many of the animations rely on animation modules to provide the actual animations for the sequencer. These include:
- JB2A
- Jacks Cartoon Spell Effects
- Jinkers Animation
- Others mentioned on the website

## Quick Usage Tutorial

1. Install the module and activate in your world
2. Import the autorec file that comes with this module
3. Open any character
4. Edit a power item and enter:
   - A descriptor
   - A range type
   - A power effect
   - Optionally an area effect shape
5. Validate if there is a descriptor animation that can be looked up for your power item
6. Play the power item! Select attacker and target, then click the power attack button
7. Test with example characters and look through example macros
8. (Optional) Install sound files

## Animation Lookup Types

The module looks up animations in this order:

1. **match** - A macro with a name matching `<descriptor>-<range type>-<area shape>-<power effect>` was found
2. **autorec** - An entry was found in automated animations global rec that matched the pattern
3. **descriptor** - A descriptor-based effect was able to dynamically build a sequencer script based on the pattern

## Descriptor Sequencer Builder UI

The UI allows customization of animations with sections for:
- **Cast sequencer effect** for the power item
- **Project sequencer effect** for the power item (if ranged only)
- **Who is affected** by the animation (the selected or the target)
- **Power-effects** you want animated by sequencer

These values are auto-selected by the module to best match the attributes of the power item.

Currently works for Radiation, Earth, Air and Ice. Water, Electricity, and Holy coming soon, with Super Strength, Insect, and Super Speed making a fast follow.

## Key Concepts

- **Component-based approach**: Reusable animation components that can be mixed and matched
- **Descriptor-based lookup**: Animations are found/assembled based on descriptor + range + area + effect
- **Dynamic script generation**: Can build sequencer scripts on the fly from components
- **Visual editor**: UI for rapidly assembling sequencer components

## What We're Changing for New System

- **What**: Same - animations based on descriptor/range/area/effect combinations
- **Why**: Same - support infinite power combinations with reusable components
- **How**: Different - 
  - Visual editor for rapidly assembling Sequencer components
  - Standardized component library (Self, Project, Target, etc.)
  - Better abstraction of Sequencer details
  - Integration with new foundry-mm3 system (not legacy system)
  - Better Attacks functionality now built into core system (not separate module)

