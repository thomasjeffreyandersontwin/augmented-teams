ActorTemplate
    Define minion type: MinionMember,FoundryActor

BoardToken
    Represent minion visually: MinionMember,FoundryScene

CombatAction
    Apply to target: CombatTarget,MinionMember

CombatTarget
    Receive mob attack: BoardToken,CombatAction

MinionMember
    Participate in mob: Mob
    Perform individual action: BoardToken,CombatAction

Mob
    Group minions together: MinionMember
    Execute collective actions: CombatAction,TargetingStrategy

MobTemplate
    Define mob composition: Mob,ActorTemplate
    Spawn mob instances: Mob,FoundryScene

MovementPath
    Represent path waypoints: PathfindingStrategy,FoundryScene
    Validate path accessibility: Mob,BoardToken

PathfindingStrategy
    Get movement path: Mob,FoundryScene
    Identify obstacles: FoundryScene,BoardToken

TargetingStrategy
    Identify targets by criteria: CombatTarget,Mob
