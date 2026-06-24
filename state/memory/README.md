# memory/

working memory the agent reads and writes during operation. unlike the ledger and audit log, this is mutable.

the distinction matters: memory is what the agent is thinking about right now. the ledger is the permanent record of what it decided and why. a model swap discards nothing important from memory because everything that mattered was committed to the ledger as a reasoned decision. memory can be cold-started; the ledger cannot be lost.

keep memory small and disposable. if something here needs to survive a swap, it belongs in the ledger.
