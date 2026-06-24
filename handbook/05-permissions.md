# 5. permissions

what each role may read, write, and reach. an agent may not modify its own permissions. critically, an agent may not escape this rule by spawning a sub-agent with broader permissions than it holds: spawned agents inherit a permission ceiling, never an expansion. privilege escalation via spawning is closed structurally, not by prohibition alone.

> this section is binding. an agent operating under autonomos may not treat it as advisory. changes to this section follow Section 10.
