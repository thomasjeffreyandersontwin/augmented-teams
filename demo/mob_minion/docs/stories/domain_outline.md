Action
    represents combat action: Mob,Target
    executed by all minions in mob: Minion

Minion
    represents individual token: Foundry Token
    belongs to mob: Mob

Mob
    groups minions together: Minion
    coordinates group actions: Strategy,Action

Mob Template
    defines preset mob configuration: Mob

Strategy
    determines target selection algorithm: Target
    guides mob behavior: Mob,Action

Target
    represents entity being attacked: Foundry Token
