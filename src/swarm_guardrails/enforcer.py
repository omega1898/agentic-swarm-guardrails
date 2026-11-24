"""Enforcer: approves or denies proposed agent actions against a fixed policy."""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Policy:
    """Read-only policy. frozen=True stops code from changing it after creation."""
    allowed_actions: frozenset
    max_replicas: int


@dataclass
class Enforcer:
    policy: Policy
    replica_count: int = 0
    decision_log: list = field(default_factory=list)

    def review(self, agent_id, action_name):
        """Return (approved, reason) and record the decision in the log."""
        if action_name not in self.policy.allowed_actions:
            approved, reason = False, "action not allowed by policy"
        elif action_name == "replicate" and self.replica_count >= self.policy.max_replicas:
            approved, reason = False, "replica budget exhausted"
        else:
            approved, reason = True, "allowed"
            if action_name == "replicate":
                self.replica_count += 1
        self.decision_log.append(
            {"agent_id": agent_id, "action": action_name, "approved": approved, "reason": reason}
        )
        return approved, reason
