# MM3E Animations Story Map

## 1. Animate
### 1.1 Skills/Abilities
- Determine + Display FX components based on selectors / character specific) with SKill/Ability 
- Associate + Display FX components based on selectors of contributing power of Abiity / Skill 
- Animate skill/ability using associated FX
- Disable FX for ability/skill




### 1.2 Effects
- Associate + Display FX (selectors / character specific) with Effect  
- Animate self Effect 
- Animate Area Attack Effect 
- Animate Ranged Attack Effect 
- Animate Melee Attack Effect
- Animate Miss vs Hit Attack Effect
- Animate Reaction Attack Effect
- Animate Defended Attack Effect (no condition)
- Animate Condition Attack Effect
- Animate Movement
- Animate Linked Effect / Stacked Effect

## 2. Edit Animations
### 2.1 Associate Animation With Item
- Edit Sequencer FX components and display Animation Builder for item
- Filter FX components based on Selector attributes of Item Being Animated (Skill / Ability / Effect / Manuevers)
- Select FX Component for Item Being Animated
- Edit FX sequencer code directly for Item Being Animated

### 2.2 Assign FX Components to Selectors
- Create / remove FX Component for selector
- Move FX component to another selector
- Associate FX component with selected selectors
- Associate Sequencer Fragment with Descriptor FX Selector
-> Always run this caster sequencer for all fire powers
-> type:descriptor value: fire

- Associate Sequencer Fragment with Effect FX Selector
-> Always run this targeted sequencer for all damage powers
-> type:descriptor value: default
-> type:effect value: damage

- Associate Sequencer Fragment with Descriptor + Range FX Selector
-> Always run this projection sequencer for all fire range powers
-> type:descriptor value: fire
-> type: range value: ranged

- Associate Sequencer Fragment with Descriptor and Effect FX Selector
-> Always run this targeted sequencer for all fire damage powers
-> type:effect value: damage
-> type:descriptor value: fire
-> fire.ranged.damage

- Associate Sequencer Fragment with Descriptor, Effect, and Range Attribute
-> only run this projection sequencer for fire range powers that are also damage
-> type:descriptor value: fire
-> type: range value: ranged
-> type:effect value: damage

- Associate Sequencer Fragment with Descriptor, Effect, Range, Duration
-> only run this targeted sequencer for fire range powers that are also protection, with duration of sustained
-> type:descriptor value: fire
-> type: range value: self
-> type:effect value: protection
-> type:duration value: sustained

### 2.3 Edit Selector Tree
- Display FX selectors tree
- Display FX component for expanded selectors
- Order Selector Tree by specific selector type 
- Edit / add / Remove Selector (incl.  descriptors)

### 2.4 Edit FX Component
- Edit FX component
- Add / Delete FX Component 
- Build Caster FX Component
- Build Projected FX Component
- Build Targeted FX Component 
- Build Area FX Component
- Duplicate FX Component


