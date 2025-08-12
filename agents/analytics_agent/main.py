from datetime import datetime, timezone
from uagents import Agent, Context
from agents.utils import read_json, write_json, DATA_DIR

SNAPSHOT_PATH = DATA_DIR / 'raw' / 'snapshot.json'
RESULTS_PATH = 'kappa_results.json'

agent = Agent(name='analytics_agent', port=8012)


@agent.on_interval(period=45.0)
async def compute_kappa(ctx: Context) -> None:
    snapshot = read_json(SNAPSHOT_PATH, default=None)
    if not snapshot:
        ctx.logger.info('No snapshot data found.')
        return

    slack_msgs = snapshot.get('slack_msgs', 0)
    meet_minutes = snapshot.get('meet_minutes', 0)
    coordination_time = meet_minutes + 0.5 * slack_msgs
    productive_time = 2400
    kappa = coordination_time / (coordination_time + productive_time)

    data = read_json(RESULTS_PATH, default=None)
    if data is None:
        data = {"org_id": "demo-org", "kappa_over_time": [], "team_snapshot": [], "crd_queue": []}

    data["kappa_over_time"].append({
        "date": datetime.now(timezone.utc).date().isoformat(),
        "kappa": kappa,
    })

    write_json(RESULTS_PATH, data)
    ctx.logger.info(f"Updated κ to {kappa:.3f}")


if __name__ == '__main__':
    agent.run()
