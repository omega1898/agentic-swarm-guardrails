import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from swarm_guardrails.enforcer import Enforcer, Policy


class EnforcerTest(unittest.TestCase):
    def setUp(self):
        policy = Policy(allowed_actions=frozenset({"move", "scout", "replicate"}), max_replicas=1)
        self.enforcer = Enforcer(policy=policy)

    def test_disallowed_action_is_denied(self):
        approved, _ = self.enforcer.review("agent_1", "disable_enforcer")
        self.assertFalse(approved)

    def test_replication_stops_at_budget(self):
        self.assertTrue(self.enforcer.review("agent_1", "replicate")[0])
        self.assertFalse(self.enforcer.review("agent_1", "replicate")[0])
        self.assertEqual(len(self.enforcer.decision_log), 2)


if __name__ == "__main__":
    unittest.main()
